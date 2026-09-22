#!/usr/bin/env python3
"""Build the JEV Project Atlas from public, source-backed inputs.

The script intentionally keeps two layers separate:
1. verified-projects.json: projects that have commit-pinned source evidence.
2. discovered-repos.json: every repository visible under GitHub's `jev` topic.

Only Python's standard library is required.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"
UPSTREAM_DATA = (
    "https://raw.githubusercontent.com/logicrw/awesome-jev-projects/"
    "main/src/data/projects.json"
)
TOPIC_PAGE = "https://github.com/topics/jev?page={page}"
SEARCH_API = "https://api.github.com/search/repositories"
USER_AGENT = "jev-project-atlas/1.0 (+https://github.com/topics/jev)"
REPO_LINK = re.compile(r'href="/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)"')
TOPIC_CARD = re.compile(r'<article class="border rounded.*?</article>', re.DOTALL)
IGNORED_OWNERS = {"topics", "sponsors", "collections", "events", "marketplace"}


def fetch_text(url: str, retries: int = 3) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.read().decode("utf-8")
        except (urllib.error.URLError, TimeoutError):
            if attempt + 1 == retries:
                raise
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"Unable to fetch {url}")


def fetch_search_page(query: str, page: int, retries: int = 4) -> dict[str, Any]:
    params = urllib.parse.urlencode(
        {"q": query, "sort": "stars", "order": "desc", "per_page": 100, "page": page}
    )
    url = f"{SEARCH_API}?{params}"
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as error:
            if error.code not in {403, 429} or attempt + 1 == retries:
                raise
            reset = int(error.headers.get("X-RateLimit-Reset", "0") or 0)
            delay = max(2, min(70, reset - int(time.time()) + 2))
            time.sleep(delay)
    raise RuntimeError(f"Unable to fetch {url}")


def fetch_verified() -> list[dict[str, Any]]:
    raw = json.loads(fetch_text(UPSTREAM_DATA))
    projects: list[dict[str, Any]] = []
    for item in raw:
        repo = item.get("repo") or repo_from_url(item.get("url", ""))
        if not repo:
            continue
        projects.append(
            {
                "repo": repo,
                "name": item.get("name") or repo.split("/")[-1],
                "author": item.get("author") or repo.split("/")[0],
                "url": item.get("url") or f"https://github.com/{repo}",
                "category": item.get("category") or "Other",
                "summary_zh": item.get("plainSummary") or "",
                "summary_en": item.get("plainSummaryEn") or "",
                "decision_point_zh": item.get("jevDecisionPoint") or "",
                "benefit_zh": item.get("highlightBenefit") or "",
                "license": item.get("license") or "Unknown",
                "language": item.get("language"),
                "stars": item.get("stars") or 0,
                "forks": item.get("forks") or 0,
                "archived": bool(item.get("archived")),
                "tags": item.get("tags") or [],
                "verification_status": item.get("verificationStatus") or "source-verified",
                "source_url": item.get("sourceUrl"),
                "source_sha": item.get("headSha"),
                "last_synced_at": item.get("lastSyncedAt"),
                "upstream_id": item.get("id"),
            }
        )
    projects.sort(key=lambda p: (-int(p["stars"]), p["repo"].lower()))
    return projects


def repo_from_url(url: str) -> str | None:
    match = re.match(r"https://github\.com/([^/]+/[^/#?]+)", url)
    return match.group(1).removesuffix(".git") if match else None


def fetch_topic_repos(max_pages: int = 100) -> list[dict[str, str]]:
    seen: dict[str, dict[str, str]] = {}

    def load_page(page: int) -> tuple[int, str | None]:
        try:
            return page, fetch_text(TOPIC_PAGE.format(page=page))
        except urllib.error.HTTPError as error:
            if error.code == 404 and page > 1:
                return page, None
            raise

    pages: dict[int, str | None] = {}
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = [pool.submit(load_page, page) for page in range(1, max_pages + 1)]
        for future in as_completed(futures):
            page, markup = future.result()
            pages[page] = markup

    empty_pages = 0
    for page in range(1, max_pages + 1):
        markup = pages.get(page)
        if markup is None:
            break
        page_repos: list[str] = []
        cards = TOPIC_CARD.findall(markup)
        for card in cards:
            match = REPO_LINK.search(card)
            if not match:
                continue
            repo = html.unescape(match.group(1)).strip("/")
            owner, name = repo.split("/", 1)
            if owner.lower() in IGNORED_OWNERS or name.lower() in {"followers", "following"}:
                continue
            page_repos.append(repo)
            key = repo.lower()
            seen.setdefault(
                key,
                {
                    "repo": repo,
                    "url": f"https://github.com/{repo}",
                    "topic_page": page,
                },
            )

        if not page_repos:
            empty_pages += 1
        else:
            empty_pages = 0
        if empty_pages >= 2:
            break

    return sorted(seen.values(), key=lambda item: item["repo"].lower())


def fetch_discovered_repos() -> list[dict[str, Any]]:
    # GitHub search caps a query at 1,000 results. Splitting zero-star and
    # starred repositories keeps both partitions below that cap.
    seen: dict[str, dict[str, Any]] = {}
    for query in ("topic:jev stars:>=1", "topic:jev stars:0"):
        first = fetch_search_page(query, 1)
        total = int(first.get("total_count") or 0)
        pages = min(10, (total + 99) // 100)
        payloads = [first]
        for page in range(2, pages + 1):
            payloads.append(fetch_search_page(query, page))
        for payload in payloads:
            for item in payload.get("items", []):
                repo = item.get("full_name")
                if not repo:
                    continue
                seen[repo.lower()] = {
                    "repo": repo,
                    "url": item.get("html_url") or f"https://github.com/{repo}",
                    "description": item.get("description") or "",
                    "stars": item.get("stargazers_count") or 0,
                    "forks": item.get("forks_count") or 0,
                    "language": item.get("language"),
                    "license": (item.get("license") or {}).get("spdx_id"),
                    "archived": bool(item.get("archived")),
                    "topics": item.get("topics") or [],
                    "updated_at": item.get("updated_at"),
                }
    return sorted(seen.values(), key=lambda item: item["repo"].lower())


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def escape_cell(value: Any) -> str:
    text = str(value or "").replace("|", "\\|").replace("\n", " ").strip()
    return text if len(text) <= 180 else text[:177].rstrip() + "…"


def generate_catalog(projects: list[dict[str, Any]], stamp: str) -> str:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for project in projects:
        grouped.setdefault(project["category"], []).append(project)

    lines = [
        "# JEV 已核验项目目录",
        "",
        f"> 数据快照：{stamp} · 共 **{len(projects)}** 个项目 · 按源码证据核验，不等同于运行时安全审计。",
        "",
        "[返回首页](README.md) · [方法说明](METHODOLOGY.md) · [机器可读数据](data/verified-projects.json)",
        "",
        "## 分类导航",
        "",
    ]
    for category in sorted(grouped):
        anchor = re.sub(r"[^a-z0-9\u4e00-\u9fff-]+", "-", category.lower()).strip("-")
        lines.append(f"- [{category} ({len(grouped[category])})](#{anchor})")

    for category in sorted(grouped):
        items = grouped[category]
        lines.extend(
            [
                "",
                f"## {category}",
                "",
                "| 项目 | 简介 | 语言 | ⭐ | 许可证 | 证据 |",
                "|---|---|---:|---:|---:|---|",
            ]
        )
        for item in items:
            evidence = (
                f"[固定提交]({item['source_url']})" if item.get("source_url") else "已核验"
            )
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"[**{escape_cell(item['repo'])}**]({item['url']})",
                        escape_cell(item["summary_zh"] or item["summary_en"]),
                        escape_cell(item.get("language") or "—"),
                        str(item.get("stars") or 0),
                        escape_cell(item.get("license") or "Unknown"),
                        evidence,
                    ]
                )
                + " |"
            )
    lines.extend(["", "---", "", "发现遗漏？请提交 Issue，并附上仓库地址与 JEV 使用位置。", ""])
    return "\n".join(lines)


def generate_readme(
    projects: list[dict[str, Any]], discovered: list[dict[str, Any]], stamp: str
) -> str:
    categories = Counter(p["category"] for p in projects)
    languages = Counter(p.get("language") or "Unknown" for p in projects)
    top_projects = sorted(projects, key=lambda p: -int(p.get("stars") or 0))[:10]
    verified_keys = {p["repo"].lower() for p in projects}
    topic_verified = sum(1 for item in discovered if item["repo"].lower() in verified_keys)
    top_category_rows = "\n".join(
        f"| {name} | {count} |" for name, count in categories.most_common()
    )
    top_project_rows = "\n".join(
        f"| [{p['repo']}]({p['url']}) | {escape_cell(p['summary_zh'] or p['summary_en'])} | {p.get('stars', 0)} | {p.get('license') or 'Unknown'} |"
        for p in top_projects
    )
    language_line = " · ".join(f"{name} {count}" for name, count in languages.most_common(8))
    return f"""<div align=\"center\">

<img src=\"assets/banner.svg\" alt=\"JEV Project Atlas\" width=\"100%\" />

# JEV Project Atlas · JEV 项目全景图

**发现、核验并总结 GitHub 上的 JEV / TypeSafe System One 项目。**

[![Verified](https://img.shields.io/badge/source--verified-{len(projects)}-2dd4bf?style=flat-square)](CATALOG.md)
[![Discovered](https://img.shields.io/badge/topic--discovered-{len(discovered)}-60a5fa?style=flat-square)](data/discovered-repos.json)
[![Updated](https://img.shields.io/badge/updated-{stamp.replace('-', '--')}-a78bfa?style=flat-square)](METHODOLOGY.md)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=flat-square)](LICENSE)

[完整目录](CATALOG.md) · [在线搜索](https://periodblue.github.io/jev-project-atlas/) · [方法与边界](METHODOLOGY.md) · [贡献项目](CONTRIBUTING.md)

</div>

## 一眼看懂

JEV 是 TypeSafe AI 面向分类、路由、评分、排序、验证与安全门控等任务的快速、类型化决策模型。本仓库不是简单复制 GitHub 搜索结果，而是把生态分成两个互不混淆的层级：

| 层级 | 数量 | 含义 |
|---|---:|---|
| ✅ 源码已核验 | **{len(projects)}** | 有固定提交的源码证据，能定位 JEV 在哪里做决策 |
| 🔭 Topic 已发现 | **{len(discovered)}** | GitHub `jev` topic 的完整快照，包含待核验项目与噪声 |
| 🔗 Topic 中已核验 | **{topic_verified}** | 同时出现在发现层和核验层的项目 |

> [!IMPORTANT]
> “已核验”表示查看过公开源码证据，不代表项目已做安全审计、性能复现或生产可用性背书。JEV 本体是托管模型；开源 SDK、集成和兼容实现不等于开放模型权重。

## 值得先看的项目

| 项目 | 做什么 | ⭐ | 许可证 |
|---|---|---:|---|
{top_project_rows}

## 生态分布

| 分类 | 项目数 |
|---|---:|
{top_category_rows}

主要语言：{language_line}

## 如何使用

- 想找可直接用的项目：打开 [完整目录](CATALOG.md)，按领域浏览。
- 想搜索、筛选、排序：打开 [在线搜索页面](https://periodblue.github.io/jev-project-atlas/)。
- 想做分析或二次开发：使用 [已核验 JSON](data/verified-projects.json) 和 [完整发现 JSON](data/discovered-repos.json)。
- 想提交遗漏：阅读 [贡献指南](CONTRIBUTING.md)，请附仓库地址和 JEV 的源码使用位置。

## 数据更新

```bash
python scripts/sync.py
```

脚本只依赖 Python 标准库，会重新抓取 GitHub topic、同步公开的源码核验数据并重建目录与搜索页。自动更新工作流每周运行一次，也可以手动触发。

## 数据来源与致谢

已核验层基于 [logicrw/awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects) 的 MIT 许可数据，并在本仓库中进行字段规范化、分层和重新呈现；发现层直接来自 [GitHub `jev` topic](https://github.com/topics/jev)。详见 [第三方声明](THIRD_PARTY_NOTICES.md)。

## 许可证

本仓库代码与原创内容采用 [MIT License](LICENSE)。各项目仍遵循它们各自的许可证；数据来源及再分发条款见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
"""


def generate_docs_data(projects: list[dict[str, Any]], stamp: str) -> str:
    compact = {
        "updated": stamp,
        "projects": projects,
    }
    return "window.JEV_ATLAS = " + json.dumps(compact, ensure_ascii=False) + ";\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Refresh the JEV Project Atlas")
    parser.add_argument("--max-pages", type=int, default=100)
    args = parser.parse_args()

    stamp = dt.datetime.now(dt.timezone.utc).date().isoformat()
    projects = fetch_verified()
    try:
        discovered = fetch_discovered_repos()
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as error:
        print(f"Search API unavailable ({error}); falling back to topic pages.")
        discovered = fetch_topic_repos(args.max_pages)
    verified_keys = {p["repo"].lower() for p in projects}
    for item in discovered:
        item["verification"] = (
            "source-verified" if item["repo"].lower() in verified_keys else "unverified"
        )

    write_json(
        DATA_DIR / "verified-projects.json",
        {
            "meta": {
                "updated": stamp,
                "count": len(projects),
                "source": UPSTREAM_DATA,
                "source_license": "MIT",
            },
            "projects": projects,
        },
    )
    write_json(
        DATA_DIR / "discovered-repos.json",
        {
            "meta": {
                "updated": stamp,
                "count": len(discovered),
                "source": "https://github.com/topics/jev",
                "scope_note": "Topic membership is self-assigned and is not proof of JEV usage.",
            },
            "repositories": discovered,
        },
    )
    (ROOT / "CATALOG.md").write_text(generate_catalog(projects, stamp), encoding="utf-8")
    (ROOT / "README.md").write_text(
        generate_readme(projects, discovered, stamp), encoding="utf-8"
    )
    (DOCS_DIR / "data.js").write_text(generate_docs_data(projects, stamp), encoding="utf-8")
    print(f"verified={len(projects)} discovered={len(discovered)} updated={stamp}")


if __name__ == "__main__":
    main()
