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
                "decision_point_en": item.get("jevDecisionPointEn") or "",
                "benefit_zh": item.get("highlightBenefit") or "",
                "benefit_en": item.get("highlightBenefitEn") or "",
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


def generate_catalog(projects: list[dict[str, Any]], stamp: str, locale: str = "en") -> str:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for project in projects:
        grouped.setdefault(project["category"], []).append(project)

    zh = locale == "zh"
    lines = (
        [
            "# JEV 已核验项目目录",
            "",
            "[English](CATALOG.md) · **简体中文**",
            "",
            f"> 数据快照：{stamp} · 共 **{len(projects)}** 个项目 · 按源码证据核验，不等同于运行时安全审计。",
            "",
            "[返回首页](README.zh-CN.md) · [方法说明](METHODOLOGY.zh-CN.md) · [机器可读数据](data/verified-projects.json)",
            "",
            "## 分类导航",
            "",
        ]
        if zh
        else [
            "# Source-verified JEV project catalog",
            "",
            "**English** · [简体中文](CATALOG.zh-CN.md)",
            "",
            f"> Snapshot: {stamp} · **{len(projects)}** projects · Verified from public source evidence; not a runtime or security audit.",
            "",
            "[Back to README](README.md) · [Methodology](METHODOLOGY.md) · [Machine-readable data](data/verified-projects.json)",
            "",
            "## Browse by category",
            "",
        ]
    )
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
                (
                    "| 项目 | 简介 | 语言 | ⭐ | 许可证 | 证据 |"
                    if zh
                    else "| Project | What it does | Language | ⭐ | License | Evidence |"
                ),
                "|---|---|---:|---:|---:|---|",
            ]
        )
        for item in items:
            evidence = (
                f"[{'固定提交' if zh else 'Pinned source'}]({item['source_url']})"
                if item.get("source_url")
                else ("已核验" if zh else "Verified")
            )
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"[**{escape_cell(item['repo'])}**]({item['url']})",
                        escape_cell(
                            (item["summary_zh"] or item["summary_en"])
                            if zh
                            else (item["summary_en"] or item["summary_zh"])
                        ),
                        escape_cell(item.get("language") or "—"),
                        str(item.get("stars") or 0),
                        escape_cell(item.get("license") or "Unknown"),
                        evidence,
                    ]
                )
                + " |"
            )
    lines.extend(
        [
            "",
            "---",
            "",
            (
                "发现遗漏？请提交 Issue，并附上仓库地址与 JEV 使用位置。"
                if zh
                else "Missing a project? Open an issue with the repository URL and the exact JEV integration point."
            ),
            "",
        ]
    )
    return "\n".join(lines)


def readme_stats(
    projects: list[dict[str, Any]], discovered: list[dict[str, Any]]
) -> dict[str, Any]:
    categories = Counter(p["category"] for p in projects)
    languages = Counter(p.get("language") or "Unknown" for p in projects)
    top_projects = sorted(projects, key=lambda p: -int(p.get("stars") or 0))[:8]
    verified_keys = {p["repo"].lower() for p in projects}
    topic_verified = sum(1 for item in discovered if item["repo"].lower() in verified_keys)
    return {
        "categories": categories,
        "languages": languages,
        "top_projects": top_projects,
        "topic_verified": topic_verified,
    }


def generate_readme_en(
    projects: list[dict[str, Any]], discovered: list[dict[str, Any]], stamp: str
) -> str:
    stats = readme_stats(projects, discovered)
    category_rows = "\n".join(
        f"| {name} | **{count}** |" for name, count in stats["categories"].most_common()
    )
    project_rows = "\n".join(
        f"| [{p['repo']}]({p['url']}) | {escape_cell(p['summary_en'] or p['summary_zh'])} | **{p.get('stars', 0):,}** | `{p.get('license') or 'Unknown'}` |"
        for p in stats["top_projects"]
    )
    language_line = " · ".join(
        f"`{name}` {count}" for name, count in stats["languages"].most_common(8)
    )
    return f"""<div align=\"center\">

<a href=\"https://periodblue.github.io/jev-project-atlas/\"><img src=\"assets/banner.svg\" alt=\"JEV Project Atlas\" width=\"100%\" /></a>

# JEV Project Atlas

### The source-backed map of the JEV / TypeSafe System One ecosystem.

[![Verified](https://img.shields.io/badge/source--verified-{len(projects)}-2dd4bf?style=for-the-badge)](CATALOG.md)
[![Discovered](https://img.shields.io/badge/topic--discovered-{len(discovered)}-60a5fa?style=for-the-badge)](data/discovered-repos.json)
[![Updated](https://img.shields.io/badge/snapshot-{stamp.replace('-', '--')}-a78bfa?style=for-the-badge)](METHODOLOGY.md)

<a href=\"https://periodblue.github.io/jev-project-atlas/\"><img src=\"https://img.shields.io/badge/Explore_the_live_atlas-0f766e?style=for-the-badge&logo=safari&logoColor=white\" alt=\"Explore the live atlas\" /></a>
<a href=\"CATALOG.md\"><img src=\"https://img.shields.io/badge/Browse_all_projects-1d4ed8?style=for-the-badge&logo=github&logoColor=white\" alt=\"Browse all projects\" /></a>

**English** · [简体中文](README.zh-CN.md)

</div>

> [!TIP]
> **Start with the [interactive atlas](https://periodblue.github.io/jev-project-atlas/)** — search 479 verified projects by domain, language, license, or decision point.

## A map, not a hype list

JEV is TypeSafe AI's fast, typed decision model for classification, routing, scoring, ranking, verification, and guardrails. This atlas separates projects backed by inspectable source evidence from repositories that merely carry a topic label.

<table>
<tr>
<td align=\"center\" width=\"33%\"><h2>{len(projects)}</h2><strong>Source-verified</strong><br><sub>Pinned evidence for the JEV decision point</sub></td>
<td align=\"center\" width=\"33%\"><h2>{len(discovered):,}</h2><strong>Topic-discovered</strong><br><sub>The full public GitHub discovery snapshot</sub></td>
<td align=\"center\" width=\"33%\"><h2>{len(stats['categories'])}</h2><strong>Real-world domains</strong><br><sub>From browser control to model routing</sub></td>
</tr>
</table>

> [!IMPORTANT]
> **Source-verified does not mean security-audited, benchmark-reproduced, or production-endorsed.** JEV itself is a hosted model; open SDKs, integrations, and compatible implementations are not open model weights.

## How trust flows through the atlas

```mermaid
flowchart LR
    A[GitHub discovery] --> B{{Evidence gate}}
    B -->|Pinned source found| C[Verified catalog]
    B -->|Evidence missing| D[Discovery backlog]
    C --> E[Searchable atlas]
    C --> F[JSON datasets]
    C --> G[Weekly refresh]
```

Every verified entry answers three questions: **What does it do? Where does JEV decide? What public source proves it?** The broader topic snapshot is retained for recall, but never presented as verified.

## Projects worth opening first

| Project | Why it matters | Stars | License |
|---|---|---:|---|
{project_rows}

## Explore the ecosystem

| Domain | Projects |
|---|---:|
{category_rows}

**Leading languages:** {language_line}

## Use the atlas your way

| I want to… | Go here |
|---|---|
| Search and filter visually | **[Interactive atlas →](https://periodblue.github.io/jev-project-atlas/)** |
| Read every verified entry | **[Full catalog →](CATALOG.md)** |
| Analyze or build on the data | [Verified JSON](data/verified-projects.json) · [Discovery JSON](data/discovered-repos.json) |
| Audit the inclusion rules | [Methodology](METHODOLOGY.md) |
| Submit a missing project | [Contribution guide](CONTRIBUTING.md) |

## Reproducible by default

```bash
python scripts/sync.py
```

The zero-dependency sync script refreshes GitHub discovery, normalizes the source-reviewed dataset, and rebuilds both languages, both catalogs, and the live explorer. GitHub Actions runs it weekly.

## Provenance

The verified layer builds on the MIT-licensed source review in [logicrw/awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects), normalized and presented here as a two-layer atlas. Discovery comes directly from the [GitHub `jev` topic](https://github.com/topics/jev). See [third-party notices](THIRD_PARTY_NOTICES.md).

## License

Atlas code and original content are [MIT licensed](LICENSE). Listed projects keep their own licenses.
"""


def generate_readme_zh(
    projects: list[dict[str, Any]], discovered: list[dict[str, Any]], stamp: str
) -> str:
    stats = readme_stats(projects, discovered)
    category_rows = "\n".join(
        f"| {name} | **{count}** |" for name, count in stats["categories"].most_common()
    )
    project_rows = "\n".join(
        f"| [{p['repo']}]({p['url']}) | {escape_cell(p['summary_zh'] or p['summary_en'])} | **{p.get('stars', 0):,}** | `{p.get('license') or 'Unknown'}` |"
        for p in stats["top_projects"]
    )
    language_line = " · ".join(
        f"`{name}` {count}" for name, count in stats["languages"].most_common(8)
    )
    return f"""<div align=\"center\">

<a href=\"https://periodblue.github.io/jev-project-atlas/\"><img src=\"assets/banner.svg\" alt=\"JEV Project Atlas\" width=\"100%\" /></a>

# JEV Project Atlas · JEV 项目全景图

### 有源码证据的 JEV / TypeSafe System One 生态地图。

[![Verified](https://img.shields.io/badge/源码核验-{len(projects)}-2dd4bf?style=for-the-badge)](CATALOG.zh-CN.md)
[![Discovered](https://img.shields.io/badge/Topic发现-{len(discovered)}-60a5fa?style=for-the-badge)](data/discovered-repos.json)
[![Updated](https://img.shields.io/badge/数据快照-{stamp.replace('-', '--')}-a78bfa?style=for-the-badge)](METHODOLOGY.zh-CN.md)

<a href=\"https://periodblue.github.io/jev-project-atlas/?lang=zh\"><img src=\"https://img.shields.io/badge/打开在线全景图-0f766e?style=for-the-badge&logo=safari&logoColor=white\" alt=\"打开在线全景图\" /></a>
<a href=\"CATALOG.zh-CN.md\"><img src=\"https://img.shields.io/badge/浏览全部项目-1d4ed8?style=for-the-badge&logo=github&logoColor=white\" alt=\"浏览全部项目\" /></a>

[English](README.md) · **简体中文**

</div>

> [!TIP]
> 建议从[在线项目全景图](https://periodblue.github.io/jev-project-atlas/?lang=zh)开始：可按领域、语言、许可证或决策点搜索 479 个已核验项目。

## 这是一张地图，不是热度榜

JEV 是 TypeSafe AI 面向分类、路由、评分、排序、验证与安全门控的快速类型化决策模型。本项目将有可检查源码证据的真实集成，与仅贴有 topic 标签的候选仓库严格分开。

<table>
<tr>
<td align=\"center\" width=\"33%\"><h2>{len(projects)}</h2><strong>源码已核验</strong><br><sub>能定位 JEV 决策点的固定提交证据</sub></td>
<td align=\"center\" width=\"33%\"><h2>{len(discovered):,}</h2><strong>Topic 已发现</strong><br><sub>GitHub 公开仓库的完整发现快照</sub></td>
<td align=\"center\" width=\"33%\"><h2>{len(stats['categories'])}</h2><strong>真实应用领域</strong><br><sub>从浏览器控制到模型路由</sub></td>
</tr>
</table>

> [!IMPORTANT]
> **源码已核验不代表通过安全审计、性能复现或生产背书。** JEV 本体是托管模型；开源 SDK、集成与兼容实现不等于开放模型权重。

## 可信信息如何进入全景图

```mermaid
flowchart LR
    A[GitHub 全量发现] --> B{{证据门槛}}
    B -->|找到固定源码| C[已核验目录]
    B -->|证据不足| D[待核验发现层]
    C --> E[在线搜索]
    C --> F[JSON 数据]
    C --> G[每周自动更新]
```

每个已核验条目都回答三个问题：**项目做什么？JEV 在哪里决策？哪段公开源码可以证明？** Topic 快照用于查漏，但绝不会被冒充为已核验项目。

## 值得先看的项目

| 项目 | 为什么值得看 | 星标 | 许可证 |
|---|---|---:|---|
{project_rows}

## 探索生态

| 应用领域 | 项目数 |
|---|---:|
{category_rows}

**主要语言：** {language_line}

## 按你的方式使用

| 我想…… | 去这里 |
|---|---|
| 可视化搜索和筛选 | **[在线项目全景图 →](https://periodblue.github.io/jev-project-atlas/?lang=zh)** |
| 阅读全部核验条目 | **[中文完整目录 →](CATALOG.zh-CN.md)** |
| 分析或二次开发 | [已核验 JSON](data/verified-projects.json) · [发现层 JSON](data/discovered-repos.json) |
| 检查收录标准 | [方法与边界](METHODOLOGY.zh-CN.md) |
| 提交遗漏项目 | [贡献指南](CONTRIBUTING.zh-CN.md) |

## 默认可复现

```bash
python scripts/sync.py
```

零依赖同步脚本会刷新 GitHub 发现层、规范化源码核验数据，并重建中英文 README、中英文目录和在线搜索页。GitHub Actions 每周自动运行。

## 数据来源

核验层基于 [logicrw/awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects) 的 MIT 许可源码审查数据，并在本仓库中重新规范化、分层与呈现；发现层直接来自 [GitHub `jev` topic](https://github.com/topics/jev)。详见[第三方声明](THIRD_PARTY_NOTICES.md)。

## 许可证

本仓库代码与原创内容采用 [MIT License](LICENSE)，各被收录项目仍遵循其自身许可证。
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
    (ROOT / "CATALOG.md").write_text(
        generate_catalog(projects, stamp, "en"), encoding="utf-8"
    )
    (ROOT / "CATALOG.zh-CN.md").write_text(
        generate_catalog(projects, stamp, "zh"), encoding="utf-8"
    )
    (ROOT / "README.md").write_text(
        generate_readme_en(projects, discovered, stamp), encoding="utf-8"
    )
    (ROOT / "README.zh-CN.md").write_text(
        generate_readme_zh(projects, discovered, stamp), encoding="utf-8"
    )
    (DOCS_DIR / "data.js").write_text(generate_docs_data(projects, stamp), encoding="utf-8")
    print(f"verified={len(projects)} discovered={len(discovered)} updated={stamp}")


if __name__ == "__main__":
    main()
