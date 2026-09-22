<div align="center">

<a href="https://periodblue.github.io/jev-project-atlas/"><img src="assets/banner.svg" alt="JEV Project Atlas" width="100%" /></a>

### 看清哪些 JEV 项目是真的。

**479 个项目附有固定源码证据，可按用途、语言、许可证以及 JEV 的准确决策点搜索。**

[![verified](https://img.shields.io/badge/源码已核验-479-14b8a6?style=flat-square)](CATALOG.zh-CN.md)
[![discovered](https://img.shields.io/badge/Topic已发现-1169-3b82f6?style=flat-square)](data/discovered-repos.json)
[![updated](https://img.shields.io/badge/更新-2026--09--22-8b5cf6?style=flat-square)](METHODOLOGY.zh-CN.md)
[![license](https://img.shields.io/badge/许可证-MIT-f59e0b?style=flat-square)](LICENSE)

**[打开在线全景图 →](https://periodblue.github.io/jev-project-atlas/?lang=zh)** &nbsp;·&nbsp; [浏览完整目录](CATALOG.zh-CN.md) &nbsp;·&nbsp; [使用数据](#使用数据)

[English](README.md) · **简体中文**

</div>

<br>

<a href="https://periodblue.github.io/jev-project-atlas/?lang=zh"><img src="assets/atlas-preview.png" alt="JEV Project Atlas 在线项目全景图" width="100%" /></a>

<p align="center"><sub>在<a href="https://periodblue.github.io/jev-project-atlas/?lang=zh">在线项目全景图</a>中搜索整个已核验生态。</sub></p>

## 去掉噪声之后的 JEV 生态

GitHub 上已有 **1,169 个仓库带有 `jev` topic**。但标签无法说明项目是在真实调用 JEV、计划未来接入、模仿接口，还是仅仅误贴了标签。

**JEV Project Atlas 把它们分清楚。** 所有候选都会被保留，但只有在公开源码中找到真实集成或决策点，项目才会进入主目录。

<table>
<tr>
<td align="center" width="33%"><h2>479</h2><b>已核验项目</b><br><sub>每项都链接到不可变源码</sub></td>
<td align="center" width="33%"><h2>17</h2><b>应用领域</b><br><sub>从 Agent 到数据库</sub></td>
<td align="center" width="33%"><h2>1,169</h2><b>持续监测仓库</b><br><sub>完整发现层始终保留</sub></td>
</tr>
</table>

## 从这里开始探索

<table>
<tr>
<td width="33%" valign="top"><h3>🧩 用 JEV 构建</h3><a href="https://github.com/vercel/ai"><strong>vercel/ai</strong></a><br><sub>AI SDK 中的 TypeSafe provider，让 TypeScript 应用通过统一 evaluate 接口调用 Jev。</sub><br><br><a href="https://github.com/langchain-ai/langchain"><strong>langchain-ai/langchain</strong></a><br><sub>给 Python LangChain 流程加一个可选 Jev 分类节点，返回类别、概率和等级评分。</sub><br><br><a href="https://github.com/pydantic/pydantic-ai"><strong>pydantic/pydantic-ai</strong></a><br><sub>Pydantic AI 的可选 Jev 模型：把输出模型里的布尔和枚举字段变成问题，拿回符合类型的判断。</sub></td>
<td width="33%" valign="top"><h3>⚡ 看 JEV 做决策</h3><a href="https://github.com/browser-use/jev-ultrafast"><strong>browser-use/jev-ultrafast</strong></a><br><sub>给浏览器一个目标，让 Jev 选择操作和页面控件，需要输入文字时再调用文本模型。</sub><br><br><a href="https://github.com/trycua/cua"><strong>trycua/cua</strong></a><br><sub>Cua 仓库的 jev-use 预览示例：Driver 观察与执行，Jev 从有界候选中选择浏览器动作。</sub><br><br><a href="https://github.com/realZachi/pg-jev"><strong>realZachi/pg-jev</strong></a><br><sub>在 PostgreSQL 查询中用自然语言给数据行筛选、分类和排序。</sub></td>
<td width="33%" valign="top"><h3>🧪 本地运行兼容形态</h3><a href="https://github.com/jaredpalmer/kev"><strong>jaredpalmer/kev</strong></a><br><sub>基于 Qwen2.5-0.5B 构建的轻量级类 Jev 决策头与适配器，支持在 MacBook 本地训练、微调与端到端运行。</sub><br><br><a href="https://github.com/featherless-ai/simple-jev"><strong>featherless-ai/simple-jev</strong></a><br><sub>将任意开源大语言模型转化为分类器与 Jev 兼容端点的适配服务，无需额外训练专用分类头。</sub></td>
</tr>
</table>

**[查看全部 479 个已核验项目 →](CATALOG.zh-CN.md)**

## 为什么可以相信这份目录？

1. **广泛发现。** 同步程序扫描完整的公开 `jev` topic，并拆分查询以绕过 GitHub 单次 1,000 条上限。
2. **严格核验。** 只有当审查者能指向固定版本源码中的 JEV 调用、适配或兼容实现时，项目才进入主目录。
3. **说人话。** 每个条目都说明项目做什么、JEV 在哪里决策、哪段源码能够证明。

> [!NOTE]
> “已核验”表示检查过公开源码，不代表通过安全审计、复现性能或获得生产背书。JEV 本体是托管模型；开源 SDK 和兼容项目并不是开放的 JEV 权重。

## 使用数据

发现层和核验层都以干净的 JSON 提交。例如，列出使用 Python 的已核验项目：

```bash
curl -sL https://raw.githubusercontent.com/PeriodBLUE/jev-project-atlas/main/data/verified-projects.json \
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

<p align="center"><b>发现了遗漏？</b> <a href="CONTRIBUTING.zh-CN.md">提交项目</a> · <a href="METHODOLOGY.zh-CN.md">阅读方法</a> · <a href="THIRD_PARTY_NOTICES.md">数据来源</a> · <a href="LICENSE">MIT License</a></p>
