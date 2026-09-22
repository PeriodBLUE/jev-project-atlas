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
    by_repo = {project["repo"].lower(): project for project in projects}

    def item(repo: str) -> str:
        project = by_repo[repo.lower()]
        summary = html.escape(project["summary_en"] or project["summary_zh"])
        return f'<a href="{project["url"]}"><strong>{project["repo"]}</strong></a><br><sub>{summary}</sub>'

    return f"""<div align=\"center\">

<a href=\"https://periodblue.github.io/jev-project-atlas/\"><img src=\"assets/banner.svg\" alt=\"JEV Project Atlas\" width=\"100%\" /></a>

### Know which JEV projects are real.

**{len(projects)} projects with pinned source evidence — searchable by use case, language, license, and the exact point where JEV makes a decision.**

[![verified](https://img.shields.io/badge/source_verified-{len(projects)}-14b8a6?style=flat-square)](CATALOG.md)
[![discovered](https://img.shields.io/badge/topic_discovered-{len(discovered)}-3b82f6?style=flat-square)](data/discovered-repos.json)
[![updated](https://img.shields.io/badge/updated-{stamp.replace('-', '--')}-8b5cf6?style=flat-square)](METHODOLOGY.md)
[![license](https://img.shields.io/badge/license-MIT-f59e0b?style=flat-square)](LICENSE)

**[Explore the live atlas →](https://periodblue.github.io/jev-project-atlas/)** &nbsp;·&nbsp; [Browse the catalog](CATALOG.md) &nbsp;·&nbsp; [Use the data](#use-the-data)

**English** · [简体中文](README.zh-CN.md)

</div>

<br>

<a href=\"https://periodblue.github.io/jev-project-atlas/\"><img src=\"assets/atlas-preview.png\" alt=\"JEV Project Atlas interactive explorer\" width=\"100%\" /></a>

<p align=\"center\"><sub>Search the verified ecosystem in the <a href=\"https://periodblue.github.io/jev-project-atlas/\">interactive explorer</a>.</sub></p>

## The JEV ecosystem, without the noise

GitHub has **{len(discovered):,} repositories tagged `jev`**. A topic tells you almost nothing: the project may call JEV in production, mention it in a roadmap, imitate its interface, or simply carry a noisy label.

**JEV Project Atlas tells those apart.** It keeps every discoverable lead, but only promotes a project after its public source reveals the actual integration or decision point.

<table>
<tr>
<td align=\"center\" width=\"33%\"><h2>{len(projects)}</h2><b>verified projects</b><br><sub>each linked to immutable source</sub></td>
<td align=\"center\" width=\"33%\"><h2>{len(stats['categories'])}</h2><b>application domains</b><br><sub>from agents to databases</sub></td>
<td align=\"center\" width=\"33%\"><h2>{len(discovered):,}</h2><b>repos monitored</b><br><sub>the recall layer stays searchable</sub></td>
</tr>
</table>

## Start exploring

<table>
<tr>
<td width=\"33%\" valign=\"top\"><h3>🧩 Build with JEV</h3>{item('vercel/ai')}<br><br>{item('langchain-ai/langchain')}<br><br>{item('pydantic/pydantic-ai')}</td>
<td width=\"33%\" valign=\"top\"><h3>⚡ See it decide</h3>{item('browser-use/jev-ultrafast')}<br><br>{item('trycua/cua')}<br><br>{item('realZachi/pg-jev')}</td>
<td width=\"33%\" valign=\"top\"><h3>🧪 Run the shape locally</h3>{item('jaredpalmer/kev')}<br><br>{item('featherless-ai/simple-jev')}</td>
</tr>
</table>

**[See all {len(projects)} verified projects →](CATALOG.md)**

## Why trust this list?

1. **Discover broadly.** The sync scans the whole public `jev` topic, split to avoid GitHub's 1,000-result search cap.
2. **Verify narrowly.** A project enters the catalog only when a reviewer can point to an immutable source file where JEV is called, adapted, or reimplemented.
3. **Explain plainly.** Every entry says what the project does, where JEV decides, and what evidence supports the claim.

> [!NOTE]
> “Verified” means the public source was inspected. It does **not** mean security-audited, benchmark-reproduced, or production-endorsed. JEV itself is hosted; open SDKs and compatible projects are not open JEV weights.

## Use the data

Both layers are committed as clean JSON. For example, list verified Python projects:

```bash
curl -sL https://raw.githubusercontent.com/PeriodBLUE/jev-project-atlas/main/data/verified-projects.json \\
  | jq -r '.projects[] | select(.language == "Python") | .repo'
```

- [`verified-projects.json`](data/verified-projects.json) — curated entries, summaries, categories, metadata, and pinned source evidence.
- [`discovered-repos.json`](data/discovered-repos.json) — the complete discovery snapshot, including unverified leads.

## Keep it current

```bash
python scripts/sync.py
```

No package install. The standard-library script refreshes discovery and rebuilds the English and Chinese READMEs, catalogs, datasets, and explorer. GitHub Actions runs it every week.

---

<p align=\"center\"><b>Found something missing?</b> <a href=\"CONTRIBUTING.md\">Submit a project</a> · <a href=\"METHODOLOGY.md\">Read the methodology</a> · <a href=\"THIRD_PARTY_NOTICES.md\">Provenance</a> · <a href=\"LICENSE\">MIT License</a></p>
"""


def generate_readme_zh(
    projects: list[dict[str, Any]], discovered: list[dict[str, Any]], stamp: str
) -> str:
    stats = readme_stats(projects, discovered)
    by_repo = {project["repo"].lower(): project for project in projects}

    def item(repo: str) -> str:
        project = by_repo[repo.lower()]
        summary = html.escape(project["summary_zh"] or project["summary_en"])
        return f'<a href="{project["url"]}"><strong>{project["repo"]}</strong></a><br><sub>{summary}</sub>'

    return f"""<div align=\"center\">

<a href=\"https://periodblue.github.io/jev-project-atlas/\"><img src=\"assets/banner.svg\" alt=\"JEV Project Atlas\" width=\"100%\" /></a>

### 看清哪些 JEV 项目是真的。

**{len(projects)} 个项目附有固定源码证据，可按用途、语言、许可证以及 JEV 的准确决策点搜索。**

[![verified](https://img.shields.io/badge/源码已核验-{len(projects)}-14b8a6?style=flat-square)](CATALOG.zh-CN.md)
[![discovered](https://img.shields.io/badge/Topic已发现-{len(discovered)}-3b82f6?style=flat-square)](data/discovered-repos.json)
[![updated](https://img.shields.io/badge/更新-{stamp.replace('-', '--')}-8b5cf6?style=flat-square)](METHODOLOGY.zh-CN.md)
[![license](https://img.shields.io/badge/许可证-MIT-f59e0b?style=flat-square)](LICENSE)

**[打开在线全景图 →](https://periodblue.github.io/jev-project-atlas/?lang=zh)** &nbsp;·&nbsp; [浏览完整目录](CATALOG.zh-CN.md) &nbsp;·&nbsp; [使用数据](#使用数据)

[English](README.md) · **简体中文**

</div>

<br>

<a href=\"https://periodblue.github.io/jev-project-atlas/?lang=zh\"><img src=\"assets/atlas-preview.png\" alt=\"JEV Project Atlas 在线项目全景图\" width=\"100%\" /></a>

<p align=\"center\"><sub>在<a href=\"https://periodblue.github.io/jev-project-atlas/?lang=zh\">在线项目全景图</a>中搜索整个已核验生态。</sub></p>

## 去掉噪声之后的 JEV 生态

GitHub 上已有 **{len(discovered):,} 个仓库带有 `jev` topic**。但标签无法说明项目是在真实调用 JEV、计划未来接入、模仿接口，还是仅仅误贴了标签。

**JEV Project Atlas 把它们分清楚。** 所有候选都会被保留，但只有在公开源码中找到真实集成或决策点，项目才会进入主目录。

<table>
<tr>
<td align=\"center\" width=\"33%\"><h2>{len(projects)}</h2><b>已核验项目</b><br><sub>每项都链接到不可变源码</sub></td>
<td align=\"center\" width=\"33%\"><h2>{len(stats['categories'])}</h2><b>应用领域</b><br><sub>从 Agent 到数据库</sub></td>
<td align=\"center\" width=\"33%\"><h2>{len(discovered):,}</h2><b>持续监测仓库</b><br><sub>完整发现层始终保留</sub></td>
</tr>
</table>

## 从这里开始探索

<table>
<tr>
<td width=\"33%\" valign=\"top\"><h3>🧩 用 JEV 构建</h3>{item('vercel/ai')}<br><br>{item('langchain-ai/langchain')}<br><br>{item('pydantic/pydantic-ai')}</td>
<td width=\"33%\" valign=\"top\"><h3>⚡ 看 JEV 做决策</h3>{item('browser-use/jev-ultrafast')}<br><br>{item('trycua/cua')}<br><br>{item('realZachi/pg-jev')}</td>
<td width=\"33%\" valign=\"top\"><h3>🧪 本地运行兼容形态</h3>{item('jaredpalmer/kev')}<br><br>{item('featherless-ai/simple-jev')}</td>
</tr>
</table>

**[查看全部 {len(projects)} 个已核验项目 →](CATALOG.zh-CN.md)**

## 为什么可以相信这份目录？

1. **广泛发现。** 同步程序扫描完整的公开 `jev` topic，并拆分查询以绕过 GitHub 单次 1,000 条上限。
2. **严格核验。** 只有当审查者能指向固定版本源码中的 JEV 调用、适配或兼容实现时，项目才进入主目录。
3. **说人话。** 每个条目都说明项目做什么、JEV 在哪里决策、哪段源码能够证明。

> [!NOTE]
> “已核验”表示检查过公开源码，不代表通过安全审计、复现性能或获得生产背书。JEV 本体是托管模型；开源 SDK 和兼容项目并不是开放的 JEV 权重。

## 使用数据

发现层和核验层都以干净的 JSON 提交。例如，列出使用 Python 的已核验项目：

```bash
curl -sL https://raw.githubusercontent.com/PeriodBLUE/jev-project-atlas/main/data/verified-projects.json \\
  | jq -r '.projects[] | select(.language == "Python") | .repo'
```

- [`verified-projects.json`](data/verified-projects.json) — 已核验条目、简介、分类、元数据与固定源码证据。
- [`discovered-repos.json`](data/discovered-repos.json) — 完整发现快照，包括尚未核验的候选项目。

## 保持更新

```bash
python scripts/sync.py
```

无需安装任何依赖。标准库脚本会刷新发现层，并重建中英文 README、目录、数据集和在线搜索页。GitHub Actions 每周自动执行。

---

<p align=\"center\"><b>发现了遗漏？</b> <a href=\"CONTRIBUTING.zh-CN.md\">提交项目</a> · <a href=\"METHODOLOGY.zh-CN.md\">阅读方法</a> · <a href=\"THIRD_PARTY_NOTICES.md\">数据来源</a> · <a href=\"LICENSE\">MIT License</a></p>
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
