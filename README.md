<div align="center">

<img src="assets/banner.svg" alt="JEV Project Atlas" width="100%" />

# JEV Project Atlas · JEV 项目全景图

**发现、核验并总结 GitHub 上的 JEV / TypeSafe System One 项目。**

[![Verified](https://img.shields.io/badge/source--verified-479-2dd4bf?style=flat-square)](CATALOG.md)
[![Discovered](https://img.shields.io/badge/topic--discovered-1161-60a5fa?style=flat-square)](data/discovered-repos.json)
[![Updated](https://img.shields.io/badge/updated-2026--09--22-a78bfa?style=flat-square)](METHODOLOGY.md)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?style=flat-square)](LICENSE)

[完整目录](CATALOG.md) · [可搜索页面](docs/index.html) · [方法与边界](METHODOLOGY.md) · [贡献项目](CONTRIBUTING.md)

</div>

## 一眼看懂

JEV 是 TypeSafe AI 面向分类、路由、评分、排序、验证与安全门控等任务的快速、类型化决策模型。本仓库不是简单复制 GitHub 搜索结果，而是把生态分成两个互不混淆的层级：

| 层级 | 数量 | 含义 |
|---|---:|---|
| ✅ 源码已核验 | **479** | 有固定提交的源码证据，能定位 JEV 在哪里做决策 |
| 🔭 Topic 已发现 | **1161** | GitHub `jev` topic 的完整快照，包含待核验项目与噪声 |
| 🔗 Topic 中已核验 | **161** | 同时出现在发现层和核验层的项目 |

> [!IMPORTANT]
> “已核验”表示查看过公开源码证据，不代表项目已做安全审计、性能复现或生产可用性背书。JEV 本体是托管模型；开源 SDK、集成和兼容实现不等于开放模型权重。

## 值得先看的项目

| 项目 | 做什么 | ⭐ | 许可证 |
|---|---|---:|---|
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 给 Python LangChain 流程加一个可选 Jev 分类节点，返回类别、概率和等级评分。 | 146831 | MIT |
| [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | 一个教育用途的 AI 对冲基金原型，其中可选 Jev 适配器把结构化判断接到基金决策流程。 | 63657 | MIT |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | LiteLLM 的复杂度路由器可选用 Jev 判断请求应交给哪个模型档位。 | 59361 | Unknown |
| [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | Oh My Pi 编程 Agent 内含可选的 TypeSafe 判断提供器，供小型决策流程调用。 | 32380 | MIT |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | claude-code-templates 社区仓库中的 Jev 路由模组，为 Claude Code 子 Agent 建议模型与思考档位。 | 30897 | MIT |
| [ComposioHQ/composio](https://github.com/ComposioHQ/composio) | Composio 的可选 TypeSafe provider，用 Jev 从工具与有限参数选项中做判断。 | 30279 | MIT |
| [vercel/ai](https://github.com/vercel/ai) | AI SDK 中的 TypeSafe provider，让 TypeScript 应用通过统一 evaluate 接口调用 Jev。 | 26887 | Unknown |
| [trycua/cua](https://github.com/trycua/cua) | Cua 仓库的 jev-use 预览示例：Driver 观察与执行，Jev 从有界候选中选择浏览器动作。 | 25783 | MIT |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | Pydantic AI 的可选 Jev 模型：把输出模型里的布尔和枚举字段变成问题，拿回符合类型的判断。 | 20109 | MIT |
| [elizaOS/eliza](https://github.com/elizaOS/eliza) | Eliza 源码中的可选 TypeSafe HTTP 适配器，默认没有注册到 Agent 运行时。 | 19406 | MIT |

## 生态分布

| 分类 | 项目数 |
|---|---:|
| SDK & Decision Frameworks | 90 |
| Security & Guardrails | 41 |
| High-Frequency & Simulation | 40 |
| Routing & Cost Optimization | 38 |
| Browser & OS Action | 38 |
| Domain & Vertical Tools | 34 |
| MCP & Integrations | 30 |
| Context GC & Filter | 29 |
| Evaluation & Observability | 29 |
| CLI & Pipelines | 29 |
| Data & Search | 28 |
| Creative Tools | 16 |
| Codebase & Graph Pathfinding | 13 |
| Decision Tools | 12 |
| SDK & Integrations | 6 |
| Voice & Conversation | 4 |
| Classification & Taxonomy | 2 |

主要语言：Unknown 220 · TypeScript 99 · Python 70 · JavaScript 33 · Rust 14 · Go 11 · Ruby 5 · Swift 3

## 如何使用

- 想找可直接用的项目：打开 [完整目录](CATALOG.md)，按领域浏览。
- 想搜索、筛选、排序：打开 [可搜索页面](docs/index.html)。
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
