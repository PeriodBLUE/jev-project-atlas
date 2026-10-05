# JEV 已核验项目目录

[English](CATALOG.md) · **简体中文**

> 数据快照：2026-10-05 · 共 **854** 个项目 · 按源码证据核验，不等同于运行时安全审计。

[返回首页](README.zh-CN.md) · [方法说明](METHODOLOGY.zh-CN.md) · [机器可读数据](data/verified-projects.json)

## 分类导航

- [Browser & OS Action (54)](#browser-os-action)
- [CLI & Pipelines (102)](#cli-pipelines)
- [Classification & Taxonomy (2)](#classification-taxonomy)
- [Codebase & Graph Pathfinding (16)](#codebase-graph-pathfinding)
- [Context GC & Filter (42)](#context-gc-filter)
- [Creative Tools (28)](#creative-tools)
- [Data & Search (51)](#data-search)
- [Decision Tools (42)](#decision-tools)
- [Domain & Vertical Tools (97)](#domain-vertical-tools)
- [Evaluation & Observability (29)](#evaluation-observability)
- [High-Frequency & Simulation (56)](#high-frequency-simulation)
- [MCP & Integrations (56)](#mcp-integrations)
- [Routing & Cost Optimization (69)](#routing-cost-optimization)
- [SDK & Decision Frameworks (133)](#sdk-decision-frameworks)
- [SDK & Integrations (6)](#sdk-integrations)
- [Security & Guardrails (67)](#security-guardrails)
- [Voice & Conversation (4)](#voice-conversation)

## Browser & OS Action

| 项目 | 简介 | 语言 | ⭐ | 许可证 | 证据 |
|---|---|---:|---:|---:|---|
| [**trycua/cua**](https://github.com/trycua/cua) | Cua 仓库的 jev-use 预览示例：Driver 观察与执行，Jev 从有界候选中选择浏览器动作。 | Rust | 27808 | MIT | [固定提交](https://github.com/trycua/cua/blob/83f142c4290a0f7d9ed545ae8532858c6e4f8145/libs/cua-driver/examples/jev-use/python/jev_adapter.py#L11) |
| [**browser-use/jev-ultrafast**](https://github.com/browser-use/jev-ultrafast) | 给浏览器一个目标，让 Jev 选择操作和页面控件，需要输入文字时再调用文本模型。 | Python | 21806 | MIT | [固定提交](https://github.com/browser-use/jev-ultrafast/blob/1231850a0bf1a0c0341fe408ef1668dbbfdfac46/jev_ultrafast/model.py) |
| [**lahfir/agent-desktop**](https://github.com/lahfir/agent-desktop) | 把电脑里的按钮和菜单交给 Jev 来选。它读原生无障碍结构，一步步完成桌面操作。 | Rust | 1743 | Apache-2.0 | [固定提交](https://github.com/lahfir/agent-desktop/blob/7a8e4a10281c7319733aa200fd79501f34529716/scripts/jev/act.mjs) |
| [**awlevin/typesafe-computer-use**](https://github.com/awlevin/typesafe-computer-use) | 用 OCR 和界面状态构造候选动作，让 Jev 决定如何操作 macOS，需要写文字时再调用文本模型。 | Python | 1144 | MIT | [固定提交](https://github.com/awlevin/typesafe-computer-use/blob/cc7b5066ae1a07b5e3182e8f87a9b5b6dfdcffc1/typesafe_computer_use/decide.py) |
| [**wy-coliney/jev-browser-use**](https://github.com/wy-coliney/jev-browser-use) | 给 Codex 浏览器工作流加一个 Skill：Jev 选导航、点击和滚动，Codex 保留文字输入与最终核验。 | JavaScript | 800 | MIT | [固定提交](https://github.com/wy-coliney/jev-browser-use/blob/f14b60e0ae1ee90cd73eb6650e30a666a84c021a/skills/jev-browser-use/bridge.mjs) |
| [**Sac-Y/Jev-cu**](https://github.com/Sac-Y/Jev-cu) | Codex Computer Use 辅助循环：界面文字候选交给 Jev，读取与执行交给桌面工具。 | JavaScript | 614 | MIT | [固定提交](https://github.com/Sac-Y/Jev-cu/blob/38fb31de7dfe6209bbe6e04057c00c6e885ba577/scripts/jev-decide.mjs#L6) |
| [**BennyKok/omg.dev**](https://github.com/BennyKok/omg.dev) | omg.dev 的移动端测试脚本可让 Jev 读取可访问性树并选择下一步交互。 | TypeScript | 545 | MIT | [固定提交](https://github.com/BennyKok/omg.dev/blob/a00f56684a569ee417be787c148eaa9874946f2b/mobile/scripts/jev.ts) |
| [**droidrun/mobile-jev**](https://github.com/droidrun/mobile-jev) | 通过 Mobilerun 控制 Android 手机，网页面板与命令行可查看 Jev 的操作过程。 | — | 431 | MIT | [固定提交](https://github.com/droidrun/mobile-jev/blob/395fc222beac4f059f9a0beb337d114a2b066e99/scripts/mobile-agent/policy.mjs#L224) |
| [**moritzkremb/jev-voice-browser**](https://github.com/moritzkremb/jev-voice-browser) | 用语音控制 Playwright 浏览器，将逐步转写的口令交给 Jev 判断。 | — | 378 | MIT | [固定提交](https://github.com/moritzkremb/jev-voice-browser/blob/054db0f3dbf537af63a8117632d3f941ccd520e1/src/jev.js#L123) |
| [**jkudish/jev-browser**](https://github.com/jkudish/jev-browser) | 给定任务与网址后驱动浏览器，返回最终页面、截图和逐步操作记录。 | — | 303 | MIT | [固定提交](https://github.com/jkudish/jev-browser/blob/8d90c51bedbe7cd07596bfaa532ded019a31d2a8/src/navigate.ts#L1) |
| [**savka777/jev-use**](https://github.com/savka777/jev-use) | 这是在 macOS 上用语音或文字下指令、由 Jev 读取 Accessibility 树并操作屏幕元素的电脑使用工具。 | — | 114 | MIT | 已核验 |
| [**kevinbadi/jev-voice**](https://github.com/kevinbadi/jev-voice) | 通过本地语音识别加一次 Jev 选择调用来打开应用、输入、搜索和操控 macOS 的语音助手。 | — | 107 | MIT | 已核验 |
| [**Ying-Kai-Liao/jev-browser**](https://github.com/Ying-Kai-Liao/jev-browser) | 浏览器自动化库、CLI 和 MCP：调用方模型给出目标与待输入文字，Jev 选择具体操作。 | JavaScript | 94 | MIT | [固定提交](https://github.com/Ying-Kai-Liao/jev-browser/blob/578cff6e701a131733d03256078bb559a45ad188/src/jev.mjs#L8) |
| [**realZachi/typesafe-adblock**](https://github.com/realZachi/typesafe-adblock) | 一个实验性 Chrome 扩展，让 Jev 判断候选 DOM 元素是否是广告，再高亮或移除。 | JavaScript | 88 | MIT | [固定提交](https://github.com/realZachi/typesafe-adblock/blob/7e067d243d87b7fe4d511653c0ddcd77b9beee18/src/typesafe.js) |
| [**chy4pro/JevBrowserExt**](https://github.com/chy4pro/JevBrowserExt) | 把 jev-ultrafast 做成 Manifest V3 Chrome 扩展：Jev 在当前标签里选操作和 DOM 元素，只有输入文字时才调用小型对话模型。 | — | 36 | MIT | 已核验 |
| [**jcpsimmons/jev-macos-loop**](https://github.com/jcpsimmons/jev-macos-loop) | 在 Mac 本地识别屏幕文字和控件，把文字选项交给 Jev，再点击它选中的元素。 | JavaScript | 23 | AGPL-3.0 | [固定提交](https://github.com/jcpsimmons/jev-macos-loop/blob/1aadc01ef262c3b01460909c5dd102f0d9616ba5/src/providers.mjs) |
| [**imohitmayank/jevfill**](https://github.com/imohitmayank/jevfill) | Jevfill 是一个 Chrome 扩展，可调用 Jev 根据用户粘贴的纯文本笔记自动填写网页表单。 | — | 20 | MIT | 已核验 |
| [**romaluev/jev-ego**](https://github.com/romaluev/jev-ego) | 面向 ego lite 的浏览器 Agent，把页面可操作元素编号后交给 Jev 选择下一步。 | TypeScript | 16 | Unknown | [固定提交](https://github.com/romaluev/jev-ego/blob/12eaafe795db56da821d9268ee7b9ae9ea24b23b/src/model.ts) |
| [**forvela/jev-agent-browser**](https://github.com/forvela/jev-agent-browser) | 该项目让 Jev 选择类型化浏览器操作并由 agent-browser 执行，以完成有界的浏览、研究和分类任务。 | — | 13 | MIT | 已核验 |
| [**ZJU-REAL/CUA-JEV**](https://github.com/ZJU-REAL/CUA-JEV) | CUA-JEV是一个开源参考框架，任务适配器把浏览器、桌面UI、办公应用、终端或文件系统的结构化状态转为合法、可执行、可验证的候选动作，由Jev选择具体动作及其执行通道，再由框架守卫执行、验证结果状态并继续观察，首版包含四个经Windows验证的工作流示例。 | — | 11 | Unknown | 已核验 |
| [**tontoko/jev-browser**](https://github.com/tontoko/jev-browser) | 基于 Playwright 的 Jev 浏览器自动化工具，共用 CLI、MCP 与 TypeScript SDK。 | JavaScript | 10 | Apache-2.0 | [固定提交](https://github.com/tontoko/jev-browser/blob/05b8257db8d7df77a82274016de84d965a38214f/src/decision.ts) |
| [**Friedjof/jev-mobile**](https://github.com/Friedjof/jev-mobile) | jev-mobile 是一个自主的 Android 子 Agent，以 TypeSafe Jev 为决策器，对 USB 连接的设备执行观察、归一化、决策、变更和验证的持久任务循环。 | — | 8 | MIT | 已核验 |
| [**himomohi/aside-jev**](https://github.com/himomohi/aside-jev) | 给 Aside 浏览器 Agent 提供 Jev 判断的 MCP 服务器与 skill。 | Python | 8 | MIT | [固定提交](https://github.com/himomohi/aside-jev/blob/d2923f7949a9576e82b51d2c5e5514c17d80d60b/src/aside_jev/jev.py) |
| [**ranjan2829/AskJev**](https://github.com/ranjan2829/AskJev) | 通过 MCP 把 Agent 接到浏览器，由 Jev 选择网页动作，并对付款、删除等操作设置确认环节。 | TypeScript | 8 | MIT | [固定提交](https://github.com/ranjan2829/AskJev/blob/7beec5eba7c4a294d21013c158cd884e1c24f08b/mcp/src/jev-client.ts) |
| [**jaibhasin/jev-yt-time-saver**](https://github.com/jaibhasin/jev-yt-time-saver) | jev-yt-time-saver：Jev 根据视频标题、频道、时长、描述和搜索意图判断每个 YouTube 视频是否浪费时间并给出浪费分数。 | — | 7 | Unknown | 已核验 |
| [**stas4000/jev-clerk**](https://github.com/stas4000/jev-clerk) | 在 macOS 桌面上把供应商发票录入会计软件：Jev 每步从封闭动作表里选点击对象，深度模型只改剧本。 | Python | 7 | Unknown | [固定提交](https://github.com/stas4000/jev-clerk/blob/b471384e56bd9cec8f56ba8415f69b1006ce43e9/jev_clerk/jev.py) |
| [**arthurfiorette/jev-playwright**](https://github.com/arthurfiorette/jev-playwright) | 在 CI 中根据代码改动智能缩减 Playwright 测试集：让 Jev 评估 diff 并挑选出相关的测试用例，跳过不必要的全量测试。 | — | 6 | MIT | 已核验 |
| [**paulsmith/computer-use-jev**](https://github.com/paulsmith/computer-use-jev) | 用 Go 控制 macOS 应用，让 Jev 从可访问性树里选择控件和操作。 | Go | 6 | MIT | [固定提交](https://github.com/paulsmith/computer-use-jev/blob/ff0ad8ba8e25755d37fb8d93718144c4568a596b/typesafe/client.go) |
| [**jiangkoumo/ego-jev**](https://github.com/jiangkoumo/ego-jev) | **用 Jev（TypeSafe System One）驱动 ego lite 浏览器，把「下一步点哪里」的决策放进单个进程内闭环。** | — | 5 | MIT | 已核验 |
| [**Mrlyk/jev-browser**](https://github.com/Mrlyk/jev-browser) | 在交互终端中用自然语言操作浏览器，也可通过结构化 CLI 命令供 AI Agent 调用。 | — | 5 | Apache-2.0 | 已核验 |
| [**brnyxx/jev-ra**](https://github.com/brnyxx/jev-ra) | **面向 CLI 编码智能体的高速浏览器操作层。** Claude Code、Codex 或任何 MCP 客户端把目标交给 jev-ra。System One 决策模型 TypeSafe Jev 在一次往返中同时选出每一步的操作和目标元素。制定计划、 提供要输入的文本、读取页面内容、在 jev-ra 上交时接手，这些都由调用方的智能体完成。循环内不会再… | — | 4 | MIT | 已核验 |
| [**vmendes90/jev-shield**](https://github.com/vmendes90/jev-shield) | 一个 Chrome 广告过滤扩展，用 Jev 判断信息流元素是否带有推广意图。 | TypeScript | 4 | MIT | [固定提交](https://github.com/vmendes90/jev-shield/blob/85cf3445931cbed7320f140db9af5d1fd13c4c64/src/background/typesafe.ts) |
| [**xinwang-nwpu/jev-mobile**](https://github.com/xinwang-nwpu/jev-mobile) | **Android 手机自动化 agent：一次 Jev 模型请求同时决策"做什么操作"和"操作哪个元素"，无截图、纯 A11Y 无障碍树结构化状态，ADB 直接执行。** | — | 4 | MIT | 已核验 |
| [**AMMIROSOH/jev-2048-selenium**](https://github.com/AMMIROSOH/jev-2048-selenium) | 该项目用 Selenium 自动游玩 2048，结合 expectimax 搜索与 TypeSafe Jev 的 Choice 决策来选择每一步合法走法，并支持 FFmpeg 竖屏录制。 | — | 3 | Unknown | 已核验 |
| [**garry-schuette/browser-use-with-jev**](https://github.com/garry-schuette/browser-use-with-jev) | 这是一个 Python 集成，保留 Browser Use 的执行引擎，由 Jev 选择具体浏览器操作，宿主模型负责生成与验证。 | — | 3 | MIT | 已核验 |
| [**jonymusky/jev-browser-qa**](https://github.com/jonymusky/jev-browser-qa) | 该项目用 Playwright 执行并录制浏览器流程，用 Jev 判断自然语言断言、按意图选择控件和执行目标导向点击循环，并提供 JSON-flow CLI、运行看板和 Agent skill。 | — | 3 | MIT | 已核验 |
| [**rorshopping/jev-browser-local**](https://github.com/rorshopping/jev-browser-local) | 该项目把 jev-browser 接到本地 Jev 风格决策引擎与桥接服务，在本机完成浏览器操作决策和输入文本生成，无需调用云端模型。 | — | 3 | Unknown | 已核验 |
| [**sedum-dev/sedum**](https://github.com/sedum-dev/sedum) | sedum：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 3 | MIT | 已核验 |
| [**aidil2105/jev-browser-pilot**](https://github.com/aidil2105/jev-browser-pilot) | 该项目提供有界决策层，由代码负责观察、执行与验证，Jev 模型每步只选择一个候选操作。 | — | 2 | MIT | 已核验 |
| [**ChenYCL/jev-browser-skill**](https://github.com/ChenYCL/jev-browser-skill) | 在 **ego lite** 里的真实运行，由工具自己录制（`run --step-screenshots`）。左边是每一步之前 Jev 看到的页面，右边是 Jev 对这一步的校准判断以及代码控制器执行的动作。每个演示都只是一条 `jev-browser run` 命令。 | — | 2 | MIT | 已核验 |
| [**dingw530/playwright-jev**](https://github.com/dingw530/playwright-jev) | 基于 Jev + playwright-cli 的自然语言 Web E2E 测试工具：Jev 负责决策，Playwright 负责执行，代码负责断言与安全边界。Goal-driven web E2E testing with Jev + playwright-cli: bounded AI decisions, real browser executi… | — | 2 | MIT | 已核验 |
| [**Just-Betr/jevtest**](https://github.com/Just-Betr/jevtest) | jevtest：根据界面状态选择下一步动作或目标；本地执行器负责操作。 | — | 2 | MIT | 已核验 |
| [**Teylersf/WindowsJev**](https://github.com/Teylersf/WindowsJev) | WindowsJev：Jev 在每一步从确定性生成的有限候选 UI 动作中选择唯一最能安全推进目标的下一步动作，并判断当前界面是否已证明目标完成。 | — | 2 | MIT | 已核验 |
| [**ZHUBoer/ego-jev**](https://github.com/ZHUBoer/ego-jev) | 该项目让 Agent 用 Ego Lite 操作浏览器，并调用 Jev 完成语义目标选择、过滤、排序、分类和文本证据判断。 | — | 2 | MIT | 已核验 |
| [**zurfyx/jev-browser-skill**](https://github.com/zurfyx/jev-browser-skill) | 这是一个让 Jev 驱动浏览器执行点击、输入和选择操作以完成指定目标的 Agent 技能，适用于 Claude Code 和 Codex。 | — | 2 | MIT | 已核验 |
| [**DDnim/jev-tweet-radar**](https://github.com/DDnim/jev-tweet-radar) | Chrome 扩展对 X 时间线里每条帖子发一次 Jev Noul 请求，显示互动价值和可选标签概率。 | JavaScript | 1 | MIT | [固定提交](https://github.com/DDnim/jev-tweet-radar/blob/b5057858ab5de6f7d665527a192f009eff8d0e76/background.js) |
| [**ElshinQ/jevaluate**](https://github.com/ElshinQ/jevaluate) | 这是一个用 Jev 驱动浏览器操作网页并在不确定时停下来交给人工的开源工具，还包含 DeepSeek 截图检查、评估脚本和 Agent skill。 | — | 1 | MIT | 已核验 |
| [**flazouh/ego-jev**](https://github.com/flazouh/ego-jev) | 该工具列出 ego-browser 页面上的可用控件，由 Jev 每步选择一个动作并由代码执行后重新观察，遇到风险或不确定时停在当前页面交回 Agent。 | — | 1 | MIT | 已核验 |
| [**jaewgwon/jevis**](https://github.com/jaewgwon/jevis) | Flutter integration_test 包：注册允许的 UI 动作，Jev 根据当前界面选下一步并判断目标是否达成。 | Dart | 1 | Apache-2.0 | [固定提交](https://github.com/jaewgwon/jevis/blob/ab5630590288706ce56bb5665680358fe0bd95e8/lib/src/jevis_policy.dart) |
| [**laihenyi/pi-Jev-browser**](https://github.com/laihenyi/pi-Jev-browser) | 八個工具裡有七個驅動一個隔離的 Playwright Chromium。第八個 `jev_desktop` 透過 輔助使用樹（accessibility tree）驅動一個 macOS 應用程式，用的是同一個迴圈與 同一組守衛。迴圈不知道自己正在驅動哪一種表面：`src/loop.ts` 只依賴 `Driver` 介面，不 import Playwri… | — | 1 | Apache-2.0 | 已核验 |
| [**PenglongHuang/jev-demo**](https://github.com/PenglongHuang/jev-demo) | TypeSafe Jev（System One 决策模型）零依赖网页体验台：浏览器操作 / 意图识别 / Agent 上下文裁剪三大预设场景，发送状态与类型化问题，拿到带校准概率的结构化答案 | — | 1 | MIT | 已核验 |
| [**phd-peter/ego-jev**](https://github.com/phd-peter/ego-jev) | 把 Ego Lite 的浏览器快照与操作接到一个有步骤上限的 Jev 决策循环。 | — | 1 | MIT | [固定提交](https://github.com/phd-peter/ego-jev/blob/0da45e4f3a3bdad56402b5c38226ad3a2e10409c/src/jev-client.ts#L1) |
| [**abeatrix/cline-plugin-jev-browser**](https://github.com/abeatrix/cline-plugin-jev-browser) | Cline 的独立 Playwright 浏览器插件，通过 Vercel AI Gateway 用 Jev 选择网页操作。 | TypeScript | 0 | Unknown | [固定提交](https://github.com/abeatrix/cline-plugin-jev-browser/blob/c886dcb35cb7d64d682a56211f9b04a5345c6433/src/jev-model.ts) |
| [**grayrepo-byte/jev_filter_for_x**](https://github.com/grayrepo-byte/jev_filter_for_x) | JevFilterForX 是一个用于 X 的浏览器扩展。它会为信息流中的帖子评分，用轻量标签解释评分，并根据你的过滤设置折叠内容。未配置 API Key 时，默认使用本地模拟评分。 | TypeScript | 0 | Unknown | [固定提交](https://github.com/grayrepo-byte/jev_filter_for_x/blob/62cb4a602026b5449a9caa94c193c534e0a19c01/src/core/jev.ts#L35-L255) |

## CLI & Pipelines

| 项目 | 简介 | 语言 | ⭐ | 许可证 | 证据 |
|---|---|---:|---:|---:|---|
| [**Alex314618-create/JevRev**](https://github.com/Alex314618-create/JevRev) | JevRev 是放在 LLM 旁边的决策层，用 JevSift 筛选方案、用 JevLoop 按轮审核单个制品、用 JevLong 观察长会话的健康状况。 | — | 702 | MIT | 已核验 |
| [**thruwire/foreman**](https://github.com/thruwire/foreman) | 独立监督环读取编码工人的 diff、日志和测试，用 Jev Noul 判断卡住、跑偏、该验证，再由 Python 策略干预。 | Python | 657 | MIT | [固定提交](https://github.com/thruwire/foreman/blob/209182dac7a3467033fd093ab4ca47d21279984a/src/foreman/foreman/jev.py) |
| [**sutro-sh/jev-align**](https://github.com/sutro-sh/jev-align) | jev-align 是一个实验性 CLI，用 Jev 构建 AI Functions，通过挑选不确定样本请用户标注并用 GEPA 改进函数定义。 | — | 302 | Apache-2.0 | 已核验 |
| [**yonatangross/orchestkit**](https://github.com/yonatangross/orchestkit) | OrchestKit 可选用 Jev 给编程会话分类，符合阈值时用结果决定会话颜色。 | TypeScript | 286 | MIT | [固定提交](https://github.com/yonatangross/orchestkit/blob/569095f35ce61a4881197dfb8117f4c3312e2bee/src/hooks/src/lib/session-category-provider.ts) |
| [**keltokhy/jgrep**](https://github.com/keltokhy/jgrep) | jgrep 是用自然语言描述替代正则表达式来过滤文本行、结构化记录、函数和 diff 片段的命令行工具，每条记录交由 Jev 作 Noul 判断后输出符合项。 | — | 133 | MIT | 已核验 |
| [**christianmat/jev-pokemon**](https://github.com/christianmat/jev-pokemon) | jev-pokemon：对输入文本做分类或打分，交给本地规则继续处理。 | — | 118 | GPL-2.0 | 已核验 |
| [**mrnugget/jev-shell-history**](https://github.com/mrnugget/jev-shell-history) | 类似于 Fish 终端样式的 Zsh 历史命令建议工具，利用 Jev 对已有历史记录根据当前上下文进行智能打分排序。 | TypeScript | 117 | Unknown | [固定提交](https://github.com/mrnugget/jev-shell-history/blob/4b2b75d26c0ccf5726263904514a22a8e11659ea/src/suggest.ts#L1-L196) |
| [**mizchi/jev-lint**](https://github.com/mizchi/jev-lint) | 一个用 Jev 校准概率对代码匹配结果做语义 lint 检查的命令行工具。 | — | 114 | MIT | 已核验 |
| [**OmniJev/OneJev**](https://github.com/OmniJev/OneJev) | OneJev：对输入文本做分类或打分，交给本地规则继续处理。 | — | 110 | Apache-2.0 | 已核验 |
| [**sharziki/semdecide**](https://github.com/sharziki/semdecide) | 基于 Python 的语义判断 CLI，可给文本或 JSONL 管道做判断、分类、打分和过滤。 | Python | 75 | MIT | [固定提交](https://github.com/sharziki/semdecide/blob/33cf5c03c50e02e59df3f3ea81f0650f6b791545/src/reflex_guard/providers/typesafe.py) |
| [**EliaAlberti/jev-rules**](https://github.com/EliaAlberti/jev-rules) | jev-rules：对输入文本做分类或打分，交给本地规则继续处理。 | — | 64 | MIT | 已核验 |
| [**kyu1204/jgrep**](https://github.com/kyu1204/jgrep) | jgrep 是用英文描述代码行为来搜索代码、git diff 和表格行的命令行工具，它把代码块与每个块一个 Noul 问题一起发给 Jev，并输出命中的 file:line，同时支持用 Noul/Choice/Score 问题检查 diff 和为 CSV/JSONL 的每一行打分。 | — | 59 | MIT | 已核验 |
| [**henryklunaris/hey-jev**](https://github.com/henryklunaris/hey-jev) | hey-jev 在终端和自动化脚本中加入文本判断。 | — | 58 | Unknown | 已核验 |
| [**AkashPriyadarshii/jev-superpowers**](https://github.com/AkashPriyadarshii/jev-superpowers) | 面向编码智能体的系统化开发流程框架，融合 Jev 进行无幻觉依赖审查、完成度门禁与错误重试决策。 | JavaScript | 36 | MIT | [固定提交](https://github.com/AkashPriyadarshii/jev-superpowers/blob/6ddc702c231fd33fdf04b1ab1c0cce96fd8d2a19/skills/systematic-debugging/condition-based-waiting-example.ts#L1-L159) |
| [**mizchi/jev-test-filter**](https://github.com/mizchi/jev-test-filter) | 该工具读取 git diff，用 Jev 为每个测试评估受影响程度，并输出 vitest、jest、node:test、Playwright、cargo test 和 go test 可直接使用的过滤参数。 | — | 33 | MIT | 已核验 |
| [**win4r/jev-skill-suggester**](https://github.com/win4r/jev-skill-suggester) | 用 TypeSafe Jev 为当前任务推荐一个合适的已安装 Skill。先阅读技能描述筛选，再核对候选正文片段；允许返回“无需技能”或“不确定”。用户明确指定的技能通过本地查找优先处理。 | — | 32 | MIT | 已核验 |
| [**lukstei/slop-grader**](https://github.com/lukstei/slop-grader) | 这是一个基于规则的 CLI 工具，用 Jev 的 Score 做文档级打分、用 Choice 和 Noul 做逐行违规标记，并把结果交给 Agent 去修复文本和 Markdown 文件。 | — | 31 | MIT | 已核验 |
| [**smkrv/jev-calibrate**](https://github.com/smkrv/jev-calibrate) | 该工具使用标注示例调优 Jev 问题，并在留出验证集上为每个问题给出可用性结论。 | — | 31 | MIT | 已核验 |
| [**keltokhy/jsort**](https://github.com/keltokhy/jsort) | 按自然语言描述的维度对文本行/段落/文件进行两两比较排序并输出分数与标准误的命令行工具。 | — | 25 | MIT | 已核验 |
| [**shiftynick/jev-axi**](https://github.com/shiftynick/jev-axi) | 在命令行调用 Jev 做 pick、rate、check、rank、triage、guard，并可接到 Agent 工具调用前的 hook。 | TypeScript | 25 | MIT | [固定提交](https://github.com/shiftynick/jev-axi/blob/db4b6fe56f962463d3924019bd038462a2190b2d/src/client.ts) |
| [**wuxie888/jev-yaba-wechat**](https://github.com/wuxie888/jev-yaba-wechat) | 微信里的话不知道怎么接？macOS 悬浮聊天助手：识别消息意图与沟通风险，GPT 生成多种话术，Jev 评估候选，一键填入微信。话我帮你想，发送你来定。 | — | 24 | MIT | 已核验 |
| [**Nasrallah-AL/jev-cli**](https://github.com/Nasrallah-AL/jev-cli) | 名为 jevctl 的终端工具，把核验、分类与评分问题接到文本输入和脚本里。 | TypeScript | 22 | MIT | [固定提交](https://github.com/Nasrallah-AL/jev-cli/blob/02ca80177aaef0b30a897959207f99df1e0c8446/src/provider.ts) |
| [**jsk4581/jev-blindspot**](https://github.com/jsk4581/jev-blindspot) | 这是一个给 Claude Code 和 Codex CLI 用的侧边面板助手，先用 Jev 判断每次提交的提示词是否值得再看一遍，只有通过时才让 Agent 自身的只读无头模式读取项目并返回盲点，且不拦截提示词也不向会话添加内容。 | — | 20 | MIT | 已核验 |
| [**rhighs/jev-code**](https://github.com/rhighs/jev-code) | 一个实验性编程终端，让 Jev 逐步选择 AST 节点来组成 Python 或 Bash，也能作为命令行判断工具。 | TypeScript | 20 | Unknown | [固定提交](https://github.com/rhighs/jev-code/blob/51bf5c1242a51feba8c5a4e18b61e379a9e94e5e/src/provider.ts) |
| [**syumai/jevyoumean**](https://github.com/syumai/jevyoumean) | jevyoumean：对输入文本做分类或打分，交给本地规则继续处理。 | — | 16 | MIT | 已核验 |
| [**tumf/jev-cli**](https://github.com/tumf/jev-cli) | 为 Jev 提供 CLI 和 stdio MCP 入口，输入文本或 JSON，输出结构化判断。 | Python | 13 | MIT | [固定提交](https://github.com/tumf/jev-cli/blob/60441de4f96870686a5388bd6ed714f36eed646b/src/jev_cli/__init__.py) |
| [**exYze/rift**](https://github.com/exYze/rift) | Rust 编程终端 Rift 的可选 TypeSafe 决策客户端，给受限判断调用 Jev。 | Rust | 12 | MIT | [固定提交](https://github.com/exYze/rift/blob/b446c3fb8ecf0b0e445b16436fd937262956d010/crates/rift-typesafe/src/lib.rs) |
| [**kushals256/jevcache**](https://github.com/kushals256/jevcache) | jevcache：对输入文本做分类或打分，交给本地规则继续处理。 | — | 12 | MIT | 已核验 |
| [**da-vinci-noob/pi-jev-model-router**](https://github.com/da-vinci-noob/pi-jev-model-router) | pi-jev-model-router：对输入文本做分类或打分，交给本地规则继续处理。 | — | 11 | MIT | 已核验 |
| [**ethan-ab/xscout-jev**](https://github.com/ethan-ab/xscout-jev) | xscout-jev：对输入文本做分类或打分，交给本地规则继续处理。 | — | 11 | MIT | 已核验 |
| [**ZephyrDeng/ego-jev**](https://github.com/ZephyrDeng/ego-jev) | ego-jev：对输入文本做分类或打分，交给本地规则继续处理。 | — | 11 | MIT | 已核验 |
| [**danielnc/jev-browse**](https://github.com/danielnc/jev-browse) | jev-browse：对输入文本做分类或打分，交给本地规则继续处理。 | — | 8 | MIT | 已核验 |
| [**kyle-chalmers/typesafe-jev-incident-router**](https://github.com/kyle-chalmers/typesafe-jev-incident-router) | typesafe-jev-incident-router：对输入文本做分类或打分，交给本地规则继续处理。 | — | 8 | Unknown | 已核验 |
| [**kylemclaren/jevsearch**](https://github.com/kylemclaren/jevsearch) | 这是一个网站搜索命令面板，先显示关键词匹配结果，再用 Jev 模型按用户意图重新排序。 | — | 8 | MIT | 已核验 |
| [**jkudish/jev-agent-tools**](https://github.com/jkudish/jev-agent-tools) | jev-agent-tools：对输入文本做分类或打分，交给本地规则继续处理。 | — | 6 | MIT | 已核验 |
| [**sugarforever/tryjev**](https://github.com/sugarforever/tryjev) | tryjev：对输入文本做分类或打分，交给本地规则继续处理。 | — | 6 | MIT | 已核验 |
| [**sumleo/prompt2jev**](https://github.com/sumleo/prompt2jev) | prompt2jev：对输入文本做分类或打分，交给本地规则继续处理。 | — | 6 | MIT | 已核验 |
| [**Arpit-Khandelwal/jev-linkedin-slop-filter**](https://github.com/Arpit-Khandelwal/jev-linkedin-slop-filter) | jev-linkedin-slop-filter：对输入文本做分类或打分，交给本地规则继续处理。 | — | 5 | MIT | 已核验 |
| [**ishantanu/jevmetrics**](https://github.com/ishantanu/jevmetrics) | jevmetrics 是一个 OpenTelemetry Collector 指标处理器，它调用 Jev 模型根据指标元数据推断操作价值，并据此注释或过滤指标。 | — | 5 | Apache-2.0 | 已核验 |
| [**jacks3tr/Jev-Desktop**](https://github.com/jacks3tr/Jev-Desktop) | Jev-Desktop：对输入文本做分类或打分，交给本地规则继续处理。 | — | 5 | MIT | 已核验 |
| [**ShuhanSun/jev-oas-sentinel**](https://github.com/ShuhanSun/jev-oas-sentinel) | 该工具比较两个 OpenAPI 文档，用确定性检查发现结构兼容性问题，并用 TypeSafe Jev 评估变更描述中的语义风险。 | — | 5 | Apache-2.0 | 已核验 |
| [**ddfeyes/jev-mode**](https://github.com/ddfeyes/jev-mode) | jev-mode 是把 Agent 批量语义判断移出上下文、交由 Jev 做类型化裁决的 Python 工具。 | — | 4 | MIT | 已核验 |
| [**glud123/jev-assist**](https://github.com/glud123/jev-assist) | 别让贵的主模型干 grep 试错的粗活——交给 jev 排完整个仓库，主模型只负责读对的文件、写对的代码。 | — | 4 | MIT | 已核验 |
| [**kiler398/jev-demo**](https://github.com/kiler398/jev-demo) | 模拟对话，实时看 **Jev**（TypeSafe AI 的 System One 模型）怎么判、怎么路由、怎么拦。 | — | 4 | Unknown | 已核验 |
| [**markjaquith/typesafe-ai-playground**](https://github.com/markjaquith/typesafe-ai-playground) | Rust 命令行实验集，可筛查医疗隐私信息、检查代码注释、分析语气并分类行业和职业。 | Rust | 4 | MIT | [固定提交](https://github.com/markjaquith/typesafe-ai-playground/blob/344d77450e1cf3d7aebd2c9566b362b9c693b8e2/src/typesafe.rs#L57) |
| [**Ramneet-Singh/jevopt**](https://github.com/Ramneet-Singh/jevopt) | jevopt：对输入文本做分类或打分，交给本地规则继续处理。 | — | 4 | GPL-3.0 | 已核验 |
| [**SampleBias/Jev_Onco_Statistical_Hierarchy**](https://github.com/SampleBias/Jev_Onco_Statistical_Hierarchy) | Jev_Onco_Statistical_Hierarchy：对输入文本做分类或打分，交给本地规则继续处理。 | — | 4 | MIT | 已核验 |
| [**VBS2004/jevcut**](https://github.com/VBS2004/jevcut) | jevcut：对输入文本做分类或打分，交给本地规则继续处理。 | — | 4 | MIT | 已核验 |
| [**boldbug1/jev-triage**](https://github.com/boldbug1/jev-triage) | 这是一个用 Go 编写的命令行工具，用 Jev 对每条消息进行分类并评估紧急程度和挫败感，然后按紧急程度排序输出表格、低置信度人工复核列表和 HTML 报告。 | — | 3 | MIT | 已核验 |
| [**DoGMaTiiC/hermes-jev**](https://github.com/DoGMaTiiC/hermes-jev) | hermes-jev：对输入文本做分类或打分，交给本地规则继续处理。 | — | 3 | Unknown | 已核验 |
| [**f-lombardo/jev-php**](https://github.com/f-lombardo/jev-php) | jev-php：对输入文本做分类或打分，交给本地规则继续处理。 | — | 3 | LGPL-2.1 | 已核验 |
| [**gauravkhuraana/jev-qa-demos**](https://github.com/gauravkhuraana/jev-qa-demos) | jev-qa-demos：对输入文本做分类或打分，交给本地规则继续处理。 | — | 3 | Unknown | 已核验 |
| [**jkf87/jev-handson**](https://github.com/jkf87/jev-handson) | jev-handson：对输入文本做分类或打分，交给本地规则继续处理。 | — | 3 | Unknown | 已核验 |
| [**joshLong145/jev-cli**](https://github.com/joshLong145/jev-cli) | jev-cli 是用 Python 编写的命令行工具，用 Jev 分析 JSON、NDJSON、JSONC 和文本日志并返回带类型的判定答案。 | — | 3 | Unknown | 已核验 |
| [**jtsang4/jev-cli**](https://github.com/jtsang4/jev-cli) | 在终端里问 Jev 判断题。输入文本或 JSON，再给出分类、是非或评分问题，拿回脚本能直接读取的 JSON。 | TypeScript | 3 | MIT | [固定提交](https://github.com/jtsang4/jev-cli/blob/6ea8abdf702d2fc28bfffd979e83db8c32f3ceb5/src/providers/jev.ts) |
| [**lianghsun/jev-tmmluplus-eval**](https://github.com/lianghsun/jev-tmmluplus-eval) | 该项目通过 Jev 的四选一作答接口对 TMMLU+ v1.1 繁体中文基准进行评测与计分。 | — | 3 | MIT | 已核验 |
| [**lookski/openjev**](https://github.com/lookski/openjev) | Jev (TypeSafe AI, 2026 年 9 月) 让 "决策模型" 一词刷屏: 发送一段状态 (state) + 若干类型化问题, 返回**带校准概率的类型安全答案** —— 不生成文本, 没有幻觉, 70–500 ms 延迟. | — | 3 | MIT | 已核验 |
| [**LYchoon/paper-radar-jev**](https://github.com/LYchoon/paper-radar-jev) | 以上指令會保留已存在的本機設定。編輯專案根目錄的 `.env`，將空白值換成自己的 key： | — | 3 | MIT | 已核验 |
| [**NomenAK/jev-tools**](https://github.com/NomenAK/jev-tools) | jev-tools：对输入文本做分类或打分，交给本地规则继续处理。 | — | 3 | MIT | 已核验 |
| [**selmakcby/jev-kiyafet-bul**](https://github.com/selmakcby/jev-kiyafet-bul) | jev-kiyafet-bul：对输入文本做分类或打分，交给本地规则继续处理。 | — | 3 | Unknown | 已核验 |
| [**Selmar/typesafe-jev-calibrate-for-code-review**](https://github.com/Selmar/typesafe-jev-calibrate-for-code-review) | 该仓库记录了使用 Jev 进行代码评审的校准实验，并提供代码与注释规则集及评分脚本用于复现测量结果。 | — | 3 | Unknown | 已核验 |
| [**AABBAASS1/jev-router**](https://github.com/AABBAASS1/jev-router) | 该 CLI 向 Jev 查询任务应分配给哪个 Agent，然后打开 Claude、ChatGPT、Cursor 或 Antigravity 的应用或网页并填入提示词。 | — | 2 | Unknown | 已核验 |
| [**allebee/pytest-jev**](https://github.com/allebee/pytest-jev) | pytest-jev：对输入文本做分类或打分，交给本地规则继续处理。 | — | 2 | MIT | 已核验 |
| [**gualican/jev-model-router**](https://github.com/gualican/jev-model-router) | jev-model-router：对输入文本做分类或打分，交给本地规则继续处理。 | — | 2 | MIT | 已核验 |
| [**Larkspur-Wang/Jev_steer_or_queue**](https://github.com/Larkspur-Wang/Jev_steer_or_queue) | 编码 agent 对任务运行中收到的消息一视同仁。Claude Code 会立刻把它注入当前 turn。“改用简单点的方案”这样很合适；“做完之后顺便更新 changelog”会被混进当前任务；“停一下，别继续了”要靠模型自己愿意停。 | — | 2 | MIT | 已核验 |
| [**sathariels/jevcheck**](https://github.com/sathariels/jevcheck) | jevcheck：对输入文本做分类或打分，交给本地规则继续处理。 | — | 2 | MIT | 已核验 |
| [**Shakibuzzaman3104/claude-jev-funnel**](https://github.com/Shakibuzzaman3104/claude-jev-funnel) | claude-jev-funnel：对输入文本做分类或打分，交给本地规则继续处理。 | — | 2 | Apache-2.0 | 已核验 |
| [**taichocop/jevault**](https://github.com/taichocop/jevault) | jevault：对输入文本做分类或打分，交给本地规则继续处理。 | — | 2 | MIT | 已核验 |
| [**wanghai673/jev-browser-skill**](https://github.com/wanghai673/jev-browser-skill) | ⚡ 快速浏览器 Skill：Jev 驱动，Codex 即用。连续执行、预置输入，一句话启动浏览器任务。 | — | 2 | MIT | 已核验 |
| [**wellkilo/codex-jev-preflight**](https://github.com/wellkilo/codex-jev-preflight) | 在 Codex 开始执行前，通过 TypeSafe Jev 获取 `task_type`、`complexity`、`risk` 和 `execution_mode`。判定仅作为建议上下文，并且始终 fail-open，不会阻塞任务。 | — | 2 | MIT | 已核验 |
| [**xianggelila177/VideoAdGuard-Jev**](https://github.com/xianggelila177/VideoAdGuard-Jev) | VideoAdGuard-Jev：对输入文本做分类或打分，交给本地规则继续处理。 | — | 2 | GPL-2.0 | 已核验 |
| [**adamwdff/jev-gate**](https://github.com/adamwdff/jev-gate) | 在 **WorkBuddy / Hermes Agent** 里，**模型读你的提示词之前**，先让 Jev（TypeSafe System One 判定模型）花 ~1 秒对这次请求做一次结构化判定，把结论注入给主模型当路由提示。 | — | 1 | MIT | 已核验 |
| [**allebee/jevgrep**](https://github.com/allebee/jevgrep) | jevgrep：对输入文本做分类或打分，交给本地规则继续处理。 | — | 1 | MIT | 已核验 |
| [**amberwhitehead/jevscript**](https://github.com/amberwhitehead/jevscript) | 把语义判断作为语言原语的早期实验，目前实现的是 Jev 请求批处理验证脚本。 | JavaScript | 1 | Unknown | [固定提交](https://github.com/amberwhitehead/jevscript/blob/a01032218d8d57f84c5f310f585cd2da17671c9a/spike/m0.mjs) |
| [**ARCJ137442/jev-switch**](https://github.com/ARCJ137442/jev-switch) | A fast, local-first gateway for aggregating and routing TypeSafe Jev model endpoints \| 一款快速、本地优先的网关，用于聚合与路由 TypeSafe Jev 模型入口 | — | 1 | Apache-2.0 | 已核验 |
| [**arnab621/typesafe-jev-plugin**](https://github.com/arnab621/typesafe-jev-plugin) | 该插件用于创建可复用的 solution signature，并将 CSV、Excel 或文本数据集送入 Jev API 进行分类与评分后导出为 Excel 结果。 | — | 1 | Unknown | 已核验 |
| [**creativoma/here-we-go-jev**](https://github.com/creativoma/here-we-go-jev) | here-we-go-jev：对输入文本做分类或打分，交给本地规则继续处理。 | — | 1 | MIT | 已核验 |
| [**dsaad68/fuzzy-jev**](https://github.com/dsaad68/fuzzy-jev) | fuzzy-jev：对输入文本做分类或打分，交给本地规则继续处理。 | — | 1 | MIT | 已核验 |
| [**Eliot5566/jev-arena**](https://github.com/Eliot5566/jev-arena) | **用白話英文寫一個格鬥機器人，讓 System One 模型每秒幫它做好幾次決定。** | — | 1 | MIT | 已核验 |
| [**FlyPig23/Codex_ChatGPT_JEV_Switch**](https://github.com/FlyPig23/Codex_ChatGPT_JEV_Switch) | [智能切换设计文档](docs/routing.md) · [安全模型](docs/security.md) | — | 1 | MIT | 已核验 |
| [**huzeyfe07/jev-route**](https://github.com/huzeyfe07/jev-route) | jev-route：对输入文本做分类或打分，交给本地规则继续处理。 | — | 1 | MIT | 已核验 |
| [**kleosr/cursor-clijev-compaction**](https://github.com/kleosr/cursor-clijev-compaction) | cursor-clijev-compaction：对输入文本做分类或打分，交给本地规则继续处理。 | — | 1 | MIT | 已核验 |
| [**Kunyanli230/Jevometry**](https://github.com/Kunyanli230/Jevometry) | Jevometry：对输入文本做分类或打分，交给本地规则继续处理。 | — | 1 | MIT | 已核验 |
| [**logicrw/ask-jev**](https://github.com/logicrw/ask-jev) | 面向 AI 编程智能体与 CLI 管道的有界决策与原文提纯工具，硬性 280ms 时限，纯 Python 标准库零依赖，全链路 Fail-Open 优雅降级。 | — | 1 | GPL-3.0 | 已核验 |
| [**marcodicesare-dev/jev-skill**](https://github.com/marcodicesare-dev/jev-skill) | jev-skill：对输入文本做分类或打分，交给本地规则继续处理。 | — | 1 | MIT | 已核验 |
| [**MaxIvanyshen/jevkit**](https://github.com/MaxIvanyshen/jevkit) | jevkit：对输入文本做分类或打分，交给本地规则继续处理。 | — | 1 | Unknown | 已核验 |
| [**maxlibin/jev-toto**](https://github.com/maxlibin/jev-toto) | 这是一个 Rust 命令行工具，用于统计新加坡 TOTO 近期开奖数据，并请 Jev 模型给出每个号码的下期概率和冷热评分。 | — | 1 | MIT | 已核验 |
| [**miounet11/jevcode**](https://github.com/miounet11/jevcode) | Jev 是 TypeSafe 的 System One 决策模型：你给它**状态 + 类型化问题**，它返回**可直接进代码的决策**（带置信度），不是聊天文案。 | — | 1 | Unknown | 已核验 |
| [**mrkpatchaa/github-star-classifier-jev**](https://github.com/mrkpatchaa/github-star-classifier-jev) | github-star-classifier-jev：对输入文本做分类或打分，交给本地规则继续处理。 | — | 1 | Unknown | 已核验 |
| [**PhilippElhaus/Codex-Jev**](https://github.com/PhilippElhaus/Codex-Jev) | Codex-Jev：对输入文本做分类或打分，交给本地规则继续处理。 | — | 1 | MIT | 已核验 |
| [**pochang6/jev-buzzword-rush**](https://github.com/pochang6/jev-buzzword-rush) | 返しの文章を LLM に生成させると、体感速度は LLM の応答待ちで決まってしまいます。 このゲームでは、文章を一切生成しません。 | — | 1 | MIT | 已核验 |
| [**Resadan-dev/jev-zork**](https://github.com/Resadan-dev/jev-zork) | jev-zork：对输入文本做分类或打分，交给本地规则继续处理。 | — | 1 | MIT | 已核验 |
| [**sispehar/jev-for-splunk**](https://github.com/sispehar/jev-for-splunk) | jev-for-splunk：对输入文本做分类或打分，交给本地规则继续处理。 | — | 1 | Unknown | 已核验 |
| [**softpudding/jev-frontier-100**](https://github.com/softpudding/jev-frontier-100) | **Jev 1.13.0：77.0%。** 每个条件为 100 道题 × 3 轮；共保留 3,000 次有效回答。 不取最好的一轮，也不做多数投票。 | — | 1 | MIT | 已核验 |
| [**tapsin/jev-local**](https://github.com/tapsin/jev-local) | jev-local：对输入文本做分类或打分，交给本地规则继续处理。 | — | 1 | Unknown | 已核验 |
| [**Thestral12/pr-sieve**](https://github.com/Thestral12/pr-sieve) | GitHub Action 把 `.jev.yml` 规则编译成 Jev 问题，按数值决定 fail、comment 或 pass。 | TypeScript | 1 | MIT | [固定提交](https://github.com/Thestral12/pr-sieve/blob/9f37d439e37d99a145bc8367d982fe68df030e57/src/jev/client.ts) |
| [**Thneoly/r2r-jev**](https://github.com/Thneoly/r2r-jev) | r2r-jev：对输入文本做分类或打分，交给本地规则继续处理。 | — | 1 | Apache-2.0 | 已核验 |
| [**WanLanglin/jev-skills**](https://github.com/WanLanglin/jev-skills) | jev-skills：对输入文本做分类或打分，交给本地规则继续处理。 | — | 1 | Unknown | 已核验 |
| [**wenchenxi/jev-console**](https://github.com/wenchenxi/jev-console) | 给 TypeSafe 的 **Jev（System One 决策模型）** 做的本地小控制台 + 命令行。 | — | 1 | MIT | 已核验 |
| [**wotai-dev/typesafe-jev-tools**](https://github.com/wotai-dev/typesafe-jev-tools) | 该仓库提供一个 Claude Code hook，在写出 LLM 调用或手写分类器时注入三选一测试，提示当前判断是否需要模型、Jev 或普通代码。 | — | 1 | MIT | 已核验 |
| [**harshpuri84/slopcheck-jev**](https://github.com/harshpuri84/slopcheck-jev) | slopcheck-jev 在终端和自动化脚本中加入文本判断。 | — | 0 | MIT | 已核验 |
| [**rxova/jev-planner**](https://github.com/rxova/jev-planner) | jev-planner：Jev 对多Agent生成的计划打分并抉择是否需要交叉评审、哪个计划更强以及由谁来合并最终计划。 | — | 0 | MIT | 已核验 |

## Classification & Taxonomy

| 项目 | 简介 | 语言 | ⭐ | 许可证 | 证据 |
|---|---|---:|---:|---:|---|
| [**GiesN/typesafe-jev-workflow**](https://github.com/GiesN/typesafe-jev-workflow) | 一个异步 LangGraph 示例：让 Jev 把模拟邮件分成发票事务和普通邮件。 | Python | 11 | Unknown | [固定提交](https://github.com/GiesN/typesafe-jev-workflow/blob/251019670ebc3bf95870e924740d5876c1cd56b5/src/typesafe_ai_langgraph/typesafe_ai_langgraph_workflow.py) |
| [**reachjalil/jev-tree**](https://github.com/reachjalil/jev-tree) | 选项太多，一次问不下？先把目录分成树，让 Jev 逐层选分支，最后落到具体商品、事件类型或工作流。 | TypeScript | 9 | MIT | [固定提交](https://github.com/reachjalil/jev-tree/blob/95bff63bd653fee4dc71f33f9431dce0f81e2ca3/src/index.ts) |

## Codebase & Graph Pathfinding

| 项目 | 简介 | 语言 | ⭐ | 许可证 | 证据 |
|---|---|---:|---:|---:|---|
| [**dzhng/jevgrep**](https://github.com/dzhng/jevgrep) | 面向 Coding Agent 的生产级代码语义检索 CLI 工具，使用 Jev 智能识别相关文件、导读线索与原文片段，经 SWE-bench 测试验证可降低 ~30% Token 成本。 | — | 2062 | MIT | 已核验 |
| [**CelestoAI/celesto**](https://github.com/CelestoAI/celesto) | Celesto 的 PR 审查示例在沙盒中准备检查，再比较普通模型与 Jev 对候选问题的判断。 | — | 1002 | Apache-2.0 | [固定提交](https://github.com/CelestoAI/celesto/blob/fff7bb567752baee4ce195fcb78b5ee5e4da889f/examples/pr-review-jev/models.py#L96) |
| [**devagrawal09/jev-review**](https://github.com/devagrawal09/jev-review) | 分阶段检查 Git diff 或整个代码库，在本地面板里展示可复核的审查线索。 | TypeScript | 656 | MIT | [固定提交](https://github.com/devagrawal09/jev-review/blob/31f89602797fb7bea007f8a480bf368bf564954e/src/review/judgments.ts#L38) |
| [**jexp/neo4jev**](https://github.com/jexp/neo4jev) | 在 Neo4j 图谱里逐步找关系，让 Jev 在每个节点选择下一条边。 | Jupyter Notebook | 156 | MIT | [固定提交](https://github.com/jexp/neo4jev/blob/d157bbe496eb91813475156942bef1c6badfb342/src/neo4jev/navigator.py) |
| [**devagrawal09/jev-code**](https://github.com/devagrawal09/jev-code) | 给编程 Agent 提供代码定位、改动意图检查、测试失败整理和审查意见分流。 | TypeScript | 118 | MIT | [固定提交](https://github.com/devagrawal09/jev-code/blob/fd092558ebea389c81d44f9b10e826d9a72afaa3/src/adapters/jev.ts) |
| [**nassim-arifette/jevgrep**](https://github.com/nassim-arifette/jevgrep) | JevGrep 是一个基于 Jev 的语义代码搜索工具，可通过 CLI 或 MCP 按行为描述查找代码，并返回带文件路径和行号的原文片段。 | — | 95 | MIT | 已核验 |
| [**ellipsis-dev/blink**](https://github.com/ellipsis-dev/blink) | 用自然语言查找文件：多个 walker 沿目录树逐层搜索。 | TypeScript | 92 | Unknown | [固定提交](https://github.com/ellipsis-dev/blink/blob/a621ede75649303a933828c18c27ad800bb43ef0/src/search.ts) |
| [**devanshbatham/commit-miner**](https://github.com/devanshbatham/commit-miner) | 用 Jev 给 Git commit 的日志和 diff 分类，整理 bug 修复、安全修复、CWE 与改动类型。 | Rust | 36 | Unknown | [固定提交](https://github.com/devanshbatham/commit-miner/blob/977617ebce07c56b965253a68577b1d92b93fdf1/src/jev.rs) |
| [**BorisLeMeec/jev**](https://github.com/BorisLeMeec/jev) | Go 编写的 Claude Code 插件，用 Jev 查找相关文件、跨文件回答有界问题并处理大段读取。 | Go | 33 | MIT | [固定提交](https://github.com/BorisLeMeec/jev/blob/e81c1d006b8b23a616486610f311039088521d0c/internal/typesafe/client.go#L23) |
| [**buchmark/claude-jev**](https://github.com/buchmark/claude-jev) | 给 Claude Code 的审查发现、排错假设、设计方案和代码搜索结果增加一次 Jev 复核。 | — | 7 | MIT | [固定提交](https://github.com/buchmark/claude-jev/blob/06fe407f2894bc5c44f2dfc41e05d3592e5215a5/src/infrastructure/typesafe-jev.ts#L114) |
| [**baronunread/leanest**](https://github.com/baronunread/leanest) | 在现有测试运行器前增加 Jev 筛选，根据 diff 和测试源码判断哪些测试应运行。 | TypeScript | 5 | MIT | [固定提交](https://github.com/baronunread/leanest/blob/dfb8c6b83e5b362d8258ee64835e15b5766e08d2/src/jev-client.ts) |
| [**tonyzdev/PiJ**](https://github.com/tonyzdev/PiJ) | 基于 Pi 的终端编码 Agent，主模型负责推理、改代码与工具调用，Jev 提供辅助判断。 | TypeScript | 5 | MIT | [固定提交](https://github.com/tonyzdev/PiJ/blob/9588d6078af3f3be2b52906e0968ccf8e1542d74/src/jev.ts) |
| [**fatwang2/jev-review-action**](https://github.com/fatwang2/jev-review-action) | 可配置的 GitHub Action，用 Jev 检查目录投稿或给 PR 分类，并更新模板评论。 | — | 3 | MIT | [固定提交](https://github.com/fatwang2/jev-review-action/blob/0cc579cb2aa5b160b6d8a788a4775953a31c6e1e/src/typesafe.mjs#L36) |
| [**jimmyhealer/jevex**](https://github.com/jimmyhealer/jevex) | jevex 是一个 MCP 工具，先索引代码库再用 Jev 对候选内容排序，告诉 Agent 应该去读哪些文件和行范围。 | — | 1 | MIT | 已核验 |
| [**joacotornello/jev-prompt-enhancer**](https://github.com/joacotornello/jev-prompt-enhancer) | jev-prompt-enhancer：评估候选代码或关系与目标的相关程度，选择下一条路径。 | — | 1 | Unknown | 已核验 |
| [**neo4j-field/jev-graphrag**](https://github.com/neo4j-field/jev-graphrag) | 该仓库演示如何用 Jev 作为 Neo4j 知识图谱抽取与 GraphRAG 流程中的校准决策层，并包含实体去重演示和候选用例清单。 | — | 1 | Unknown | 已核验 |

## Context GC & Filter

| 项目 | 简介 | 语言 | ⭐ | 许可证 | 证据 |
|---|---|---:|---:|---:|---|
| [**tamaratran/fast-jev-compaction**](https://github.com/tamaratran/fast-jev-compaction) | 为 Claude Code 删减旧工具调用和结果，保留留下来的原文，不另写摘要。 | — | 7328 | MIT | [固定提交](https://github.com/tamaratran/fast-jev-compaction/blob/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/src/client.ts#L1) |
| [**tamaratran/jev-pruner**](https://github.com/tamaratran/jev-pruner) | Claude Code 输出修剪插件，在 Bash 执行后、结果进入主模型前筛掉部分冗余文本。 | TypeScript | 158 | MIT | [固定提交](https://github.com/tamaratran/jev-pruner/blob/c5bf7df482b9f8df3dcb838034f06da0d8d0d07a/src/jev.ts) |
| [**libingzheren/Jev-Mem**](https://github.com/libingzheren/Jev-Mem) | Jev-Mem 用轻量 System-One 控制器组织记忆并指导多关系检索，再由 System-Two 语言模型根据检索到的证据合成答案。 | — | 145 | MIT | 已核验 |
| [**GhalebDweikat/winnow**](https://github.com/GhalebDweikat/winnow) | 给 Claude Code 的长日志装一道筛子。暂时不相关的内容先藏起来，想看时还能完整找回。 | Python | 101 | MIT | [固定提交](https://github.com/GhalebDweikat/winnow/blob/51d80b945c74c8384bc47fa817179f668289afd8/sidecar/src/winnow/judge.py) |
| [**rokcso/bluenoise**](https://github.com/rokcso/bluenoise) | 为 X/Twitter 过滤帖子与回复的浏览器扩展；默认用本地规则，可选择用 Jev 检查未匹配的回复。 | TypeScript | 92 | MIT | [固定提交](https://github.com/rokcso/bluenoise/blob/ef81ea7a7c3677501d6de8f9235a4d6a866b573a/entrypoints/background.ts) |
| [**shitianfang/jev-use**](https://github.com/shitianfang/jev-use) | 把 Claude Code / Codex / pi 中不需要输出文本的判断步骤交给 Jev 执行，需要写字或置信度不足的步骤按类型化契约退回 LLM。 | — | 42 | MIT | 已核验 |
| [**samdotmak/jev-recall**](https://github.com/samdotmak/jev-recall) | Jev Recall 针对用户请求，用 Jev 模型对每条记忆逐一判断是否相关并筛选出相关记忆。 | — | 37 | MIT | 已核验 |
| [**compozy/yoshi**](https://github.com/compozy/yoshi) | 面向 Claude Code 与 Codex 的上下文剪枝代理，通过 Jev 评估历史条目必要性并保持工具调用协议结构完整。 | TypeScript | 28 | MIT | [固定提交](https://github.com/compozy/yoshi/blob/55c719718e5039f2276fbad804211682ae012f1e/benchmarks/jev-calibrate.ts#L1-L188) |
| [**bugkiwi/elons-job**](https://github.com/bugkiwi/elons-job) | 本地优先的 Chrome 扩展：先用规则筛选 X 回复，再让 Jev 判断色情、性暗示和引流内容，并提供可恢复的隐藏占位符。 | JavaScript | 20 | MIT | [固定提交](https://github.com/bugkiwi/elons-job/blob/be01f869871fcda5841fb77df3df6e46abbda493/src/background.js#L46-L101) |
| [**reachjalil/jevlogs**](https://github.com/reachjalil/jevlogs) | 在 OpenTelemetry 日志进入进一步分析前，用 Jev 标注诊断价值、优先级和路由信号。 | — | 17 | MIT | [固定提交](https://github.com/reachjalil/jevlogs/blob/b1ff60079c30d50a7f93dbfa09848f9539665d44/src/index.ts#L52) |
| [**ethanplusai/jev-chat-for-twitch**](https://github.com/ethanplusai/jev-chat-for-twitch) | 这是一个 Chrome 扩展，可在 Twitch 直播旁增加一列只显示经 Jev 筛选的消息。 | — | 13 | MIT | 已核验 |
| [**joelhooks/pi-fast-jev-compaction**](https://github.com/joelhooks/pi-fast-jev-compaction) | Pi 扩展：清理过时工具历史，保留原文；不足以释放上下文时交给 Pi 原生摘要。 | — | 13 | MIT | [固定提交](https://github.com/joelhooks/pi-fast-jev-compaction/blob/eb83f533f4fd10a08728b02c062c249afda5a4dc/src/core/request.ts#L8) |
| [**kubet/azdaja**](https://github.com/kubet/azdaja) | Azdaja 是与 harness 无关的递归语言模型层，将完整资料保存在本地求值器中并只对选定内容做语义递归，可配合 Jev 进行类型化语义判断。 | — | 13 | MIT | 已核验 |
| [**jerryfane/omp-jev-compaction**](https://github.com/jerryfane/omp-jev-compaction) | 为 Oh My Pi 删减工具历史的扩展，保留原文并复用旧判断以减少前缀反复改写。 | — | 11 | MIT | [固定提交](https://github.com/jerryfane/omp-jev-compaction/blob/5cc9daf51d97f0922d39f8396694631d6a87535c/src/asker.ts#L15) |
| [**leonaaardob/fast-dev-compaction**](https://github.com/leonaaardob/fast-dev-compaction) | Codex 插件与上下文压缩工具，在会话生命周期钩子中利用 Jev 判定历史记录的保留价值并进行无损还原。 | TypeScript | 9 | MIT | [固定提交](https://github.com/leonaaardob/fast-dev-compaction/blob/7147a4bab4ff9caf64ae44a2db1ab1f907a20291/dist/compact.js#L1-L234) |
| [**Nyarlathoteppppp/pi-jev-context**](https://github.com/Nyarlathoteppppp/pi-jev-context) | pi-jev-context：判断内容是否相关，由本地阈值决定保留或过滤。 | — | 7 | MIT | 已核验 |
| [**ShivamPansuriya/jev-skill-gate**](https://github.com/ShivamPansuriya/jev-skill-gate) | 按当前项目给 Claude Code 技能排相关度，减少默认加载的技能说明。 | JavaScript | 7 | MIT | [固定提交](https://github.com/ShivamPansuriya/jev-skill-gate/blob/1ab4c9a7cd117e1c7e129021303416bb7c2f5328/src/jev.mjs) |
| [**eran-broder/jev-skills**](https://github.com/eran-broder/jev-skills) | 该插件把技能库移出上下文窗口，让 Jev 在每一轮判断并只注入相关的技能。 | — | 6 | MIT | 已核验 |
| [**MithrilMan/your-signal**](https://github.com/MithrilMan/your-signal) | 一个自带 key 的 Chrome 扩展，让 Jev 按个人偏好给 X 信息流评分，再调整帖子的显示方式。 | JavaScript | 5 | MIT | [固定提交](https://github.com/MithrilMan/your-signal/blob/2970c069231b96f094f6fcfe4c11bfcf2da0ecb2/extension/background.js) |
| [**Parthkomalwad/jevbrief**](https://github.com/Parthkomalwad/jevbrief) | jevbrief 在数据源与 Jev 之间筛选事实并记录丢弃原因，然后向 Jev 提出单个明确问题并保存可回放的决策记录。 | — | 5 | MIT | 已核验 |
| [**wjw66/deepseek-harness-jev-pre-compaction**](https://github.com/wjw66/deepseek-harness-jev-pre-compaction) | 在上下文接近deepseek-harness插件，在上下文压缩阈值前，自动识别并移除低价值的工具结果，降低上下文占用 | — | 5 | MIT | 已核验 |
| [**alpha-tales/alphaoptimizer**](https://github.com/alpha-tales/alphaoptimizer) | AlphaOptimizer 会筛选 Codex 的大型命令与工具输出，保留关键行并将完整输出暂存本地供按需读取，在配置密钥时使用 Jev 排序相关内容。 | — | 4 | MIT | 已核验 |
| [**nourhelmi/pi-jev-compaction**](https://github.com/nourhelmi/pi-jev-compaction) | 该 Pi 扩展使用 Jev 评估较旧的工具输出并将其从上下文中清除，同时保留原始会话记录以便通过检索取回。 | — | 4 | MIT | 已核验 |
| [**Wang-auspicious/codex-jev-compaction**](https://github.com/Wang-auspicious/codex-jev-compaction) | 为 Codex 整理任务交接上下文，用 Jev 筛选旧工具记录，并保留选中内容的原文。 | JavaScript | 4 | MIT | [固定提交](https://github.com/Wang-auspicious/codex-jev-compaction/blob/26fa09f83113a777b0d0db25d847f1c2a25d3388/plugins/codex-jev-compaction/lib/core.mjs) |
| [**Waxmell114514/jev-compaction**](https://github.com/Waxmell114514/jev-compaction) | 该项目让 Jev 只为片段打分而不改写原文，将低分 Agent 上下文移入存储并留下可调用 expand 取回原文的指针。 | — | 4 | MIT | 已核验 |
| [**kolawong/fast-compaction-dsh**](https://github.com/kolawong/fast-compaction-dsh) | DSH 的上下文压缩插件 | — | 3 | Unknown | 已核验 |
| [**lazniak/jevskill**](https://github.com/lazniak/jevskill) | jevskill：判断内容是否相关，由本地阈值决定保留或过滤。 | — | 3 | MIT | 已核验 |
| [**Dharundp6/jev-carryforward**](https://github.com/Dharundp6/jev-carryforward) | 这是一个按项目保存事实的 MCP 服务器，在开始任务时用 Jev 对已保存内容打分并只返回当前相关条目。 | — | 2 | MIT | 已核验 |
| [**KamilPostrozny/pi-fast-jev-compaction**](https://github.com/KamilPostrozny/pi-fast-jev-compaction) | 该扩展使用 TypeSafe Jev 逐个工具调用决定旧结果在模型 Context 中的保留，不改写用户与助手正文且保持持久会话记录完整。 | — | 2 | MIT | 已核验 |
| [**kevinpita/pi-jev-context**](https://github.com/kevinpita/pi-jev-context) | Pi 的可逆上下文筛选扩展，用 Jev 判断旧消息是否仍值得发给主模型。 | TypeScript | 2 | MIT | [固定提交](https://github.com/kevinpita/pi-jev-context/blob/640ffa74c376fe8e487e4fec3e75de741f5b53e1/src/jev.ts) |
| [**redreamality/jev-skill-selection**](https://github.com/redreamality/jev-skill-selection) | **别再把每个 `SKILL.md` 都塞进提示词。** 在第一条模型消息之前做 keep/drop —— 压缩上下文，省 token。 | — | 2 | MIT | 已核验 |
| [**silvariasereneblossom/jeverifier**](https://github.com/silvariasereneblossom/jeverifier) | jeverifier：判断内容是否相关，由本地阈值决定保留或过滤。 | — | 2 | MIT | 已核验 |
| [**Excalibur9527/dsh-jev**](https://github.com/Excalibur9527/dsh-jev) | DSH Plugin（DeepSeek Harness 插件）：每轮对话调用 typesafe.ai systemone(jev) 判定用户情绪/意图，结果注入模型上下文；API Key 与全部参数在 GUI 设置页配置 | — | 1 | MIT | 已核验 |
| [**SqaaSSL/openclaw-jev-compaction**](https://github.com/SqaaSSL/openclaw-jev-compaction) | 这是一个为 OpenClaw 提供的逐字上下文压缩引擎，它请 Jev 判断哪些工具调用和工具结果仍需保留并删除其余内容，且从不做总结。 | — | 1 | MIT | 已核验 |
| [**tusharck/jev-inbox-queue**](https://github.com/tusharck/jev-inbox-queue) | 该项目用 Jev 回答每个邮件主题的七个类型化问题，再用 Python 规则将其整理为待办行动队列。 | — | 1 | MIT | 已核验 |
| [**Wang-auspicious/pi-jev-compaction**](https://github.com/Wang-auspicious/pi-jev-compaction) | 给 Pi 做抽取式上下文压缩：让 Jev 判断旧的只读工具记录是否仍有用，保留部分直接复制原文。 | TypeScript | 1 | MIT | [固定提交](https://github.com/Wang-auspicious/pi-jev-compaction/blob/058d91db752f97c7d52062e465eb151bddab060d/src/client.ts) |
| [**willfish/pi-observational-memory-jev**](https://github.com/willfish/pi-observational-memory-jev) | 该扩展将历史切块后由 Jev 判断保留与分类，原样保存记录并用确定性渲染做压缩。 | — | 1 | MIT | 已核验 |
| [**xuan7zhang/jev-toolspace**](https://github.com/xuan7zhang/jev-toolspace) | 该仓库使用 Jev 作为相关性判断器，为 tool-using LLM Agent 构建任务级工具空间，对每个请求或执行轨迹为注册表中每个工具打分并保留 top-K 工具。 | — | 1 | Unknown | 已核验 |
| [**zbush/jev-context**](https://github.com/zbush/jev-context) | Codex 代码搜索插件：ripgrep 找候选，Jev 过滤后只返回判为相关的片段。 | — | 1 | MIT | [固定提交](https://github.com/zbush/jev-context/blob/2be700faebe862c259a16ac9f78266b728874ef6/src/jev.mjs#L46) |
| [**ilkerulusoy/pi-jev-compact**](https://github.com/ilkerulusoy/pi-jev-compact) | Pi 上下文整理扩展，默认筛除旧工具历史，另可选择把助手文字纳入候选。 | TypeScript | 0 | Unknown | [固定提交](https://github.com/ilkerulusoy/pi-jev-compact/blob/7d54b2e9a437fcf445c7f50aa49d673dbd863176/src/core/jev.ts#L3) |
| [**joslynSmall/fast-jev-compaction-pi**](https://github.com/joslynSmall/fast-jev-compaction-pi) | 为 Pi 的上下文压缩筛选并原样保留关键工具证据，删除或截短过时的工具输出。 | — | 0 | MIT | 已核验 |
| [**Wing9897/jev.tg**](https://github.com/Wing9897/jev.tg) | Laya 是選用本機模型，權重不在這個 repo。需要時再裝，第一次判斷才會下載： | — | 0 | Unknown | 已核验 |

## Creative Tools

| 项目 | 简介 | 语言 | ⭐ | 许可证 | 证据 |
|---|---|---:|---:|---:|---|
| [**vercel-labs/json-render**](https://github.com/vercel-labs/json-render) | json-render 网站里的 Jev UI 组合实验：从预定义组件与属性候选中选择，再由代码组装界面。 | TypeScript | 18476 | Apache-2.0 | [固定提交](https://github.com/vercel-labs/json-render/blob/3ad381881194e7011ad3ccd6d668033495a06c29/apps/web/lib/jev/compose.ts) |
| [**trungdq88/youtube-sponsor-detection**](https://github.com/trungdq88/youtube-sponsor-detection) | 结合实时音频与字幕由 Jev 驱动的 YouTube 视频赞助广告片段检测与自动跳过扩展。 | JavaScript | 109 | Unknown | [固定提交](https://github.com/trungdq88/youtube-sponsor-detection/blob/de01f0568d043035889a296a61ce21e0accc8b16/extension/lib/jev.js#L1-L541) |
| [**ChetasLua/jevmeter**](https://github.com/ChetasLua/jevmeter) | 把视频转成带评分仪表的视频成片：Jev 按选定规则给字幕句子评分，再由渲染器叠加显示。 | Python | 105 | MIT | [固定提交](https://github.com/ChetasLua/jevmeter/blob/cbf8e117b5b8835e3294c3a8ee652c7dfa737a9a/jevmeter/score.py) |
| [**datawhalechina/jev-cookbook**](https://github.com/datawhalechina/jev-cookbook) | ⚡ 适合中国宝宝的 Jev 入门教程｜手把手带你了解关于 Jev 的一切——Jupyter Notebook 轻松实验，从三种问题原语到 18 篇实战配方、语音智能家居、模型评测与本地微调，全面掌握 System One 判断模型的开发范式 | — | 94 | Unknown | 已核验 |
| [**achimala/jev-paint**](https://github.com/achimala/jev-paint) | 把 Jev 的结构化判断接进程序；具体用途与决策流程请查看项目源码。 | — | 63 | MIT | 已核验 |
| [**RafalWilinski/vibecheck**](https://github.com/RafalWilinski/vibecheck) | 在 X 发帖前显示一个 Jev 评分卡，检查草稿的清晰度、语气、冒犯倾向等维度。 | JavaScript | 49 | Unknown | [固定提交](https://github.com/RafalWilinski/vibecheck/blob/badf9dad5deecababd8afe43a574a5ea6d376711/background.js) |
| [**AlbionaHoti/refgarden**](https://github.com/AlbionaHoti/refgarden) | 创意参考图库，汇集 The Met、NASA 与 Cosmos 的素材；本地 Explore 模式可使用 Jev。 | TypeScript | 33 | MIT | [固定提交](https://github.com/AlbionaHoti/refgarden/blob/6affd25a31dd0ed39fc9f71508732fb7ee0b8acc/src/jev-client.ts) |
| [**DanRWilloughby/snifftest**](https://github.com/DanRWilloughby/snifftest) | Markdown 与纯文本写作检查器，用本地规则和可选 Jev 判断标记文风问题。 | TypeScript | 33 | MIT | [固定提交](https://github.com/DanRWilloughby/snifftest/blob/240653e2b082c114c38fed50a42e7eb311e21219/src/jev.ts#L50) |
| [**cocktailpeanut/jevthoven**](https://github.com/cocktailpeanut/jevthoven) | 用一句话描述音乐，让 Jev 选择乐器、和声与逐小节片段，生成可编辑的多轨 MIDI。 | TypeScript | 16 | MIT | [固定提交](https://github.com/cocktailpeanut/jevthoven/blob/e5e0c67d8bae92f96c9ce05138f55c3ab72c6aac/app/server/provider.ts) |
| [**harshil1712/slidepilot**](https://github.com/harshil1712/slidepilot) | 基于语音语义理解的 Slidev 自动翻页控制器，运行于 Cloudflare Agents 与 Jev 之上。 | TypeScript | 8 | MIT | [固定提交](https://github.com/harshil1712/slidepilot/blob/8ba4e89b56e4f9a08be2f1f69346240cab95a7b6/apps/worker/src/decision.ts#L1-L219) |
| [**joevidev/ui-generator-instinct-jev**](https://github.com/joevidev/ui-generator-instinct-jev) | 描述想要的界面，Jev 从既有 shadcn/ui 组件、字段和样式中选择，应用负责渲染。 | TypeScript | 7 | Unknown | [固定提交](https://github.com/joevidev/ui-generator-instinct-jev/blob/9a81c2dc23b561980c7a6d4302c71f34e5ab4ae6/lib/decide.ts) |
| [**paramjeetn/jev-cookbook**](https://github.com/paramjeetn/jev-cookbook) | jev-cookbook：在有限的素材或组件候选中选择，并由本地程序呈现结果。 | — | 7 | MIT | 已核验 |
| [**hndrr/ComfyUI-Jev**](https://github.com/hndrr/ComfyUI-Jev) | 该项目为 ComfyUI 提供使用 Jev 进行文本选择、条件判断、评分和数字提取的自定义节点，并可将结果传递给其他节点使用。 | — | 6 | MIT | 已核验 |
| [**kolibril13/jev-in-blender-experiment**](https://github.com/kolibril13/jev-in-blender-experiment) | 这是一个 Blender 扩展，在三维视图侧栏增加 Jev 搜索页，可用自然语言查找并执行对应的 Blender 操作。 | — | 6 | MIT | 已核验 |
| [**VBS2004/jev-windows-agent**](https://github.com/VBS2004/jev-windows-agent) | jev-windows-agent：在有限的素材或组件候选中选择，并由本地程序呈现结果。 | — | 5 | MIT | 已核验 |
| [**colinmcdermott/emoji-jev**](https://github.com/colinmcdermott/emoji-jev) | 该应用根据用户输入的文本调用 Jev 并行获取表情 Choice、情绪 Choice、Score 和 Boolean 结果，并将其显示为表情键盘。 | — | 3 | Unknown | 已核验 |
| [**hazlema/jev-riffs**](https://github.com/hazlema/jev-riffs) | jev-riffs：在有限的素材或组件候选中选择，并由本地程序呈现结果。 | — | 3 | MIT | 已核验 |
| [**adammichaelwood/jev-music-theory-1**](https://github.com/adammichaelwood/jev-music-theory-1) | 用 Jev 做和声练习、乐理选择题，并通过连续选择和弦播放电钢琴。 | TypeScript | 2 | Unknown | [固定提交](https://github.com/adammichaelwood/jev-music-theory-1/blob/7c5b4b8b7e40309f87388c3c5c4d3ed6a3872928/core/decide/jev.ts) |
| [**Anson-gzy/jev-paste**](https://github.com/Anson-gzy/jev-paste) | **jev-paste** 是一款专为 macOS 设计的智能剪贴板实体提取与内联补全工具。 | — | 2 | MIT | 已核验 |
| [**drpaneas/jev**](https://github.com/drpaneas/jev) | jev：在有限的素材或组件候选中选择，并由本地程序呈现结果。 | — | 2 | MIT | 已核验 |
| [**mahmut-gundogdu/bes-kelime-jev**](https://github.com/mahmut-gundogdu/bes-kelime-jev) | 这是一个土耳其语聊天小应用，无论输入什么都只用五个固定短语之一回复，具体用哪个由 Jev evaluation 模型选择。 | — | 2 | MIT | 已核验 |
| [**MM-sheng/jevspeak**](https://github.com/MM-sheng/jevspeak) | JevSpeak 让 Jev 对用户消息做出约13个概率性选择并形成语义中间表示，再用确定性语言编译器将其渲染成英文或中文句子。 | — | 2 | MIT | 已核验 |
| [**nemalabs/voicevox-jev-proxy**](https://github.com/nemalabs/voicevox-jev-proxy) | voicevox-jev-proxy：在有限的素材或组件候选中选择，并由本地程序呈现结果。 | — | 2 | MIT | 已核验 |
| [**phureewat29/jev-got**](https://github.com/phureewat29/jev-got) | 《权力的游戏》文字冒险：大模型写剧情，Jev 判断地点、情绪和危险，再切换配乐与背景。 | TypeScript | 2 | Unknown | [固定提交](https://github.com/phureewat29/jev-got/blob/232fc0ad0cc6f4d4e095df71ac5f05b0f49033a9/src/core/providers/TypeSafe.ts) |
| [**suidouble/let-jev-speak**](https://github.com/suidouble/let-jev-speak) | 该项目通过一次一词地反复调用分类接口，让只做分类的 Jev 拼出自由文本回答。 | — | 2 | MIT | 已核验 |
| [**wustep/jev-playground**](https://github.com/wustep/jev-playground) | jev-playground：在有限的素材或组件候选中选择，并由本地程序呈现结果。 | — | 2 | Unknown | 已核验 |
| [**Faizullah9181/jev-esketcher**](https://github.com/Faizullah9181/jev-esketcher) | jev-esketcher：在有限的素材或组件候选中选择，并由本地程序呈现结果。 | — | 1 | MIT | 已核验 |
| [**cwdx/1-million-emojis**](https://github.com/cwdx/1-million-emojis) | 1-million-emojis：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 0 | MIT | 已核验 |

## Data & Search

| 项目 | 简介 | 语言 | ⭐ | 许可证 | 证据 |
|---|---|---:|---:|---:|---|
| [**zilliztech/deep-searcher**](https://github.com/zilliztech/deep-searcher) | 开源深度研究与私域检索框架，集成 Jev 决策对搜索步长与早停做评估判断。 | — | 8292 | Apache-2.0 | 已核验 |
| [**zilliztech/GPTCache**](https://github.com/zilliztech/GPTCache) | 基于 Jev 的语义缓存评估器，通过 Noul 二元判断核验缓存响应是否可复用于当前请求。 | — | 8209 | MIT | 已核验 |
| [**zilliztech/memsearch**](https://github.com/zilliztech/memsearch) | memsearch：Jev 对每个候选记忆片段判断其是否包含回答查询所需的特定事实并给出noul相关性分数，用于重排序检索结果。 | — | 2705 | MIT | 已核验 |
| [**milvus-io/bootcamp**](https://github.com/milvus-io/bootcamp) | Milvus 官方实战教程：结合 Milvus 向量检索与 Jev 原语，实现搜索重排、查询路由与门禁过滤。 | — | 2445 | Apache-2.0 | 已核验 |
| [**kentcdodds/kody**](https://github.com/kentcdodds/kody) | 可选的二段检索：先扩大混合召回，再用 Cloudflare Workers AI 上的 `typesafe/jev` Score 重排。 | TypeScript | 723 | Unknown | [固定提交](https://github.com/kentcdodds/kody/blob/ed9275186dc817530dd2289e62c208ac3809391f/packages/worker/src/mcp/tools/search-jev-rerank.ts) |
| [**superagents-lab/jev-search**](https://github.com/superagents-lab/jev-search) | 用自然语言搜网页：Jev 选择搜索来源和时间范围，再给返回的链接排序。 | — | 503 | MIT | [固定提交](https://github.com/superagents-lab/jev-search/blob/522868762f0637b20bf533f136e930cceb83b9f3/src/lib/typesafe.ts#L48) |
| [**realZachi/pg-jev**](https://github.com/realZachi/pg-jev) | 在 PostgreSQL 查询中用自然语言给数据行筛选、分类和排序。 | Shell | 391 | Unknown | [固定提交](https://github.com/realZachi/pg-jev/blob/afd11fa856d7a2b831a1bfd8ee7f869ce8efcd62/sql/jev--0.2.0.sql) |
| [**zilliztech/vector-graph-rag**](https://github.com/zilliztech/vector-graph-rag) | 该项目从文档中抽取三元组并将实体与关系存为 Milvus 向量，通过向量检索、子图扩展和单次 LLM 重排回答多跳问题，并提供可选的 Jev 重排器。 | — | 253 | MIT | 已核验 |
| [**uehaj/jev-semgrep**](https://github.com/uehaj/jev-semgrep) | 用 Jev 给每一行打“是否符合某含义”的分，可用 AND/OR/NOT 组合，并支持跨语言查询。 | JavaScript | 144 | Unknown | [固定提交](https://github.com/uehaj/jev-semgrep/blob/21120e9ee634defdb279b7243e03ea84aaeed2da/semgrep.mjs) |
| [**AkashPriyadarshii/jev-curate**](https://github.com/AkashPriyadarshii/jev-curate) | Rust 数据集筛选实验，用 Jev 给文本记录评分并分流到保留或拒绝结果。 | Rust | 96 | MIT | [固定提交](https://github.com/AkashPriyadarshii/jev-curate/blob/a35d420cdf15eb1d109171fc896ddc54e6cb9a45/src/client.rs) |
| [**giuliosmall/pg_typesafe**](https://github.com/giuliosmall/pg_typesafe) | 一个预览阶段的 PostgreSQL C 扩展，让 SQL 直接调用 Jev 做分类、是非判断和评分。 | C | 87 | MIT | [固定提交](https://github.com/giuliosmall/pg_typesafe/blob/4b5bfc1df11b18c3f07bb10804eeb47e4508ec6a/typesafe.c) |
| [**RenaGao/jev-dataops**](https://github.com/RenaGao/jev-dataops) | 该项目是一个开源工作台，用于上传并筛选数据、用 JEV 评估数据质量、运行 LoRA 训练，并在保留测试集上评估模型。 | — | 61 | MIT | 已核验 |
| [**milvus-io/milvus-model**](https://github.com/milvus-io/milvus-model) | 该库为 Milvus 集成了来自 OpenAI、Voyage AI、Cohere、Jina AI、TypeSafe 以及 SentenceTransformers 和 Hugging Face TEI 的 embedding 和 reranker 模型。 | — | 60 | Apache-2.0 | 已核验 |
| [**bodepudimuneendra-netizen/laya-jev-GraphRAG**](https://github.com/bodepudimuneendra-netizen/laya-jev-GraphRAG) | 该项目是一个 Agentic GraphRAG 引擎，使用可切换的 Laya 与 Jev 决策模型完成文档摄取、检索、A* 图遍历和答案生成，并支持 Neo4j、Memgraph、Apache AGE 和 Kùzu 四种图数据库。 | — | 49 | Apache-2.0 | 已核验 |
| [**pnthn-ai/polar_llama**](https://github.com/pnthn-ai/polar_llama) | Polars 上的并行推理库：聊天模型走各家补全接口，Jev 则按行做 Noul、Choice、Score，或对整份文档套一份类型化契约。 | — | 30 | MIT | 已核验 |
| [**colliber/duckdb-jev**](https://github.com/colliber/duckdb-jev) | 一个 DuckDB 扩展，在 SQL 中调用 Jev，并把回答转换成 ENUM、数值或 STRUCT 等类型。 | C++ | 28 | MIT | [固定提交](https://github.com/colliber/duckdb-jev/blob/fad67eb4a1def91fcf1efbc96bdf5e6e11208644/src/jev_client.cpp) |
| [**ktaletsk/jevframe**](https://github.com/ktaletsk/jevframe) | 该库使用 TypeSafe Jev 对 pandas 和 Polars DataFrame 的每一行提出自然语言问题，并返回带完整概率分布的文本分类、情感分析和评分结果。 | — | 21 | MIT | 已核验 |
| [**hev/reranker**](https://github.com/hev/reranker) | 把查询和最多约 30 篇候选放进一次 Jev state，每篇一个 Noul「是否相关」，用来过滤或重排。 | Python | 14 | Apache-2.0 | [固定提交](https://github.com/hev/reranker/blob/1eb47266270b32b2a3667f9fb89646378ca9c9d6/hev_rerank/rerank.py#L1-L105) |
| [**kylemclaren/jevql**](https://github.com/kylemclaren/jevql) | 在普通 PostgreSQL 查询外加一层语义处理，用 Jev 筛选、分组和排序，无需安装数据库扩展。 | Go | 14 | MIT | [固定提交](https://github.com/kylemclaren/jevql/blob/b5e546bafd18a2c887142bbbdfbce7ed9e06960e/internal/typesafe/client.go) |
| [**zhuyansen/jev-search-rerank-eval**](https://github.com/zhuyansen/jev-search-rerank-eval) | 中英文检索重排效果评估系统，对比 Jev 重排与词法搜索、向量检索及混合融合基线，并分析评审者自循环偏差。 | Python | 10 | MIT | [固定提交](https://github.com/zhuyansen/jev-search-rerank-eval/blob/c896f14e944182e17a002dd7546f06ba3788d586/src/jse/rankers/jev.py#L1-L46) |
| [**jeffonelson/jev-bigquery-cloudrun**](https://github.com/jeffonelson/jev-bigquery-cloudrun) | 该仓库通过私有的 Cloud Run 适配器调用 Jev API，对 BigQuery 中的 30 张虚构支持工单按负责团队、紧急程度和阻塞情况分类，并将结果存回 BigQuery 供 SQL 查询。 | — | 9 | Unknown | 已核验 |
| [**aifabrice/jev-rag**](https://github.com/aifabrice/jev-rag) | **Jev RAG 是一个开源的本地知识库检索工具，提供七种可切换路径：默认 BM25 + Jev、无向量 Agentic Search、Embedding 混合检索、多轮 Agentic Hybrid、知识分类树路由、统一 Jev Passage Gate，以及两级 Jev Line Search。** | — | 8 | MIT | 已核验 |
| [**prasanthj/duckdb-jev**](https://github.com/prasanthj/duckdb-jev) | 该仓库是原生 C++ DuckDB 扩展，可直接在 SQL 中调用 Jev 进行语义判断、分类和打分，并支持批量与流式推理。 | — | 8 | Apache-2.0 | 已核验 |
| [**WiktorB2004/llama-index-jev**](https://github.com/WiktorB2004/llama-index-jev) | 为 LlamaIndex 提供 Jev 重排序器和路由器，给检索片段评分或选择查询工具。 | Python | 8 | MIT | [固定提交](https://github.com/WiktorB2004/llama-index-jev/blob/72c73dc50bca4b7ea6928ef65ea09f1a7ee4a01e/packages/llama-index-postprocessor-jev/llama_index/postprocessor/jev/openrouter.py) |
| [**PromtEngineer/jev-harness**](https://github.com/PromtEngineer/jev-harness) | jev-harness：给候选记录判断相关性或打分，再由本地程序筛选和排序。 | — | 7 | MIT | 已核验 |
| [**stas4000/jev-papers**](https://github.com/stas4000/jev-papers) | 该项目用 Jev 对 1000 篇 arXiv AI 论文各做一次 24 选一主题分类，再用 LLM judge 抽样复核并在静态页面中展示主题分布。 | — | 7 | MIT | 已核验 |
| [**sufianetaouil/every**](https://github.com/sufianetaouil/every) | 代码库全量函数语义问答工具：对代码库内每个函数发起是非问题提问，按 Noul 概率在秒级内排列出最相关的函数。 | — | 7 | MIT | 已核验 |
| [**keltokhy/jlink**](https://github.com/keltokhy/jlink) | jlink 让用户用 plain English 写出匹配规则，在本地做候选 blocking 生成记录对，再用 Jev Noul 逐对判断是否为同一实体并给出概率，然后解析链接并提供审计与引用文本。 | — | 6 | MIT | 已核验 |
| [**larguesa/jev-search**](https://github.com/larguesa/jev-search) | 这是一个用 Jev 按语义逐行检索文本的 Python 命令行工具，用作关键词搜索的补充视角。 | — | 6 | MIT | 已核验 |
| [**teempai/jev-in-codex**](https://github.com/teempai/jev-in-codex) | 该仓库是 Codex 插件，通过 Jev 对工作区内 JSONL 文本记录进行批量标注，生成每条记录带一个标签的输出文件以供复核。 | — | 6 | MIT | 已核验 |
| [**AkashPriyadarshii/jev-scout**](https://github.com/AkashPriyadarshii/jev-scout) | 用搜索结果建立真实仓库与 Rust crate 候选，再让 Jev 按需求相关性进行评分和选择。 | Rust | 5 | MIT | [固定提交](https://github.com/AkashPriyadarshii/jev-scout/blob/acae39260212267288353451c6977aeab7d6af1d/src/jev.rs) |
| [**EugeneBoondock/jevsql**](https://github.com/EugeneBoondock/jevsql) | 给 SQLite 加入 Jev 语义判断，可过滤、排序、匹配记录并追踪判断所用的证据。 | JavaScript | 5 | MIT | [固定提交](https://github.com/EugeneBoondock/jevsql/blob/e0b42f3b4312189f0b9c3996818675c714f126e7/src/client.mjs#L5) |
| [**jkrup/jeveryword**](https://github.com/jkrup/jeveryword) | 该库将文本切分为带编号的词供 Jev 选择，并将选中的编号还原为原文子串，用于字段抽取、词标注和原文引用。 | — | 5 | MIT | 已核验 |
| [**kylemclaren/jevpdf**](https://github.com/kylemclaren/jevpdf) | 打开 PDF 并用自己的话提问，应用用 Jev 判断每一行是否回答问题并高亮匹配行。 | — | 5 | MIT | 已核验 |
| [**Peu77/JevFind**](https://github.com/Peu77/JevFind) | 这是一个由 Jev 驱动的语义代码搜索工具，可用自然语言查询找到相关文件、行范围和代码片段。 | — | 5 | MIT | 已核验 |
| [**sarathi-aiml/jevsql**](https://github.com/sarathi-aiml/jevsql) | 该项目使用 Jev 回答类型化问题，再由代码组装参数化 SELECT 查询来实现自然语言转 SQL。 | — | 4 | Unknown | 已核验 |
| [**shinpr/jev-reranker**](https://github.com/shinpr/jev-reranker) | 该工具从标准输入读取 JSON 候选文档，并使用 Jev 按查询对其进行重排、过滤或压缩后输出。 | — | 4 | MIT | 已核验 |
| [**CompleteTech-LLC-AI-Research/jev-311-heatmap**](https://github.com/CompleteTech-LLC-AI-Research/jev-311-heatmap) | 该项目下载 NYC 311 投诉数据，用 JEV 评估投诉描述，并在地理网格上生成可交互热力图。 | — | 3 | Unknown | 已核验 |
| [**hemanth/hfjev**](https://github.com/hemanth/hfjev) | hfjev 可加载 Hugging Face 数据集，并使用 Choice、Score 和 Noul 等 Jev 原语对每一行进行类型化语义分类。 | — | 3 | MIT | 已核验 |
| [**keltokhy/jselect**](https://github.com/keltokhy/jselect) | jselect 根据任务挑选带来源引用的原文片段，并用 Jev 判断相关性，在 Token 预算内组装可直接供 Agent 阅读的上下文。 | — | 3 | MIT | 已核验 |
| [**romeromarcelo/jev-retrieval**](https://github.com/romeromarcelo/jev-retrieval) | 这是一个用 Rust 编写的代码与文档检索命令行工具，先用本地 BM25 召回候选文件，再用 Jev 的 Noul 逐窗口验证相关性，最后用 Choice 重排并输出带分数的文件路径与行号。 | — | 3 | Apache-2.0 | 已核验 |
| [**shimo4228/jev-research-pipeline**](https://github.com/shimo4228/jev-research-pipeline) | 该项目是一个每日研究监测管道，确定性 Python 控制流程，TypeSafe Jev 按研究问题筛选来源，Qwen 撰写 Obsidian 笔记。 | — | 3 | MIT | 已核验 |
| [**aarzhaev/jevtok-ts**](https://github.com/aarzhaev/jevtok-ts) | jevtok-ts：给候选记录判断相关性或打分，再由本地程序筛选和排序。 | — | 2 | MIT | 已核验 |
| [**abhishekmamdapure/jev-information-extraction**](https://github.com/abhishekmamdapure/jev-information-extraction) | jev-information-extraction：Jev 为每个自然语言问题从当前页面的文本块候选中选择最相关的答案块并返回概率排名。 | — | 2 | Unknown | 已核验 |
| [**halfspin-qc/jev-reviews**](https://github.com/halfspin-qc/jev-reviews) | jev-reviews：给候选记录判断相关性或打分，再由本地程序筛选和排序。 | — | 2 | Unknown | 已核验 |
| [**komikat/jev-bfs**](https://github.com/komikat/jev-bfs) | 基于 Jev 引导的维基百科链接竞速寻路器：利用 Jev 评估出站链接相关性，在终端实时寻径两词条之间的最短路径。 | — | 1 | MIT | 已核验 |
| [**nothans/sieve**](https://github.com/nothans/sieve) | sieve：Jev 对每对笔记做五选一关系判断、对每个问题或规则给出是否成立的概率，用于矛盾检测、排序和门禁。 | — | 1 | MIT | 已核验 |
| [**ozers/jevsome-projects**](https://github.com/ozers/jevsome-projects) | 一个 Jev 项目目录与发现流水线，保存接入证据，并可用 Jev 辅助分类。 | JavaScript | 1 | MIT | [固定提交](https://github.com/ozers/jevsome-projects/blob/ba0bfdceb27f8ba1df10f76d4b5b090438eee952/pipeline/lib/jev.mjs) |
| [**sunyasheng/JevDeepResearch**](https://github.com/sunyasheng/JevDeepResearch) | JevDeepResearch：对输入文本做分类或打分，交给本地规则继续处理。 | — | 1 | Apache-2.0 | 已核验 |
| [**vijaycinn/el-jev**](https://github.com/vijaycinn/el-jev) | el-jev：给候选记录判断相关性或打分，再由本地程序筛选和排序。 | — | 1 | MIT | 已核验 |
| [**zzz1YAO/DataJev**](https://github.com/zzz1YAO/DataJev) | DataJev 让 LLM 编写并由 Python 执行单步数据分析，再由 Jev 控制器根据压缩分析状态决定 CONTINUE、SWITCH、VERIFY 或 STOP。 | — | 1 | MIT | 已核验 |

## Decision Tools

| 项目 | 简介 | 语言 | ⭐ | 许可证 | 证据 |
|---|---|---:|---:|---:|---|
| [**monteduro/killmyidea**](https://github.com/monteduro/killmyidea) | 创业点子评估演示，用 Jev 的多项评分给出 KILL、FIX 或 SHIP 标签。 | TypeScript | 247 | Unknown | [固定提交](https://github.com/monteduro/killmyidea/blob/bc853421f2eb6f17da435621896dd6cd881a051c/src/lib/typesafe.ts) |
| [**altryne/jevify**](https://github.com/altryne/jevify) | 一个 Agent Skill，帮助找出项目中适合用 Jev 的判断环节，并设计问题与对照实验。 | Python | 37 | MIT | [固定提交](https://github.com/altryne/jevify/blob/9b50ba134487f9a5a568386583c18e876cae3f56/scripts/run_cases.py) |
| [**keeltrace/hermes-jev**](https://github.com/keeltrace/hermes-jev) | Hermes Agent 的异步 Jev 辅助决策系统，用于相关性、完成度、恢复路径和可选工具准入等判断。 | Python | 34 | MIT | [固定提交](https://github.com/keeltrace/hermes-jev/blob/4feea5ef45aeb301622f18175ed4cf2e068b99bd/hermes_jev/client.py) |
| [**0x7067/claude-jev**](https://github.com/0x7067/claude-jev) | claude-jev：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 20 | MIT | 已核验 |
| [**valentynkit/jev-belay**](https://github.com/valentynkit/jev-belay) | Claude Code 的 Stop 钩子：本地先看本轮是否改过文件、是否已有通过的检查，只有这时才问 Jev 结束语是不是未经核实的完成声明。 | — | 20 | MIT | 已核验 |
| [**yushen100/wechat-jev-assistant**](https://github.com/yushen100/wechat-jev-assistant) | Windows 微信对话分析助手：本地读取、脱敏、TypeSafe Jev 判断与加密历史 | — | 18 | Unknown | 已核验 |
| [**valentynkit/jev-commit**](https://github.com/valentynkit/jev-commit) | commit-msg 钩子：一次 Jev 请求对照暂存 diff 给提交说明打五个 Noul，默认只警告。默认拦住提交的是本地正则腰带对新增行的高置信命中；secret_shaped Noul 只在 --strict 时参与拦截。 | — | 12 | MIT | 已核验 |
| [**Aimark-dai/jev-chat-windows-deepseek-jev**](https://github.com/Aimark-dai/jev-chat-windows-deepseek-jev) | Windows 微信回复助手：DeepSeek 官方生成话术，TypeSafe JEV 官方判断排序，支持可取消的 3 秒自动发送。 | — | 10 | Unknown | 已核验 |
| [**TheAdaply/jev-apply**](https://github.com/TheAdaply/jev-apply) | jev-apply：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 9 | MIT | 已核验 |
| [**valentynkit/jev-plays-pokemon-red**](https://github.com/valentynkit/jev-plays-pokemon-red) | 在 PyBoy 上玩 Pokemon Red：代码负责路线和算术，只在游戏真正分叉时让 Jev 从已合法的动作里选一个。 | — | 9 | MIT | 已核验 |
| [**QCJLchina/Jev-chat-assistant**](https://github.com/QCJLchina/Jev-chat-assistant) | Jev辅助判断的对话聊天助手 | — | 8 | MIT | 已核验 |
| [**valentynkit/jev.nvim**](https://github.com/valentynkit/jev.nvim) | Neovim 插件：用自然语言问当前 buffer，Treesitter 按函数切开，Jev 给每个函数打概率；全部命中按概率进入 quickfix。 | — | 8 | MIT | 已核验 |
| [**shimo4228/jev-skill-router**](https://github.com/shimo4228/jev-skill-router) | 这是一个 Claude Code 插件，每次收到提示就请 Jev 从已安装技能中挑选最多一个合适的技能，并默认以 shadow 模式只记录结果而不干预对话。 | — | 7 | MIT | 已核验 |
| [**valentynkit/jev-skip**](https://github.com/valentynkit/jev-skip) | Chrome 扩展：只读字幕，把片段交给 Jev 分类（段数或 Token 预算超限就拆请求），在进度条上画出五类片段，并对达到阈值的 sponsor、self_promo、intro、outro、recap 自动跳过。 | — | 7 | MIT | 已核验 |
| [**nssmd/jev-bot**](https://github.com/nssmd/jev-bot) | jev-bot：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 6 | MIT | 已核验 |
| [**Yaxin9Luo/spending-effort-with-jev**](https://github.com/Yaxin9Luo/spending-effort-with-jev) | spending-effort-with-jev：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 6 | MIT | 已核验 |
| [**DanielKillenberger/jev-predict-skill**](https://github.com/DanielKillenberger/jev-predict-skill) | 一个可供 Agent 执行的 skill 配方，根据规则和证据预测另一个 skill 的闭集结论。 | HTML | 4 | Unknown | [固定提交](https://github.com/DanielKillenberger/jev-predict-skill/blob/c80051db825de4a0af6efb03803e682daa466996/SKILL.md) |
| [**DataGobes/jev-demos**](https://github.com/DataGobes/jev-demos) | jev-demos：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 4 | MIT | 已核验 |
| [**harrymunro/jev-laya-benchmark**](https://github.com/harrymunro/jev-laya-benchmark) | jev-laya-benchmark：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 4 | MIT | 已核验 |
| [**Tongyun1/Jev-in-the-Loop**](https://github.com/Tongyun1/Jev-in-the-Loop) | **Jev-in-the-Loop 致力于研究如何用 Jev 加速各类需要 LLM 做决策的任务。** 从选择下一步操作，到推进一段工作流，我们探索把 Jev 引入决策循环，让智能体从理解意图更快地走向完成任务。 | — | 4 | MIT | 已核验 |
| [**455-dIAO/jev-codex-router-skill**](https://github.com/455-dIAO/jev-codex-router-skill) | 按任务需求选择 **模型 × 推理强度**，把路由流程装进一个可分享的 Codex Skill。 | — | 3 | Unknown | 已核验 |
| [**davertor/jev-slop-guard**](https://github.com/davertor/jev-slop-guard) | jev-slop-guard：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 3 | MIT | 已核验 |
| [**noetion/dsh-jev**](https://github.com/noetion/dsh-jev) | dsh-jev：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 3 | MIT | 已核验 |
| [**Oranquelui/astra-jev-harness**](https://github.com/Oranquelui/astra-jev-harness) | astra-jev-harness：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 3 | MIT | 已核验 |
| [**pandore/jev-chat-gate**](https://github.com/pandore/jev-chat-gate) | jev-chat-gate：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 3 | MIT | 已核验 |
| [**statico/jev-nethack**](https://github.com/statico/jev-nethack) | jev-nethack：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 3 | MIT | 已核验 |
| [**ZJemYoung/jev-chat-windows-laya**](https://github.com/ZJemYoung/jev-chat-windows-laya) | Windows 版微信聊天副驾（上游 fork）：本地 laya 判断引擎免密钥运行 + 修复高缩放屏抓取错位 Windows fork of jev-chat: key-free local laya judge + DPI-aware screen capture fix | — | 3 | MIT | 已核验 |
| [**coasty-ai/JevCode**](https://github.com/coasty-ai/JevCode) | JevCode：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 2 | MIT | 已核验 |
| [**AppChainAI/Jevatar**](https://github.com/AppChainAI/Jevatar) | 密钥只存在于服务端，不下发到浏览器。 | — | 1 | MIT | 已核验 |
| [**ccai40359-wq/jev-triage**](https://github.com/ccai40359-wq/jev-triage) | jev-triage：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 1 | MIT | 已核验 |
| [**DansiDanutz/fake-real-jev**](https://github.com/DansiDanutz/fake-real-jev) | fake-real-jev：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 1 | MIT | 已核验 |
| [**dtheofr/typesafe-jev-ruby**](https://github.com/dtheofr/typesafe-jev-ruby) | typesafe-jev-ruby：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 1 | MIT | 已核验 |
| [**harsha89/jev-demo**](https://github.com/harsha89/jev-demo) | jev-demo：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 1 | Unknown | 已核验 |
| [**kt3k/jevchat**](https://github.com/kt3k/jevchat) | 一个聊天式 Jev 演示：回答从预先定义或自定义的选项里选择，而不是生成长文。 | JavaScript | 1 | Unknown | [固定提交](https://github.com/kt3k/jevchat/blob/18ecea877ebcdaa66b0d2eba9a4db87f0b9715ab/main.ts) |
| [**Little-Planet-Labs/jev-playground**](https://github.com/Little-Planet-Labs/jev-playground) | 在网页里输入状态与选择题或评分题，查看 Jev 的回答和概率分布。 | TypeScript | 1 | Unknown | [固定提交](https://github.com/Little-Planet-Labs/jev-playground/blob/418b723779569b1cb1f21a4f7f34c546d44c7e34/src/app/api/evaluate/route.ts) |
| [**russfranky/jev-crawlers**](https://github.com/russfranky/jev-crawlers) | jev-crawlers：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 1 | MIT | 已核验 |
| [**sable-inc/jev-linter-action**](https://github.com/sable-inc/jev-linter-action) | jev-linter-action：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 1 | MIT | 已核验 |
| [**sedthh/xjevboost**](https://github.com/sedthh/xjevboost) | xjevboost：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 1 | Apache-2.0 | 已核验 |
| [**X0EF/jev_projects**](https://github.com/X0EF/jev_projects) | jev_projects：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 1 | MIT | 已核验 |
| [**bugkiwi/turing-jail**](https://github.com/bugkiwi/turing-jail) | 由 TypeSafe Jev System One 驱动的三关 AI 审讯游戏：通过求情、逻辑与悖论测试，争取获得释放。 | TypeScript | 0 | Unknown | [固定提交](https://github.com/bugkiwi/turing-jail/blob/629ff1b5617800d851811ce4379845f5ac59f729/server.ts#L91-L123) |
| [**iamjonatha/jev-book-tags**](https://github.com/iamjonatha/jev-book-tags) | jev-book-tags：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 0 | Unknown | 已核验 |
| [**patryckalves/jev-no-enem**](https://github.com/patryckalves/jev-no-enem) | jev-no-enem：把任务状态交给 Jev，返回供本地程序使用的结构化判断；具体策略请查看来源。 | — | 0 | Unknown | 已核验 |

## Domain & Vertical Tools

| 项目 | 简介 | 语言 | ⭐ | 许可证 | 证据 |
|---|---|---:|---:|---:|---|
| [**virattt/ai-hedge-fund**](https://github.com/virattt/ai-hedge-fund) | 一个教育用途的 AI 对冲基金原型，其中可选 Jev 适配器把结构化判断接到基金决策流程。 | Python | 63832 | MIT | [固定提交](https://github.com/virattt/ai-hedge-fund/blob/154a8b2f46dca0f40764d814e4e747b0ad71f4c4/hedge_fund/llm/client.py) |
| [**jarrodwatts/jev-trader**](https://github.com/jarrodwatts/jev-trader) | 在 Monad 的 Kuru MON-USDC 订单簿上尝试做市，Jev 可按新区块选择买卖方向。 | TypeScript | 2745 | MIT | [固定提交](https://github.com/jarrodwatts/jev-trader/blob/b587759e459ea049590102e54a0b07800864cdc3/src/model.ts) |
| [**jev-chat/jev-chat-windows**](https://github.com/jev-chat/jev-chat-windows) | 微信（Windows 4.x）旁挂的回复辅助：窗口截图 + 本地离线 OCR 读对方消息 → Jev 判断意图 → 3 条候选一键填入，发送永远手动 | — | 720 | Unknown | 已核验 |
| [**kyotofin/tax-doc-classifier**](https://github.com/kyotofin/tax-doc-classifier) | 税务文档页面分类器，用 Jev 从预先定义的 IRS 表格与页面类型中选择类别。 | TypeScript | 489 | Apache-2.0 | [固定提交](https://github.com/kyotofin/tax-doc-classifier/blob/6afcf701395466d7c936ec8178daf017b9d96b0c/src/backend.ts) |
| [**AgriciDaniel/jev-seo**](https://github.com/AgriciDaniel/jev-seo) | 从一个首页网址对任意网站做实时SEO审计，抓取网站并结合52条规则与Jev判断打分，生成PDF、XLSX和Markdown三份报告。 | — | 479 | MIT | 已核验 |
| [**aowang-ai/jev-trade**](https://github.com/aowang-ai/jev-trade) | 一个 Hyperliquid 交易机器人实验，用 Jev 判断做多、做空，以及开仓、平仓或等待。 | TypeScript | 179 | Unknown | [固定提交](https://github.com/aowang-ai/jev-trade/blob/df2c9656324a8a75996eb0612de7adcfe3ce6f89/src/model.ts) |
| [**Liyucheng1997/332_lab-jev-chat**](https://github.com/Liyucheng1997/332_lab-jev-chat) | Jev Chat Assistant for Windows - 电脑版微信意图判断与 DeepSeek 建议回复 | — | 164 | MIT | 已核验 |
| [**socai-io/jev-social**](https://github.com/socai-io/jev-social) | 该项目由 Jev 逐步选择 Instagram、TikTok 和 LinkedIn 的搜索、打开主页或帖子、读取评论及下载视频等操作，并由 socai 在真实浏览器中执行后整理成带引用的报告。 | — | 140 | MIT | 已核验 |
| [**irfndi/prism-liquidity-agent**](https://github.com/irfndi/prism-liquidity-agent) | 观察 Solana 流动性池的 Agent，Jev 提供影子判断与规则结果对照。 | TypeScript | 116 | MIT | [固定提交](https://github.com/irfndi/prism-liquidity-agent/blob/22c67bdbe30bab608226832256a5013ad826b707/engine/jev-service.ts) |
| [**vinilana/jev-eval-agent**](https://github.com/vinilana/jev-eval-agent) | 智能体工具选择基准测试平台，在包含 100 个模拟工具的个人助理环境下对比大模型直接选工具与 Jev 路由的效率。 | HTML | 106 | Unknown | [固定提交](https://github.com/vinilana/jev-eval-agent/blob/037de1120c84b4b63cdf748e2acf258ff66d7731/agent/lib/jev-router.ts#L1-L154) |
| [**AkashPriyadarshii/jev-seo**](https://github.com/AkashPriyadarshii/jev-seo) | Rust SEO/GEO 命令行与 MCP 实验工具，结合网页检查、DuckDuckGo 查询和可选 Jev 评分。 | Rust | 92 | MIT | [固定提交](https://github.com/AkashPriyadarshii/jev-seo/blob/bbd59fe994d557e12f31d3548a012e0f02db64d9/src/engine.rs#L28) |
| [**codegirl-007/jevlint**](https://github.com/codegirl-007/jevlint) | jevlint：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 92 | MIT | 已核验 |
| [**AustinAWay/Working-Memory-Jev**](https://github.com/AustinAWay/Working-Memory-Jev) | 这是一个在本地运行的教学辅助工具，它使用 Jev API 分析英语教学文本在各阅读步骤中的主动分组、来源连接和需求变化，并与1–5槽位预算进行比较。 | — | 76 | Unknown | 已核验 |
| [**AboveColin/HA-Jev**](https://github.com/AboveColin/HA-Jev) | 把 Jev 的判断变成 Home Assistant 传感器，例如检查衣服是否洗完后一直没取。 | Python | 69 | MIT | [固定提交](https://github.com/AboveColin/HA-Jev/blob/1b48f2fa1e94d076b54082f889f04b0083bcd1a8/custom_components/jev/coordinator.py) |
| [**Nisaka520/JevIntent**](https://github.com/Nisaka520/JevIntent) | 微信（FkWeChat 插件）：长按消息分析意图 / 情绪 / 回复姿态，只在本机弹提示，对方无感知 | — | 63 | MIT | 已核验 |
| [**tomerglick57/Jevstiller**](https://github.com/tomerglick57/Jevstiller) | Jevstiller：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 57 | Apache-2.0 | 已核验 |
| [**hqman/JevScout**](https://github.com/hqman/JevScout) | 供编程 Agent 调用的求职检索演示 Skill，通过 Chrome 浏览公司招聘页，用 Jev 筛选 AI 与软件工程职位并保存结果。 | Python | 39 | Unknown | [固定提交](https://github.com/hqman/JevScout/blob/b51390be0c3ca28b5407ab6d8c8044912a03bb31/jev_job_hunter/jev.py#L246-L273) |
| [**zadescoxp/Jev-Trades**](https://github.com/zadescoxp/Jev-Trades) | 用实时加密货币行情练习模拟交易。Jev 给出交易判断，面板展示虚拟仓位和技术指标，不连真实下单接口。 | Python | 39 | Apache-2.0 | [固定提交](https://github.com/zadescoxp/Jev-Trades/blob/01fb18e4484d626f03345eaff2b93b641677b786/pipeline/paper_trader.py) |
| [**choxos/jev-reviewer**](https://github.com/choxos/jev-reviewer) | 为系统综述从论文与补充材料中挑出原文证据，供研究者逐条核对并导出提取表。 | JavaScript | 37 | MIT | [固定提交](https://github.com/choxos/jev-reviewer/blob/b00d05fc888973b0147383dd7315318280d01635/server.js) |
| [**bytelabs-oss/clash-jev**](https://github.com/bytelabs-oss/clash-jev) | clash-jev：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 35 | MIT | 已核验 |
| [**Eliot5566/JEV-Paper-Radar**](https://github.com/Eliot5566/JEV-Paper-Radar) | 该项目每天早上用 Jev 根据用户以自然语言描述的兴趣为 arXiv 新论文评分，并把入选论文生成网页和 RSS 呈现出来。 | — | 27 | MIT | 已核验 |
| [**liaoyuhua/jev-trip**](https://github.com/liaoyuhua/jev-trip) | Jev Trip 是一个可解释的单日行程规划器，由 LLM 提出活动草案并由 Jev 筛选候选以及核对交通与行程。 | — | 26 | MIT | 已核验 |
| [**stas4000/jev-linkmap**](https://github.com/stas4000/jev-linkmap) | 该项目抓取网站内容并生成候选内部链接，由 Jev 判断是否值得链接及选择原文中的锚文本，并支持用深模型复核分歧来改写 rubric。 | — | 22 | Unknown | 已核验 |
| [**TypeSafeAI/typesafe-playground**](https://github.com/TypeSafeAI/typesafe-playground) | TypeSafe AI Jev 社区试验场，内置 110 个分类、对话路由、提取与决策实验用例，支持移动端交互与 A/B 对比。 | TypeScript | 21 | MIT | [固定提交](https://github.com/BunsDev/typesafe-ai-playground/blob/f67c3571fca1c468b4585f17282a58a1f57b1a17/app/api/run/route.ts#L1-L65) |
| [**grandamenium/jev-anything**](https://github.com/grandamenium/jev-anything) | jev-anything：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 18 | MIT | 已核验 |
| [**kenhuangus/jev-usecases**](https://github.com/kenhuangus/jev-usecases) | jev-usecases：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 18 | MIT | 已核验 |
| [**Ice-Hazymoon/jevlint**](https://github.com/Ice-Hazymoon/jevlint) | jevlint：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 15 | MIT | 已核验 |
| [**Nisaka520/JevBystander**](https://github.com/Nisaka520/JevBystander) | 安卓无障碍版微信判读：只读屏、只弹 3 条 Toast（意图 / 情绪 / 着急 / 建议），不生成回复文案、不发送 · 零第三方依赖，APK 861 KB | — | 15 | MIT | 已核验 |
| [**sunil-sadasivan/jevernetes**](https://github.com/sunil-sadasivan/jevernetes) | Jevernetes 在终端和本地仪表盘中实时采集 Kubernetes 日志，支持用 Jev 做语义搜索和分析、查看上下文，并把选中的日志证据整理后交给 coding Agent。 | — | 14 | MIT | 已核验 |
| [**bl888m/jev-bot**](https://github.com/bl888m/jev-bot) | 该项目把股票、加密货币和迷因币的市场状态输入 Jev，输出 BUY/SELL/HOLD/AVOID 决策并默认用纸面交易执行。 | — | 11 | Unknown | 已核验 |
| [**dagfinndybvig/Jev_Ontology**](https://github.com/dagfinndybvig/Jev_Ontology) | 该项目用 LLM 编写本体，用 Jev 对客服工单和图书馆图像按本体分类，并用 Jev 的分类结果反馈修订本体。 | — | 11 | Unknown | 已核验 |
| [**romiluz13/jevmory**](https://github.com/romiluz13/jevmory) | jevmory：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 11 | MIT | 已核验 |
| [**kuhung/ask-jev**](https://github.com/kuhung/ask-jev) | 面向中国大陆年轻人的复古新野蛮主义 (Neo-Brutalism) 生活微决策老管家。专治“买不买”、“花不花”、“用不用”、“中午吃什么”、“去不去”等内耗纠结，直截了当给结论。 | — | 10 | Unknown | 已核验 |
| [**darwintechlab/openjev**](https://github.com/darwintechlab/openjev) | openjev：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 9 | MIT | 已核验 |
| [**ItisNoMatter/kojev**](https://github.com/ItisNoMatter/kojev) | kojev：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 9 | MIT | 已核验 |
| [**poiuyjie/jev_project_context**](https://github.com/poiuyjie/jev_project_context) | 科研项目很少死于结果丢失——它们死于**上下文**丢失：那个数字是哪份配置跑出来的、为什么选这个基线、哪些结果已被作废、哪些只是假设。这个 skill 把 AI 智能体（Claude Code、ZCode 及任何兼容 skills 的智能体）变成一个守纪律的实验记录员：10 个操作、受控有效性词表、溯源门、只读审计。 | — | 9 | MIT | 已核验 |
| [**Parth1811/JevFlow**](https://github.com/Parth1811/JevFlow) | JevFlow：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 8 | MIT | 已核验 |
| [**joshhu/jevtest**](https://github.com/joshhu/jevtest) | 情緒測謊器：嘴上說「好」，心裡真的好嗎？用 TypeSafe Jev（System One 模型）透過 OpenRouter 即時判斷，並與一般 LLM 對照 | — | 7 | Unknown | 已核验 |
| [**choxos/jevchess**](https://github.com/choxos/jevchess) | 该项目是让Jev与OpenRouter大模型、Stockfish引擎或人类实时对弈、回放并统计战绩的单页国际象棋应用。 | — | 6 | MIT | 已核验 |
| [**ARCJ137442/jev-2048**](https://github.com/ARCJ137442/jev-2048) | An instrumented 2048 web lab where every move is a Jev (TypeSafe AI System One) Choice, with no heuristic fallback \| 用 Jev 决策模型驱动每一步的 2048 网页实验台，概率、置信度、延迟与成本全部摊开可见，且刻意不做启发式兜底 | — | 5 | MIT | 已核验 |
| [**Foadsf/jev-for-engineers**](https://github.com/Foadsf/jev-for-engineers) | 机械与电气工程的八组 Jev 小实验：分派设计任务、检查仿真日志、匹配零件，再由 Python 规则决定怎么处理。 | Python | 5 | MIT | [固定提交](https://github.com/Foadsf/jev-for-engineers/blob/181e75208ac3b982c80889267a28a1ed718452a9/jev.py) |
| [**lzq-0529/jev-span**](https://github.com/lzq-0529/jev-span) | Zero-shot named entity recognition on TypeSafe Jev. Define entity types in plain words — no training data, no GPU. 73.7 strict F1 across 12 Chinese/English NER benchmarks, with… | — | 5 | MIT | 已核验 |
| [**usail-hkust/JevLight**](https://github.com/usail-hkust/JevLight) | JevLight 是基于 CityFlow 的交通信号控制框架，为 Jev、Laya、规则控制器和强化学习基线提供统一运行器，进行结构化相位和绿灯时长决策。 | — | 5 | MIT | 已核验 |
| [**xhongc/jev-music-tag**](https://github.com/xhongc/jev-music-tag) | 利用 jev 刮削音乐元数据,风格,语言 | — | 5 | Unknown | 已核验 |
| [**Adkid-Zephyr/work-with-jev**](https://github.com/Adkid-Zephyr/work-with-jev) | **工作群消息太多？用 Jev 挑出需要你处理的事，整理成一份跨群待办。** | — | 4 | MIT | 已核验 |
| [**Cairn-ink/cairn-jev-lab**](https://github.com/Cairn-ink/cairn-jev-lab) | 這是一個實驗性的記憶收錄評估工具。輸入原文與候選記憶，Jev 評估證據，程式依據明確規則回傳「保存、略過、待定」。適合讓開發者在交給 agent 自動記憶之前，先測試自己的標準。 | — | 4 | MIT | 已核验 |
| [**daniel4x/JevEmon**](https://github.com/daniel4x/JevEmon) | JevEmon从宝可梦火红ROM内存读取地图与队伍状态，让Jev在可到达目的地中选择行走目标并指挥野生宝可梦对战，从主角家一路走到常青市。 | — | 4 | GPL-3.0 | 已核验 |
| [**grmkris/robo-harness**](https://github.com/grmkris/robo-harness) | SO-101 机械臂具身智能控制工作台：整合 Bun/Effect 与 Python 驱动，利用 Jev 做关节动作边界决策与预算控制。 | — | 4 | Unknown | 已核验 |
| [**matthew004-web/heyreach-jev-bot**](https://github.com/matthew004-web/heyreach-jev-bot) | 该项目使用 Jev 为 HeyReach 中的潜在客户和首条消息变体打分，为每位客户挑选最佳消息，并将结果写回为潜在客户名单和 DRAFT 营销活动。 | — | 4 | Unknown | 已核验 |
| [**RileyCarney/JevTools**](https://github.com/RileyCarney/JevTools) | JevTools：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 4 | GPL-3.0 | 已核验 |
| [**sahajamit/jev-lens**](https://github.com/sahajamit/jev-lens) | jev-lens：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 4 | MIT | 已核验 |
| [**yangyu666/dsh-jev-prune**](https://github.com/yangyu666/dsh-jev-prune) | dsh-jev-prune：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 4 | MIT | 已核验 |
| [**AstonyCat/jev-tab-grouper**](https://github.com/AstonyCat/jev-tab-grouper) | **不会真的有人手动整理 Chrome 标签页吧？** | — | 3 | MIT | 已核验 |
| [**Eric-Zhou-0302/jev-A-share-trader**](https://github.com/Eric-Zhou-0302/jev-A-share-trader) | **八个分析维度，一份可追溯的判断。** | — | 3 | MIT | 已核验 |
| [**EthanAlgoX/jev-trading**](https://github.com/EthanAlgoX/jev-trading) | 1. Keep **Demo** selected (`演示体验`). 2. Click **Try a decision** (`体验一次决策`). 3. Review the action, probabilities, and data quality on the right. 4. Open a record in **Recent anal… | — | 3 | Unknown | 已核验 |
| [**gaborishka/jev-wrapped**](https://github.com/gaborishka/jev-wrapped) | 输入公开 Telegram 频道名称即可生成卡片，展示过去十二个月帖子类型、广告、标题党和情绪施压的构成变化，每篇帖子由 Jev 单独判定。 | — | 3 | MIT | 已核验 |
| [**jevbook/jevscan**](https://github.com/jevbook/jevscan) | 读取 EVM Token 市场特征，输出关注或回避等风险判断，提供库、CLI 和 MCP 接口。 | JavaScript | 3 | MIT | [固定提交](https://github.com/jevbook/jevscan/blob/cdaf9b882cc6e221ceeaac2767fac82f584b9d88/src/engine.js) |
| [**jimmyliao/jev-storyboard-lab**](https://github.com/jimmyliao/jev-storyboard-lab) | jev-storyboard-lab：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 3 | MIT | 已核验 |
| [**juanlentino/jev-connector**](https://github.com/juanlentino/jev-connector) | jev-connector：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 3 | GPL-2.0 | 已核验 |
| [**mattn/sqlite3-jev**](https://github.com/mattn/sqlite3-jev) | 将 TypeSafe Jev 判断能力下沉为 SQLite 自定义 SQL 函数的 C 语言扩展：直接在 SQL 查询中实现语义打分与选择。 | — | 3 | MIT | 已核验 |
| [**mingleiw/jev-oncall**](https://github.com/mingleiw/jev-oncall) | jev-oncall：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 3 | MIT | 已核验 |
| [**morcoan/JevSeek**](https://github.com/morcoan/JevSeek) | 本地编码桌面与 CLI 智能体，将 Jev 的动作路由与 DeepSeek 的代码参数生成分层解耦协同。 | Python | 3 | MIT | [固定提交](https://github.com/morcoan/JevSeek/blob/030d59114a03720783e839481a7814e7aecaad85/desktop.py#L1-L141) |
| [**smithclay/dbt_jev**](https://github.com/smithclay/dbt_jev) | dbt_jev：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 3 | MIT | 已核验 |
| [**unownone/jevsume**](https://github.com/unownone/jevsume) | 给简历做一次结构化体检。既检查措辞、结构和机器可读性，也能对照具体职位描述，看这份简历是否匹配。 | TypeScript | 3 | Unknown | [固定提交](https://github.com/unownone/jevsume/blob/650a96a4c90da129cf745687d25abca36120c470/packages/jev/http.ts) |
| [**0xshikhar/jev-fuse**](https://github.com/0xshikhar/jev-fuse) | jev-fuse：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 2 | Apache-2.0 | 已核验 |
| [**darwintechlab/claude-jev**](https://github.com/darwintechlab/claude-jev) | claude-jev：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 2 | MIT | 已核验 |
| [**EmiRoberti77/jev-py-integration**](https://github.com/EmiRoberti77/jev-py-integration) | jev-py-integration：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 2 | Unknown | 已核验 |
| [**Fox-Islam/jevlint**](https://github.com/Fox-Islam/jevlint) | jevlint：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 2 | MIT | 已核验 |
| [**Kaos599/jev-writer**](https://github.com/Kaos599/jev-writer) | jev-writer：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 2 | MIT | 已核验 |
| [**Kunyanli230/jev-clean**](https://github.com/Kunyanli230/jev-clean) | jev-clean：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 2 | MIT | 已核验 |
| [**LouisUltra/jev-deep-dive**](https://github.com/LouisUltra/jev-deep-dive) | jev-deep-dive：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 2 | CC-BY-4.0 | 已核验 |
| [**mychaelangelo/tempo-jev-demo**](https://github.com/mychaelangelo/tempo-jev-demo) | 一个本地自然语言任务工作区，可将用户请求转为看板、表格、日历等视图与任务变更，并对比不同模型的表现。 | — | 2 | MIT | 已核验 |
| [**satiricalguru/Hinge-Jev**](https://github.com/satiricalguru/Hinge-Jev) | Hinge-Jev：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 2 | MIT | 已核验 |
| [**snjrusmn/jev-humanizer**](https://github.com/snjrusmn/jev-humanizer) | jev-humanizer：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 2 | MIT | 已核验 |
| [**stas4000/jev-geo-audit**](https://github.com/stas4000/jev-geo-audit) | 该项目批量抓取300个公开页面并用Jev打分其被AI引用的可能性，同时用大模型法官对比一致性、成本与延迟。 | — | 2 | MIT | 已核验 |
| [**0xZee/jev-stock-decision-maker**](https://github.com/0xZee/jev-stock-decision-maker) | jev-stock-decision-maker：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 1 | Unknown | 已核验 |
| [**Alpha-Harper-Franklin/jev-drive**](https://github.com/Alpha-Harper-Franklin/jev-drive) | 已实现真实 Jev API 接入、真实 RGB 的视觉推理与对照、过期响应检查、数据分组和指标工具。首轮完成 27 张录制图像的诊断实验，但尚无驾驶结果标签，也未完成 CARLA/BeamNG 闭环实验。首轮结果说明：生成视觉描述的成本不可忽略，不能把 Jev 接口便宜直接等同于整个驾驶系统更快。 | — | 1 | MIT | 已核验 |
| [**Charlie-Wang-03/jev-testbench**](https://github.com/Charlie-Wang-03/jev-testbench) | `jev-testbench` 是一个基于 Agentic Engineering 搭建的 Jev 模型简易实验台。 | — | 1 | MIT | 已核验 |
| [**clduab11/jev-test**](https://github.com/clduab11/jev-test) | jev-test：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 1 | MIT | 已核验 |
| [**CMaintz/jev-triage**](https://github.com/CMaintz/jev-triage) | jev-triage：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 1 | MIT | 已核验 |
| [**dabaicai001/jeves-desk**](https://github.com/dabaicai001/jeves-desk) | 通用客服平台:ChatKit UI + Jev 决策 + Qwen 生成 + RAG 知识库 + 插件化 Tools + MCP 数据面,换行业只改 YAML 不改代码 | — | 1 | Unknown | 已核验 |
| [**darthblanc/tictacjev**](https://github.com/darthblanc/tictacjev) | 这是一个人类与 Jev 对弈的井字棋应用，Jev 每一步选择的格子及其置信度和候选格概率都会显示在走棋记录中。 | — | 1 | Unknown | 已核验 |
| [**gabazureus/jevextract**](https://github.com/gabazureus/jevextract) | jevextract：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 1 | MIT | 已核验 |
| [**havietkok-sys/BizzJev**](https://github.com/havietkok-sys/BizzJev) | BizzJev：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 1 | Unknown | 已核验 |
| [**hemanth/tc39-atlas**](https://github.com/hemanth/tc39-atlas) | 该项目是交互式 TC39 提案语义浏览工具，使用 Jev 按采用路径、认知负担、Web 兼容风险和意图原型对 ECMAScript 提案进行分类展示。 | — | 1 | Unknown | 已核验 |
| [**j341nono/jev-prompt-optimization**](https://github.com/j341nono/jev-prompt-optimization) | 该工具使用带标注数据集，通过 EvoPrompt 或 GEPA 自动优化 TypeSafe Jev Choice 的 instructions 和各 criteria 描述。 | — | 1 | MIT | 已核验 |
| [**nanami-0713/jev-resume-screening**](https://github.com/nanami-0713/jev-resume-screening) | TypeSafe Jev (System One) 简历-JD 匹配度初筛：判据模板 + 正/负/陷阱三类样本测试档案，判据 v1→v3 迭代全程可复现 / Resume-JD screening with TypeSafe Jev: atomic questions, calibrated criteria v1→v3, full reproduci… | — | 1 | Unknown | 已核验 |
| [**Patrick-SCH03/jev-issue-radar**](https://github.com/Patrick-SCH03/jev-issue-radar) | Jev Issue Radar 是一个只读的 GitHub 重复问题分类看板，它检索候选问题并用 Jev 的 Choice 将每对问题判为重复、相关、不同或信息不足，同时并排展示双方原始报告中的选中段落供维护者审查。 | — | 1 | MIT | 已核验 |
| [**saimahmedqazi/typesafe-jev-playground**](https://github.com/saimahmedqazi/typesafe-jev-playground) | typesafe-jev-playground：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 1 | Unknown | 已核验 |
| [**sumitrevolt/leadgenrationaivoiceagent**](https://github.com/sumitrevolt/leadgenrationaivoiceagent) | 营销与语音平台中的 TypeSafe 实验模块，用 Jev 为预设 Agent 角色选择专长标签。 | Python | 1 | MIT | [固定提交](https://github.com/sumitrevolt/leadgenrationaivoiceagent/blob/0ed2da0ea032eb077a196798d1ed5e6aa8602a2b/app/platform/agent_talent_pool.py#L59) |
| [**TimMikeladze/JevLang**](https://github.com/TimMikeladze/JevLang) | JevLang：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 1 | MIT | 已核验 |
| [**viniciusfinger/jev-intent-classification**](https://github.com/viniciusfinger/jev-intent-classification) | jev-intent-classification：评估业务状态，给出供本地规则参考的分类或风险分数。 | — | 1 | Unknown | 已核验 |
| [**Waxmell114514/jev-trade**](https://github.com/Waxmell114514/jev-trade) | 把 BTC、ETH 的行情变成文字状态，让 Jev 给交易判断，再放进含延迟和费用的模拟撮合里观察。 | Python | 1 | Unknown | [固定提交](https://github.com/Waxmell114514/jev-trade/blob/df43b9636e34096f83457fe58bfe3f038879614c/jevtrade/jev/client.py) |
| [**Zafer-Liu/jev-xiangqi**](https://github.com/Zafer-Liu/jev-xiangqi) | 跟 Jev 下中国象棋。AI 的每一手都来自一次 `system_one()` 调用里的 Score 0-4 扇出评估——没有 minimax、没有子力价值表，纯靠 Jev 读局面。 | — | 1 | BSD-2-Clause | 已核验 |
| [**jaygajera17/JevPulse**](https://github.com/jaygajera17/JevPulse) | 该项目批量分析 YouTube 视频评论并生成观众共识与证据报告。 | — | 0 | Unknown | 已核验 |
| [**ngocvychu38-web/cube-lab**](https://github.com/ngocvychu38-web/cube-lab) | 完整开发复盘与技术说明：[实现过程与原理](docs/实现过程与原理.md)，包括需求演进、状态模型、七步搜索算法、Jev协议、动画、音效、计时、本地存储、发布记录与验证边界。 | — | 0 | Unknown | 已核验 |
| [**pc418/jev-calculator**](https://github.com/pc418/jev-calculator) | 这是一个由 Jev 逐字选择答案字符并展示每步概率分布的计算器。 | — | 0 | MIT | 已核验 |

## Evaluation & Observability

| 项目 | 简介 | 语言 | ⭐ | 许可证 | 证据 |
|---|---|---:|---:|---:|---|
| [**latitude-dev/latitude-llm**](https://github.com/latitude-dev/latitude-llm) | Latitude 的可选 Jev 预分类器为对话检查打分，并记录检查选择的依据。 | — | 4700 | MIT | [固定提交](https://github.com/latitude-dev/latitude-llm/blob/6b2484c1d74973877fc7d353b8867c7496568d78/packages/domain/flaggers/src/use-cases/run-jev-preclassifier.ts#L1) |
| [**NiazMorshed2007/jev-review**](https://github.com/NiazMorshed2007/jev-review) | 供编码 Agent 使用的本地 MCP 代码质量检查器，返回多个维度的结构化评分。 | TypeScript | 230 | MIT | [固定提交](https://github.com/NiazMorshed2007/jev-review/blob/57690af54ef7d862c2483342c1e61c14dffcf727/src/jev/client.ts) |
| [**supercorp-ai/supercov**](https://github.com/supercorp-ai/supercov) | 编程 Agent 的代码质量与覆盖率 CLI：Jev 检查源码属性，本地覆盖率工具帮助选择补测目标。 | — | 143 | MIT | [固定提交](https://github.com/supercorp-ai/supercov/blob/55f5ce93a239829c224b89e6749991310be91ea4/crates/supercov-cli/src/quality.rs#L30) |
| [**ldbumble/taskuary**](https://github.com/ldbumble/taskuary) | Taskuary 的可选 Jev 判断模块，对任务运行状态检查用户定义的条件。 | Python | 135 | MIT | [固定提交](https://github.com/ldbumble/taskuary/blob/4ad29d7b292a7899767338cfcc83b2dde8f43330/taskuary/jev.py) |
| [**qkal/Canny**](https://github.com/qkal/Canny) | 为 Claude Code 与 Codex CLI 记录执行账本，检查改动后是否有通过的验证。 | TypeScript | 105 | MIT | [固定提交](https://github.com/qkal/Canny/blob/74bc3487370ae6d61cef69c5642cce504a8579cb/src/jev.ts) |
| [**mizchi/jev-playground**](https://github.com/mizchi/jev-playground) | MoonBit 与 TypeScript 的 Jev 实验集，覆盖棋类、浏览器、命令风险和小型语言。 | TypeScript | 72 | Unknown | [固定提交](https://github.com/mizchi/jev-playground/blob/92701bb053ffcec7bb77f23f26b6b1b01ad83f8b/lib/client.mbt) |
| [**alp82/goodwatch-monorepo**](https://github.com/alp82/goodwatch-monorepo) | GoodWatch 仓库内的影视特征评分实验，比较 Jev 对情绪、情节等特征的不同问法和批量方式。 | Python | 39 | MIT | [固定提交](https://github.com/alp82/goodwatch-monorepo/blob/58aa7b3683f82ee4ea58f7da1007ee76400a7115/goodwatch-flows/windmill/f/dna/prototype_comparison/jev_run.py) |
| [**iammrduncan/typesafe-ai-benchmark**](https://github.com/iammrduncan/typesafe-ai-benchmark) | 在共同的应用任务上对照 Jev 与其他结构化输出模型，记录错误、延迟、Token 与估算成本。 | TypeScript | 38 | MIT | [固定提交](https://github.com/iammrduncan/typesafe-ai-benchmark/blob/cf348cd291bb538ad9fa902334649ef5dd937e92/packages/demos/lib/jev.ts) |
| [**AbdelStark/jev-benchmarks**](https://github.com/AbdelStark/jev-benchmarks) | 把 Jev 和 GLiNER 放到同一批分类题上，除了答对率，也检查概率靠不靠谱。 | Python | 22 | Apache-2.0 | [固定提交](https://github.com/AbdelStark/jev-benchmarks/blob/0d610cc53e79bcbec691312b0c4adb4a0e371642/src/jev_benchmarks/adapters/jev.py) |
| [**kavehmz/typesafe-playground**](https://github.com/kavehmz/typesafe-playground) | 可交互的 Jev 实验集，展示客服工单分流预览和三维驾驶仿真。 | JavaScript | 13 | Unknown | [固定提交](https://github.com/kavehmz/typesafe-playground/blob/ec6102ef693de3c1775af5c844d48713b6d3f4a2/demo01/server.mjs#L67) |
| [**abhixhek/jevcal**](https://github.com/abhixhek/jevcal) | 用自己的标注数据评估 Jev 概率、选择置信度阈值，并检查模型更新后的变化。 | Python | 10 | MIT | [固定提交](https://github.com/abhixhek/jevcal/blob/ae8f3144d69c9cb0e5e0a2c17f70b9d14714cb9f/src/jevcal/providers/typesafe.py) |
| [**doeixd/jev-pref**](https://github.com/doeixd/jev-pref) | 把 AGENTS.md 中的项目偏好整理为规则，再用 Jev 检查 hunk、暂存文件或 PR。 | JavaScript | 10 | MIT | [固定提交](https://github.com/doeixd/jev-pref/blob/9d77ea6069123a0b3eedf465ec39781842722b0a/packages/jev-pref/src/jev.js) |
| [**anessbelbati/jev-rerank-bench**](https://github.com/anessbelbati/jev-rerank-bench) | 比较 Jev、专用 reranker 和聊天模型对同一批搜索片段的排序结果。 | — | 9 | MIT | [固定提交](https://github.com/anessbelbati/jev-rerank-bench/blob/cd9a35b22aeb4187334f7018a0ee1960a7470586/rerankers/jev.py#L28) |
| [**wondertwins/jev-benchmark**](https://github.com/wondertwins/jev-benchmark) | 通过国际象棋和游戏 NPC 对话对象识别，测试 Jev 的选择与判断边界。 | — | 6 | MIT | [固定提交](https://github.com/wondertwins/jev-benchmark/blob/1c2509ac7d5508b8a7ce00ae4df6d7652d05de8b/jevcommon/client.py#L82) |
| [**y0usaf/jev-lm**](https://github.com/y0usaf/jev-lm) | 把下一个词当选择题，试着用 Jev 拼出句子；也能让它挑选本地草拟的整段续写。 | TypeScript | 6 | MIT | [固定提交](https://github.com/y0usaf/jev-lm/blob/05e7f03bf447073a0bed3255d4de154f953e533d/python/jev_lm/api.py) |
| [**Nainish-Rai/jev-frontend-qa**](https://github.com/Nainish-Rai/jev-frontend-qa) | 用 Jev 选择浏览器操作，再通过 DOM、HTTP 和数据库状态检查前端功能是否符合约定。 | Python | 5 | MIT | [固定提交](https://github.com/Nainish-Rai/jev-frontend-qa/blob/2a57d0a23471ca627a2840eff04102ddc844dd57/src/jev_frontend_qa/core/model_client.py) |
| [**adhyaay-karnwal/jev-chat**](https://github.com/adhyaay-karnwal/jev-chat) | 实验性聊天解码器：让 Jev 反复选择词或短语，由代码把它们拼成回答。 | — | 4 | MIT | [固定提交](https://github.com/adhyaay-karnwal/jev-chat/blob/fb92fd33ddd6603aa544fe4988dd8e918f91d6ca/src/jevchat/client.py#L40) |
| [**RINNECODER/jev-behavior-study**](https://github.com/RINNECODER/jev-behavior-study) | 针对 Jev 1.13.0 的独立行为研究，记录不同问题表述、输入条件及游戏任务下的成功与失败。 | Python | 3 | MIT | [固定提交](https://github.com/RINNECODER/jev-behavior-study/blob/e4a1d7ec691a91f33d3b5879a780e6f27328f173/behavior_study.py) |
| [**SamuelSacco/jev-exploration**](https://github.com/SamuelSacco/jev-exploration) | 记录 Jev 能力与限制的研究仓库，包含主张审查、概率校准实验和可运行示例。 | Python | 3 | MIT | [固定提交](https://github.com/SamuelSacco/jev-exploration/blob/af91a6e09bf82c7f43d142de2bf5f1573d89b1b9/jevlab/client.py) |
| [**TokenTrim/jev-agent-failure-benchmark**](https://github.com/TokenTrim/jev-agent-failure-benchmark) | 用 Jev 分析多 Agent 失败记录的评测项目，预测责任 Agent、关键步骤和错误类型。 | Python | 3 | Apache-2.0 | [固定提交](https://github.com/TokenTrim/jev-agent-failure-benchmark/blob/4d46af795a4a4409940a65857da73e45abaea2db/src/jevbench/backends/jev.py) |
| [**XieChengYuan/jev-gomoku**](https://github.com/XieChengYuan/jev-gomoku) | 弈瞬：同时运行九盘 15×15 五子棋，让两位 Jev 玩家比较不同输入信息，并逐手检查请求与返回。 | JavaScript | 3 | Unknown | [固定提交](https://github.com/XieChengYuan/jev-gomoku/blob/2aac72cd54ab63fd35e7d29e65def787dda2b333/src/online.js) |
| [**PistachioAIHQ/jev-synergy-screening**](https://github.com/PistachioAIHQ/jev-synergy-screening) | 用 Jev 筛选 ADHD 综述的论文标题和摘要，并与 Cohen Abstract Triage 标注比较。 | Python | 2 | Unknown | [固定提交](https://github.com/PistachioAIHQ/jev-synergy-screening/blob/4142c88513b68520958cee1fa72ed59385f91376/src/jev_client.py) |
| [**poponline63/hermes-jev-north-star**](https://github.com/poponline63/hermes-jev-north-star) | Hermes 的目标验收 skill，保存要求、生成运行提示词，并检查证据是否满足要求。 | Python | 2 | MIT | [固定提交](https://github.com/poponline63/hermes-jev-north-star/blob/b5499f2da6b940258e2dc7c935552a217c7df993/scripts/jev_judge.py) |
| [**4esv/jev-eval**](https://github.com/4esv/jev-eval) | 在有标签的分类任务上比较 Jev 与 OpenRouter 模型的准确率、校准、时延和成本。 | Python | 1 | Unknown | [固定提交](https://github.com/4esv/jev-eval/blob/dcfd6db29dfee2a107ff6e018176c6577002f887/evaljev/runners.py#L15) |
| [**omni-/ask-jev**](https://github.com/omni-/ask-jev) | Windows PowerShell 工具，在 Codex 中用 :jev 审视会话里已记录的执行证据。 | PowerShell | 1 | MIT | [固定提交](https://github.com/omni-/ask-jev/blob/74199ef94098f4e79e5251ffc5a770cda17e2be3/lib/Jev.psm1) |
| [**TheBous/jev-flash-review**](https://github.com/TheBous/jev-flash-review) | 供编码 Agent 调用的 MCP 代码审查引擎，对提交的 diff 按规则给出结构化判断。 | TypeScript | 1 | Unknown | [固定提交](https://github.com/TheBous/jev-flash-review/blob/658a7bd52e30292daa21ca3941179429634371eb/src/judge.ts) |
| [**Bud-ro/jev-demos**](https://github.com/Bud-ro/jev-demos) | 用迷宫测试 Jev 的空间判断，比较单步选择和一次预测多步的表现。 | — | 0 | Unknown | [固定提交](https://github.com/Bud-ro/jev-demos/blob/37470f96bc4cb91c5f10703caa7460bf0c20f23a/packages/jev_common/lib/src/client.dart#L232) |
| [**jujumilk3/jev-calibration-audit**](https://github.com/jujumilk3/jev-calibration-audit) | 通过公开 API 和数据测试 Jev 概率校准、选项措辞影响及韩文判断表现。 | Python | 0 | MIT | [固定提交](https://github.com/jujumilk3/jev-calibration-audit/blob/daab9e2c2d5d5683bf07f3482deb653c26856219/src/jev_audit/client.py#L12) |
| [**Shifty-Eye-Games/foreman-jev**](https://github.com/Shifty-Eye-Games/foreman-jev) | 给 Codex 工人配一个 Jev 监督员。它评估进展，但完成前还必须跑程序员指定的验收命令。 | Python | 0 | MIT | [固定提交](https://github.com/Shifty-Eye-Games/foreman-jev/blob/3cb97e6051cb5764c50d3a0155f4d1483934fb25/src/foreman/foreman/jev.py) |

## High-Frequency & Simulation

| 项目 | 简介 | 语言 | ⭐ | 许可证 | 证据 |
|---|---|---:|---:|---:|---|
| [**jaredpalmer/kev**](https://github.com/jaredpalmer/kev) | 基于 Qwen2.5-0.5B 构建的轻量级类 Jev 决策头与适配器，支持在 MacBook 本地训练、微调与端到端运行。 | Python | 8314 | Apache-2.0 | [固定提交](https://github.com/jaredpalmer/kev/blob/cc954f2f66d86943688fdbfa07b6db18f82ed065/kev/jev.py#L1-L122) |
| [**TianyuCodings/NanoJev**](https://github.com/TianyuCodings/NanoJev) | Jev 决策模型的纳米级复刻版本，支持并行决策输出、动态候选集与完整的端到端训练评估流水线。 | Python | 2473 | MIT | [固定提交](https://github.com/TianyuCodings/NanoJev/blob/71a513bb0163b5634467842b523ee0c0ed6fb1c7/scripts/evaluate_live_jev_navigation.py#L1-L70) |
| [**fhshaik/typesafe-mario**](https://github.com/fhshaik/typesafe-mario) | 从 NES 模拟器 RAM 和状态数据中提取环境，让 Jev 选择超级马力欧的手柄按键。 | Python | 425 | Unknown | [固定提交](https://github.com/fhshaik/typesafe-mario/blob/ca22449ed187118d19326d1f54b01b6636578aa4/src/typesafe_mario/policy.py) |
| [**RomanSlack/jev-drone**](https://github.com/RomanSlack/jev-drone) | MuJoCo 无人机仿真实验：从相机缓冲区提取场景，Jev 提供战术动作建议。 | Python | 234 | MIT | [固定提交](https://github.com/RomanSlack/jev-drone/blob/cbeb53ce4f17a06ea490ae43effcdad231143610/tactics.py#L184) |
| [**standardagents/jevpilot**](https://github.com/standardagents/jevpilot) | 在浏览器里开一辆小车，让 Jev 从提前算好的路线和速度里选下一步。 | JavaScript | 208 | Unknown | [固定提交](https://github.com/standardagents/jevpilot/blob/e1beeb13b9a928fb76f167f86af584f4ce9cf180/server/jev.js) |
| [**allebee/jevk5**](https://github.com/allebee/jevk5) | 该项目是一个开放决策模型，对给定状态返回 noul、choice 和 score 等类型化答案及其概率，并提供让 Jev 与该模型在相同棋盘和问题上直接对比的俄罗斯方块程序。 | — | 131 | Apache-2.0 | 已核验 |
| [**virajbhartiya/laya-vs-jev**](https://github.com/virajbhartiya/laya-vs-jev) | **在 Apple Silicon 上本地运行开放权重的结构化决策模型。** | — | 110 | Apache-2.0 | 已核验 |
| [**Dimweaker/jev-libero**](https://github.com/Dimweaker/jev-libero) | 在 LIBERO 仿真环境中，使用 Jev 分层选择机器人原子动作，结合可逆物理前视完成操作任务。支持 JSON 任务配置，并提供关闭微波炉、关闭抽屉的演示与完整运行记录。 | — | 80 | MIT | 已核验 |
| [**lykycy123/RoboJEV**](https://github.com/lykycy123/RoboJEV) | **在 MuJoCo 中，通过两阶段 JEV 控制 Franka Panda 完成三种操作任务。** | — | 54 | Apache-2.0 | 已核验 |
| [**zhengxuyu/litjev**](https://github.com/zhengxuyu/litjev) | 将开源大模型转化为 Jev 决策层的开放复现实现，基于 Qwen 等模型直接读取选项 logits 提供 System One 兼容接口。 | Python | 46 | Apache-2.0 | [固定提交](https://github.com/zhengxuyu/litjev/blob/f21216c9fe5afe7fa52ff7064a402ee57fdbddd3/src/litjev/api.py#L1-L83) |
| [**emrickgarrett/OneVOneJev**](https://github.com/emrickgarrett/OneVOneJev) | 在浏览器里和 Jev 玩 1v1 射击。它读取结构化战况，选择走位、瞄准和开火。 | TypeScript | 40 | Unknown | [固定提交](https://github.com/emrickgarrett/OneVOneJev/blob/365b339d04446836352687b3650762106ea37f17/server/src/jev.ts) |
| [**lukaske/jev-doom-agent**](https://github.com/lukaske/jev-doom-agent) | 在浏览器里跑两份 Doom 引擎，让 Jev 根据游戏状态选择战术动作。 | TypeScript | 30 | Unknown | [固定提交](https://github.com/lukaske/jev-doom-agent/blob/318c32a24851444c1170bf083671c38723f3a35a/server/typesafe.ts) |
| [**PromptEngineer48/laya-vs-jev-arena**](https://github.com/PromptEngineer48/laya-vs-jev-arena) | 该项目让本地开源 Laya 与 API 驱动的 Jev 在贪吃蛇竞速和格斗对战中同场竞技，每一步动作都由模型实时决策。 | — | 29 | MIT | 已核验 |
| [**phyous/tsai-sc**](https://github.com/phyous/tsai-sc) | 让 Jev 操作原版 StarCraft shareware 的 Strongarm 关卡，读取状态与推理时暂停游戏。 | Python | 28 | MIT | [固定提交](https://github.com/phyous/tsai-sc/blob/6046ecc60156c4a3c04d384b41821a4ff08501b7/tsai_sc/typesafe.py) |
| [**sorrycc/typesafe-snake**](https://github.com/sorrycc/typesafe-snake) | 由 TypeSafe Jev 模型自动操作的贪吃蛇游戏，每 tick 执行一次原子决策，合法移动与物理事实均由本地代码生成。 | TypeScript | 23 | Unknown | [固定提交](https://github.com/sorrycc/typesafe-snake/blob/8bf3f7c261ad35ece3345a02d21ba638ddfaf87f/src/jev/client.ts#L1-L29) |
| [**vinilana/live-jev**](https://github.com/vinilana/live-jev) | 浏览器里的俯视小车模拟器，用 Jev 选择车道与速度，并可与聊天模型对跑。 | JavaScript | 21 | Unknown | [固定提交](https://github.com/vinilana/live-jev/blob/cd13ab0a7b58ca9b6749a78aed2a729153fa6910/server.js) |
| [**khordoo/jev-reflex-autonomy-lab**](https://github.com/khordoo/jev-reflex-autonomy-lab) | jev-reflex-autonomy-lab：Jev 作为 System 1 反射层，为每架无人机从 HOLD、转向、加减速等飞行动作中选择下一个最佳动作。 | — | 19 | MIT | 已核验 |
| [**gaborishka/jevtown**](https://github.com/gaborishka/jevtown) | 把 Jev 的结构化判断接进程序；具体用途与决策流程请查看项目源码。 | — | 13 | MIT | 已核验 |
| [**Skyvern-AI/jevscape**](https://github.com/Skyvern-AI/jevscape) | RuneBench 的 Jev 扩展，使用 rs-sdk 的有界动作目录驱动 RuneScape 游戏任务。 | TypeScript | 12 | Unknown | [固定提交](https://github.com/Skyvern-AI/jevscape/blob/8fe4d37349fc6a8d03ac1c918302eef254bb56c3/agents/jev/jev-client.ts#L3) |
| [**TarunTomar122/jev-askable-arm**](https://github.com/TarunTomar122/jev-askable-arm) | 在 ManiSkill 模拟机械臂中，让 Jev 把英文目标拆成一连串预设动作。 | — | 11 | MIT | [固定提交](https://github.com/TarunTomar122/jev-askable-arm/blob/bef98b31a122a7033dd4bfb52867cd6ccb2d7e67/jev_robotics/common.py#L76) |
| [**AbdelStark/heist-one**](https://github.com/AbdelStark/heist-one) | 可观察的浏览器潜行游戏，由 Jev 驱动守卫的强类型状态判断，而确定性代码引擎控制物理世界与移动规律。 | TypeScript | 8 | MIT | [固定提交](https://github.com/AbdelStark/heist-one/blob/632c9a55a1e5eb2cbf0b9f87db575f0b5eb36e8c/packages/game/src/decision.ts#L1-L451) |
| [**leftspace89/JevBird**](https://github.com/leftspace89/JevBird) | 让 Jev 玩 Python 版 Flappy Bird：程序先模拟路线，再让模型选择。 | Python | 8 | MIT | [固定提交](https://github.com/leftspace89/JevBird/blob/1e5fd1397382be91ce74ed0ab0cba86027c3470a/jev_pilot.py) |
| [**taodav/jev_deep_rl**](https://github.com/taodav/jev_deep_rl) | 该项目将 Jev 作为 Gymnasium 和 Atari 环境中的策略，通过游戏专用适配器把观测转换为结构化状态并选择合法动作，同时记录奖励与决策而不训练模型权重。 | — | 8 | Unknown | 已核验 |
| [**spoonnotfound/soupbase**](https://github.com/spoonnotfound/soupbase) | 汤底 Soupbase 是中英文海龟汤游戏，由 Jev 判定玩家提问和还原内容；应用代码校验结构化结果与置信度，决定是否通关。支持私有创作、链接分享和自行部署。 | — | 7 | MIT | 已核验 |
| [**AmoghCreator/doom-jev**](https://github.com/AmoghCreator/doom-jev) | 让 Jev 玩 Doom：看结构化战况，决定往哪走、瞄谁和什么时候开火。 | Python | 6 | Unknown | [固定提交](https://github.com/AmoghCreator/doom-jev/blob/b27663fc0fa386f9d15ad6ea3c8f15374b855479/agent/jev_client.py) |
| [**lbotinelly/jev-little-airways**](https://github.com/lbotinelly/jev-little-airways) | 小岛机场模拟器，让 Jev 判断飞机航路、避让、紧急广播与降落顺序。 | HTML | 6 | MIT | [固定提交](https://github.com/lbotinelly/jev-little-airways/blob/d6ec286c7821f41228bce9b33381546e4fca9bff/demo/server.mjs) |
| [**newuser7171/jev-gamepilot**](https://github.com/newuser7171/jev-gamepilot) | 该项目是基于 Laya 和 TypeSafe Jev System One 的自主游戏 Agent，可捕获游戏画面并在 Windows PC 游戏和 Android 手机游戏上执行操作。 | — | 6 | Unknown | 已核验 |
| [**FazalAAli/jev-robotics-demo**](https://github.com/FazalAAli/jev-robotics-demo) | MuJoCo 机械臂叠方块演示：程序提出候选动作，Jev 选择目标、抓放和是否完成。 | Python | 5 | MIT | [固定提交](https://github.com/FazalAAli/jev-robotics-demo/blob/531de61a75f386b0847f5f6f809a11424a75c29b/jev_agent.py) |
| [**oldmoldycake/jev_vampire_survivors**](https://github.com/oldmoldycake/jev_vampire_survivors) | 该项目让 Jev 模型通过 BepInEx 插件和 Python 大脑在原生 Linux 版 Steam 游戏 Vampire Survivors 中选择角色、关卡、升级和移动方向，并通过浏览器仪表盘实时展示决策。 | — | 5 | MIT | 已核验 |
| [**BrendanH18/jev_fsd**](https://github.com/BrendanH18/jev_fsd) | jev_fsd：读取当前状态，在可用动作中做选择。 | — | 4 | MIT | 已核验 |
| [**florian-hoenicke/jev-gpt**](https://github.com/florian-hoenicke/jev-gpt) | 用级联 Choice 把 Jev 当成逐词分类器，在词树上逐层选出下一个词。 | Python | 4 | Unknown | [固定提交](https://github.com/florian-hoenicke/jev-gpt/blob/25751a7f6a87ee31ee4ed2eb381fd746ca59c645/generate.py) |
| [**hosseintoussi/jev-flappy-bird**](https://github.com/hosseintoussi/jev-flappy-bird) | jev-flappy-bird：读取当前状态，在可用动作中做选择。 | — | 4 | MIT | 已核验 |
| [**liao96312/jev-arena-nanojev**](https://github.com/liao96312/jev-arena-nanojev) | 完全本地的 NanoJev 网格决策游戏实验场，支持中文 Pygame、多关卡与 GTX 1660S 训练 | — | 4 | Unknown | 已核验 |
| [**Bring-AI/jev-rl**](https://github.com/Bring-AI/jev-rl) | **JEV Reinforcement Learning** · 让 JEV 当裁判，让强化学习智能体学会玩游戏。 | — | 3 | MIT | 已核验 |
| [**zzsong1023/jev-market-reflex**](https://github.com/zzsong1023/jev-market-reflex) | 该项目将实时加密货币市场数据输入 Jev，生成类型化的买入/卖出/持有决策并应用于模拟纸面投资组合。 | — | 3 | MIT | 已核验 |
| [**4anti/jev-broadcast-lab**](https://github.com/4anti/jev-broadcast-lab) | 一个以国际象棋为主的 Jev 实验台，也能试工单分类、文档匹配和审核。 | JavaScript | 2 | Unknown | [固定提交](https://github.com/4anti/jev-broadcast-lab/blob/90ebea44467489e03c1fd2ab0416b54e32c25c13/web/shared/jev-client.js) |
| [**CompleteDotTech/jev-factorio-agent**](https://github.com/CompleteDotTech/jev-factorio-agent) | 这是一个由 Jev 驱动的 Factorio Agent，Jev 负责目标和下一步行动等快速宏观决策，确定性代码负责游戏规则、选项过滤与执行。 | — | 2 | MIT | 已核验 |
| [**hemanth/jev-chess**](https://github.com/hemanth/jev-chess) | 该项目使用 TypeSafe AI System One 的 Choice、Score 和 Noul 原语，将自然语言走棋意图解析为合法走法，并提供局面评估、历史棋手风格对手和整局对局分类。 | — | 2 | Unknown | 已核验 |
| [**Icohen007/jev-play-ping-pong**](https://github.com/Icohen007/jev-play-ping-pong) | 让 Jev 在浏览器乒乓球游戏中选择发球方向、回球角度和力度。 | JavaScript | 2 | MIT | [固定提交](https://github.com/Icohen007/jev-play-ping-pong/blob/af8eb3a1f2a14fcebca5accf23a7875b09b30d5e/src/typesafe.mjs#L1) |
| [**jaibhasin/jev-flappy-bird**](https://github.com/jaibhasin/jev-flappy-bird) | 该项目是一个浏览器 Flappy Bird 游戏，包含人类模式和由 Jev 选择 flap 或 wait 动作的物理模式。 | — | 2 | Unknown | 已核验 |
| [**jjd-lab/jev-synthetic-survey**](https://github.com/jjd-lab/jev-synthetic-survey) | jev-synthetic-survey：读取当前状态，在可用动作中做选择。 | — | 2 | MIT | 已核验 |
| [**lavallee/mk-jev-fly-brain**](https://github.com/lavallee/mk-jev-fly-brain) | 在 mk.js 格斗游戏中比较果蝇连接组脉冲仿真、Jev 和规则策略。 | JavaScript | 2 | MIT | [固定提交](https://github.com/lavallee/mk-jev-fly-brain/blob/8217937e6e725b0ce3160c6e1ab0183db8b8aa30/jev.py#L19) |
| [**Nachom3/jevTrader**](https://github.com/Nachom3/jevTrader) | 这是一个用 Rust 编写的高频交易程序，使用 Jev 作为决策模块。 | — | 2 | Unknown | 已核验 |
| [**phyous/tsai-civ2**](https://github.com/phyous/tsai-civ2) | Jev 玩原版《文明 II》实验框架：在浏览器中运行经典游戏引擎，实时输出各行动的概率分布并做出决策。 | — | 2 | Unknown | 已核验 |
| [**raihankhan-rk/jevarena**](https://github.com/raihankhan-rk/jevarena) | 两个 Jev Agent 在并排的浏览器 Snake 游戏里对战，观众可以查看每步方向选择。 | TypeScript | 2 | MIT | [固定提交](https://github.com/raihankhan-rk/jevarena/blob/c22adde05edfc3ee16911d38b12b337c5f9727a1/lib/server/jev.ts) |
| [**siroccomask/snake-jev**](https://github.com/siroccomask/snake-jev) | Jev 并行概率驱动的贪吃蛇实时游戏控制：在每个游戏 Tick 仅需一次并发 API 调用即可选出最佳转向。 | — | 2 | MIT | 已核验 |
| [**JanDalhuysen/jev-clash-royale-test**](https://github.com/JanDalhuysen/jev-clash-royale-test) | Clash Royale 风格沙盒里，Jev 在一次请求中决定是否出牌、出哪张、哪条路和站位深度。 | JavaScript | 1 | Unknown | [固定提交](https://github.com/JanDalhuysen/jev-clash-royale-test/blob/d25d0c7b4325a2c2f1449d40e1d834ff50069e21/jev_bot_loop.js) |
| [**LiuHao-1443/jev-table-tennis**](https://github.com/LiuHao-1443/jev-table-tennis) | 一句话：**这是一台用来观察一个决策模型「自己会不会打球」的仪器，顺便很好玩。** | — | 1 | MIT | 已核验 |
| [**mittal-parth/jev-experiments**](https://github.com/mittal-parth/jev-experiments) | 让 Jev 玩 Chrome 小恐龙和本地射击竞技场，Python 根据结构化判断执行动作。 | Python | 1 | Unknown | [固定提交](https://github.com/mittal-parth/jev-experiments/blob/2c8272ea13e2e4cee53f44dc8c6123b0c600edd6/dino_jev/client.py) |
| [**pinebit/jev-tetris**](https://github.com/pinebit/jev-tetris) | jev-tetris：读取当前状态，在可用动作中做选择。 | — | 1 | MIT | 已核验 |
| [**Romain-Jochum/typesafe-jev-decision-studio**](https://github.com/Romain-Jochum/typesafe-jev-decision-studio) | typesafe-jev-decision-studio：读取当前状态，在可用动作中做选择。 | — | 1 | Unknown | 已核验 |
| [**Siim/jev-claim-vs-measured**](https://github.com/Siim/jev-claim-vs-measured) | jev-claim-vs-measured：Jev根据市场状态特征对下一秒及15-60分钟价格涨跌给出买入/卖出方向概率决策。 | — | 1 | Unknown | 已核验 |
| [**TomRichner/can-jev-bayes**](https://github.com/TomRichner/can-jev-bayes) | 该项目在多臂老虎机任务上评估 Jev 的序列决策，并测试贝叶斯统计信息和决策建议能否改善其选择。 | — | 1 | Apache-2.0 | 已核验 |
| [**trycatchkamal/typesafe-jev-traffic-demo**](https://github.com/trycatchkamal/typesafe-jev-traffic-demo) | 该项目轮询观塘绕道与启福道交叉口的实时交通传感器数据，交由 Jev 判断信号相位优先级，并用本地状态机执行信号切换，在本地仪表盘上展示决策过程。 | — | 1 | Unknown | 已核验 |
| [**tubone24/jev-practice-speed**](https://github.com/tubone24/jev-practice-speed) | 这是一个 WebGL 卡牌游戏 Speed，玩家与以 Jev 为大脑的 CPU 对战，并实时显示 Jev 的决策速度和判断准确率。 | — | 1 | Unknown | 已核验 |
| [**YichenBC/jev-charactor**](https://github.com/YichenBC/jev-charactor) | jev-charactor：读取当前状态，在可用动作中做选择。 | — | 1 | Unknown | 已核验 |

## MCP & Integrations

| 项目 | 简介 | 语言 | ⭐ | 许可证 | 证据 |
|---|---|---:|---:|---:|---|
| [**vellum-ai/vellum-assistant**](https://github.com/vellum-ai/vellum-assistant) | Vellum Assistant 中的可选 Jev provider，可把会话状态与明确的问题交给 TypeSafe。 | TypeScript | 1379 | MIT | [固定提交](https://github.com/vellum-ai/vellum-assistant/blob/ee5ba342719e72b67698c2e1a4a78837321d0b1d/assistant/src/providers/jev/client.ts) |
| [**jkudish/jev-mcp**](https://github.com/jkudish/jev-mcp) | 给 Agent 提供核对引用、筛查内容、查找、重排、分类、比较和提取等八个 MCP 判断工具。 | TypeScript | 482 | MIT | [固定提交](https://github.com/jkudish/jev-mcp/blob/89f88b90c3180184d56961160e7178e64c98e468/src/provider.ts#L127) |
| [**itsmostafa/typesafe-mcp**](https://github.com/itsmostafa/typesafe-mcp) | 让 Claude Code、Claude Desktop、Codex 和 Pi 通过 MCP 或扩展向 Jev 提问，获取结构化判断。 | Go | 340 | MIT | [固定提交](https://github.com/itsmostafa/typesafe-mcp/blob/0c9f35d9b1859189fc7e7d01947061f311ca6dde/cmd/evaluate/client.go) |
| [**PyModel/jev-judge-mcp**](https://github.com/PyModel/jev-judge-mcp) | 这是一个为 MCP Agent 提供十一项 Jev 判断工具的服务，由 Jev 负责判断并由策略决定 auto、review 或 escalate。 | — | 85 | MIT | 已核验 |
| [**TheoOliveira/pi-jev**](https://github.com/TheoOliveira/pi-jev) | 为 Pi Agent 按任务寻找工具与技能，并提供结构化判断和可选的历史筛选。 | TypeScript | 61 | MIT | [固定提交](https://github.com/TheoOliveira/pi-jev/blob/0c3ac04bb5e039e7a334e8e79c8ad471a7a1b67c/src/jev.ts) |
| [**DevMortimer/pi-typesafe**](https://github.com/DevMortimer/pi-typesafe) | Pi 的 Jev 扩展，提供判断工具、终端试验命令和供其他扩展复用的 API。 | TypeScript | 47 | MIT | [固定提交](https://github.com/DevMortimer/pi-typesafe/blob/b822b8a0e4d729bd0db055a72581f21da686dd42/src/client.ts) |
| [**gamesonrblx/Jevbridge**](https://github.com/gamesonrblx/Jevbridge) | 通过 ACP、MCP 和命令行，把 Jev 或普通模型接成同一套结构化判断接口。 | — | 45 | MIT | [固定提交](https://github.com/gamesonrblx/Jevbridge/blob/54c5587565cb346788d67805ef2412f46a21bb33/src/client.ts#L1) |
| [**getsynkora/synkora-ai**](https://github.com/getsynkora/synkora-ai) | Synkora Agent 平台内置可选 TypeSafe 客户端与工具，用于分类、评分和是非判断。 | — | 39 | MIT | [固定提交](https://github.com/getsynkora/synkora-ai/blob/2ef7600c9772a025110e49ee06e66e18bb300843/api/src/core/typesafe_client.py#L2) |
| [**joshuaeroman/plasmallm**](https://github.com/joshuaeroman/plasmallm) | KDE Plasma 桌面助手中的 Jev Decisions 适配器，在部件里显示结构化判断结果。 | QML | 29 | GPL-2.0 | [固定提交](https://github.com/joshuaeroman/plasmallm/blob/b7d4975b31722624343d932a2b4a2d2b8a9952ff/package/contents/ui/adapters/decisions.js) |
| [**blakestone-x/jev-mcp**](https://github.com/blakestone-x/jev-mcp) | 把 Jev 的分类、打分、是非判断和候选匹配封装为 MCP 工具。 | Python | 25 | MIT | [固定提交](https://github.com/blakestone-x/jev-mcp/blob/59289a0b472a3ebc3e9abfebba2d59ec2c881863/jev_mcp/client.py) |
| [**Brainwires/jevwire**](https://github.com/Brainwires/jevwire) | 为 Agent 提供 Jev 的 MCP 工具、嵌入式库和 Claude Code hooks。 | TypeScript | 21 | MIT | [固定提交](https://github.com/Brainwires/jevwire/blob/21abf12fabced4089779f664424fc520a67eaacb/src/jev/client.ts) |
| [**Protocol-Lattice/harness-router**](https://github.com/Protocol-Lattice/harness-router) | 面向 Coding Agent 的工具选择轻量决策层，基于 MCP 架构与 Jev（OpenRouter 端点）动态评估上下文与候选工具并执行快速路由。 | — | 19 | MIT | 已核验 |
| [**integrate-your-mind/jev-codex-plugin**](https://github.com/integrate-your-mind/jev-codex-plugin) | 该 Codex 插件提供 Jev 决策咨询、失败命令诊断和基于证据的完成情况检查功能。 | — | 10 | MIT | 已核验 |
| [**rashedInt32/jev-mcp**](https://github.com/rashedInt32/jev-mcp) | 把 Jev 分类、评分、是非判断和批量提问封装成 MCP 工具，也提供 Claude Code 插件。 | — | 7 | MIT | [固定提交](https://github.com/rashedInt32/jev-mcp/blob/27603c12d06cd7899d93c0fbb8ce9331040b8a8c/src/index.ts#L230) |
| [**jiayylu/jev-as-quant**](https://github.com/jiayylu/jev-as-quant) | **把 System-1 决策模型（Laya / Jev）当作量化系统里的"判断层"，并和 Claude（System 2）组合使用。** 从需求分析、任务判断、架构设计、代码实现到模拟实验的完整项目，结论好的坏的都报告。 | — | 5 | Apache-2.0 | 已核验 |
| [**felpsdev/jev-classifier**](https://github.com/felpsdev/jev-classifier) | 连接编码 Agent 的本地 Jev 工具路由网关，同时提供 MCP 建议接口。 | TypeScript | 4 | MIT | [固定提交](https://github.com/felpsdev/jev-classifier/blob/e0c6cc7c6d2b1027be86ad8f4e03e191a88ec402/src/jev.ts) |
| [**simota/tenbin**](https://github.com/simota/tenbin) | 一套供编程 Agent 设计 Jev 判断流程的文档、MCP server 和 Skill，支持问题检查、批量评估与阈值校准。 | TypeScript | 4 | MIT | [固定提交](https://github.com/simota/tenbin/blob/80e797986b2334e988bb8c940329a31fe138fbdc/tenbin/src/client.ts) |
| [**123wwwa/JevTrace**](https://github.com/123wwwa/JevTrace) | JevTrace：通过工具接口提供选择、评分或概率判断。 | — | 3 | MIT | 已核验 |
| [**anasbekheit/typesafe-jev-mcp**](https://github.com/anasbekheit/typesafe-jev-mcp) | 该仓库是为 TypeSafe 的 Jev 模型提供服务的 MCP server，只暴露一个 evaluate 工具，用于接收 state 和类型化问题并返回带概率的 noul、choice 或 score 答案。 | — | 3 | MIT | 已核验 |
| [**BYK/jev-mcp**](https://github.com/BYK/jev-mcp) | 以评测为重点的 Jev MCP 服务，可单次提问、批量处理并比较问题和阈值。 | — | 3 | MIT | [固定提交](https://github.com/BYK/jev-mcp/blob/cee2e6d58112d006ccd3ebad1163a31083262ae9/src/typesafe.ts#L1) |
| [**himomohi/jev-skill-router**](https://github.com/himomohi/jev-skill-router) | jev-skill-router：通过工具接口提供选择、评分或概率判断。 | — | 3 | MIT | 已核验 |
| [**King4s/Jev-AI-Skill**](https://github.com/King4s/Jev-AI-Skill) | Jev-AI-Skill：通过工具接口提供选择、评分或概率判断。 | — | 3 | MIT | 已核验 |
| [**VishiATChoudhary/toolJev**](https://github.com/VishiATChoudhary/toolJev) | toolJev：通过工具接口提供选择、评分或概率判断。 | — | 3 | MIT | 已核验 |
| [**wangkuangkuang/jev-mcp-server**](https://github.com/wangkuangkuang/jev-mcp-server) | Jev 官方三种问题类型（choice/score/noul）的 Python MCP 服务器，外加批量 classify 与一键写入 5 家 agent 客户端配置的安装器，附实测延迟与成本数据。 | — | 3 | MIT | 已核验 |
| [**Ashfaqbs/jev-mcp-spring**](https://github.com/Ashfaqbs/jev-mcp-spring) | 该项目是基于 Java/Spring Boot 的 MCP server，通过 HTTP 将 TypeSafe Jev 封装为可供 MCP 客户端调用的类型化判断工具。 | — | 2 | Apache-2.0 | 已核验 |
| [**codaaiteam/jev-mcp**](https://github.com/codaaiteam/jev-mcp) | jev-mcp：通过工具接口提供选择、评分或概率判断。 | — | 2 | MIT | 已核验 |
| [**ctmx/openrouter-jev-mcp**](https://github.com/ctmx/openrouter-jev-mcp) | 该项目是通过 OpenRouter 提供 Jev Choice、Score 和 Noul 类型化决策的 Python 网关和 MCP 服务器，供编码 Agent 调用。 | — | 2 | MIT | 已核验 |
| [**kindintelligence/jev-rust-review**](https://github.com/kindintelligence/jev-rust-review) | 这是一个为 Claude Code 提供的 Rust 代码审查插件，用 MCP 服务器运行 rustc、Clippy 与 cargo-semver-checks 并结合 Jev 对变更代码做语义审查。 | — | 2 | MIT | 已核验 |
| [**legostin/jev-mcp**](https://github.com/legostin/jev-mcp) | jev-mcp：通过工具接口提供选择、评分或概率判断。 | — | 2 | MIT | 已核验 |
| [**moisesfilho/typesafe-jev-opencode**](https://github.com/moisesfilho/typesafe-jev-opencode) | typesafe-jev-opencode 把 Jev 的结构化判断做成 Agent 可调用的工具。 | — | 2 | MIT | 已核验 |
| [**molis-ai/jev-workbench**](https://github.com/molis-ai/jev-workbench) | 在本地网页定义、试跑与发布 Jev 判断函数，供后端和 Agent 调用固定版本。 | TypeScript | 2 | MIT | [固定提交](https://github.com/molis-ai/jev-workbench/blob/3d7d6f673d629a046f2e3d9b2f277095133a65c7/apps/server/src/provider.ts) |
| [**n3ndor/n8n-nodes-typesafe-jev**](https://github.com/n3ndor/n8n-nodes-typesafe-jev) | n8n 的社区 TypeSafe Jev 节点，让工作流提交结构化判断题。 | TypeScript | 2 | MIT | [固定提交](https://github.com/n3ndor/n8n-nodes-typesafe-jev/blob/22ae978a36149982fe14b8556eb0bab0250c2450/nodes/TypeSafeJev/transport.ts) |
| [**rahulthakore16/n8n-nodes-jev**](https://github.com/rahulthakore16/n8n-nodes-jev) | 该 n8n 社区节点将文本或 JSON 状态发送给 Jev，通过 Choice、Score 和 Noul 操作返回带概率和置信度的类型化决策，并保留原始输入、模型版本、Token 用量和延迟以供工作流使用。 | — | 2 | MIT | 已核验 |
| [**rajasekharponakala/jev-mcp**](https://github.com/rajasekharponakala/jev-mcp) | 该项目是封装 Jev 模型的 MCP 服务器，为 Agent 提供类型化的 noul 判断、多选和评分结果。 | — | 2 | AGPL-3.0 | 已核验 |
| [**reiswaffel78/jev-agent-toolkit**](https://github.com/reiswaffel78/jev-agent-toolkit) | 该仓库提供便携式 Agent Skill，教编码 Agent 将 Jev 用作有界判断层，并附带可选 MCP 桥及面向代码、浏览器研究、Blender 和 Unreal Engine 的工作流。 | — | 2 | MIT | 已核验 |
| [**Songokou1983/jev-mcp**](https://github.com/Songokou1983/jev-mcp) | 本地 MCP server，把 TypeSafe Jev（System One 决策模型）暴露成 Claude Code / Codex 等 MCP 客户端的原生 tool。 | — | 2 | Unknown | 已核验 |
| [**walidboulanouar/jev-agent-kit**](https://github.com/walidboulanouar/jev-agent-kit) | jev-agent-kit：通过工具接口提供选择、评分或概率判断。 | — | 2 | MIT | 已核验 |
| [**yctimlin/JevScout**](https://github.com/yctimlin/JevScout) | JevScout：通过工具接口提供选择、评分或概率判断。 | — | 2 | MIT | 已核验 |
| [**Afloat16/jev-mcp**](https://github.com/Afloat16/jev-mcp) | `jev-mcp` 将 TypeSafe AI 的 Jev 决策模型暴露为 4 个保守、只读的 MCP 工具， 用于**边界明确的概率决策**。 | — | 1 | MIT | 已核验 |
| [**baize7815/jev-mcp-open-source**](https://github.com/baize7815/jev-mcp-open-source) | 自部署的 MCP 网关，运行在 Cloudflare Workers 上，把 TypeSafe / Jev 的 System One 模型包装成九个工具，供 AI 助手在本地完成**意图路由、检索结果重排、批量语义判断**这类"判断但不生成长文"的工作。配套提供一个 Codex Skill，让助手在合适的决策点主动调用它。 | — | 1 | MIT | 已核验 |
| [**chy4pro/jev-in-mcp**](https://github.com/chy4pro/jev-in-mcp) | jev-in-mcp：通过工具接口提供选择、评分或概率判断。 | — | 1 | MIT | 已核验 |
| [**CodeIA-Academy/jev-mcp**](https://github.com/CodeIA-Academy/jev-mcp) | 该项目是一个无依赖的本地 MCP 服务器，将 Jev 作为 ask_jev 和 list_jev_models 工具提供给 Agent 使用。 | — | 1 | MIT | 已核验 |
| [**demircigoksu/jev-netlify-mcp**](https://github.com/demircigoksu/jev-netlify-mcp) | jev-netlify-mcp：通过工具接口提供选择、评分或概率判断。 | — | 1 | MIT | 已核验 |
| [**FZ2000/android-jev**](https://github.com/FZ2000/android-jev) | android-jev：通过工具接口提供选择、评分或概率判断。 | — | 1 | MIT | 已核验 |
| [**ieee0824/jev-mcp**](https://github.com/ieee0824/jev-mcp) | サーバー自身はリポジトリのファイルを読んだり、実行履歴を収集したり、ツールを実行したりしません。判断材料と有限個の候補は呼び出し側が用意します。Jevは自由文のplannerやコマンド生成器として使いません。 | — | 1 | MIT | 已核验 |
| [**jbt95/jev-toolkit**](https://github.com/jbt95/jev-toolkit) | 该仓库为 TypeSafe/Jev 提供一个基于 stdio 的 MCP 服务器，包含判断、排序和验证工具，并将调用记录在本地事件日志中。 | — | 1 | MIT | 已核验 |
| [**jiawei686/jev-review-mcp**](https://github.com/jiawei686/jev-review-mcp) | 将 git diff 转化为一个**有类型的决策** —— 无需冗长文本，宿主 agent 也无需了解任何 Jev API。 | — | 1 | MIT | 已核验 |
| [**jiawei686/jev-screen-mcp**](https://github.com/jiawei686/jev-screen-mcp) | 将文本转化为一个**有类型的决策** —— 无需冗长文本，宿主 agent 也无需了解任何 Jev API。 | — | 1 | MIT | 已核验 |
| [**kachar/jev-tool-search**](https://github.com/kachar/jev-tool-search) | jev-tool-search：通过工具接口提供选择、评分或概率判断。 | — | 1 | MIT | 已核验 |
| [**krw82/jev-playwright-mcp**](https://github.com/krw82/jev-playwright-mcp) | jev-playwright-mcp：通过工具接口提供选择、评分或概率判断。 | — | 1 | MIT | 已核验 |
| [**LeddoEngano/jev-eyes**](https://github.com/LeddoEngano/jev-eyes) | jev-eyes 在本地把图片转成 Jev 可决策的文字和布局状态，并提供 CLI、MCP server 和 Agent skill。 | — | 1 | MIT | 已核验 |
| [**MattiooFR/mcp-server-jev**](https://github.com/MattiooFR/mcp-server-jev) | 该项目为 Codex、Claude 等 MCP 客户端提供 jev_evaluate 工具，使用 Jev 对提供的文本进行分类、判断和打分。 | — | 1 | MIT | 已核验 |
| [**nekowasabi/jev-routing**](https://github.com/nekowasabi/jev-routing) | jev-routing：通过工具接口提供选择、评分或概率判断。 | — | 1 | MIT | 已核验 |
| [**ohernandezdev/jevmod**](https://github.com/ohernandezdev/jevmod) | jevmod：通过工具接口提供选择、评分或概率判断。 | — | 1 | MIT | 已核验 |
| [**thesammykins/jev_ampcode**](https://github.com/thesammykins/jev_ampcode) | 给 Amp 的方案比较插件：只比较已经提供的选项、证据和偏好。 | — | 1 | Unknown | [固定提交](https://github.com/thesammykins/jev_ampcode/blob/8741655927f4ae8ea476f833795d3bdfa6e8f293/decision.ts#L74) |
| [**Olli0103/openclaw-typesafe-ai**](https://github.com/Olli0103/openclaw-typesafe-ai) | OpenClaw 的独立社区插件，只注册一个需显式调用的 typesafe_decide 工具。 | TypeScript | 0 | MIT | [固定提交](https://github.com/Olli0103/openclaw-typesafe-ai/blob/985718448bf38a3a58d18389d376621b9bc54615/src/client.ts) |

## Routing & Cost Optimization

| 项目 | 简介 | 语言 | ⭐ | 许可证 | 证据 |
|---|---|---:|---:|---:|---|
| [**BerriAI/litellm**](https://github.com/BerriAI/litellm) | LiteLLM 的复杂度路由器可选用 Jev 判断请求应交给哪个模型档位。 | — | 60059 | Unknown | [固定提交](https://github.com/BerriAI/litellm/blob/56116079c8022da0e8f7ff9ccb017ad5aca5aed2/litellm/router_strategy/complexity_router/jev_classifier.py#L70) |
| [**can1357/oh-my-pi**](https://github.com/can1357/oh-my-pi) | Oh My Pi 编程 Agent 内含可选的 TypeSafe 判断提供器，供小型决策流程调用。 | — | 34110 | MIT | [固定提交](https://github.com/can1357/oh-my-pi/blob/78b753124d11f8dd3ae73e2524125890ff7c977e/packages/ai/src/judgment/typesafe.ts#L4) |
| [**davila7/claude-code-templates**](https://github.com/davila7/claude-code-templates) | claude-code-templates 社区仓库中的 Jev 路由模组，为 Claude Code 子 Agent 建议模型与思考档位。 | Python | 32293 | MIT | [固定提交](https://github.com/davila7/claude-code-templates/blob/61bfcd1586bf1076f6d3cfa0436317c912811e6c/cli-tool/components/mods/productivity/jev-model-router/hooks/jev-model-router.ts) |
| [**openchamber/openchamber**](https://github.com/openchamber/openchamber) | OpenChamber 可选开启自动模型路由：Jev 看消息属于哪类任务，再使用该类绑定的模型和思考档位。 | TypeScript | 11038 | MIT | [固定提交](https://github.com/openchamber/openchamber/blob/614d7f76e581a132a86575c03d3fa9aad5e624b6/packages/web/server/lib/routing/jev.js) |
| [**kunchenguid/firstmate**](https://github.com/kunchenguid/firstmate) | Firstmate 可选用 Jev 看任务简报并匹配派工规则，再由本地规则选择 Agent 配置。 | Shell | 7447 | MIT | [固定提交](https://github.com/kunchenguid/firstmate/blob/4812db801628040b609dc25a2a8a91ed5efac662/bin/fm-dispatch-resolve.sh) |
| [**kerpopule/hermes-jev-skills**](https://github.com/kerpopule/hermes-jev-skills) | 该仓库为 Hermes Agent 提供基于 Jev 的八个 SKILL.md 技能，负责模型路由、记忆筛选、转录压缩、技能选择以及计算机和浏览器操作决策。 | — | 997 | MIT | 已核验 |
| [**bastani-inc/atomic**](https://github.com/bastani-inc/atomic) | Atomic 编程 Agent 的可选 Jev 决策后端，为路由等流程提供受限的结构化选择。 | TypeScript | 843 | Unknown | [固定提交](https://github.com/bastani-inc/atomic/blob/33ca4ccb5f39488aeba67c0212a52a31cd14059d/packages/coding-agent/src/core/structured-output/jev.ts) |
| [**gargpratyush/jev-router**](https://github.com/gargpratyush/jev-router) | Claude Code / CLI 代理：Jev 给任务复杂度打分，并在当前账号可用的模型里选一个，再由本地策略决定是否更换。 | JavaScript | 521 | MIT | [固定提交](https://github.com/gargpratyush/jev-router/blob/38da6b84ea01241bfc41fbddc0928d0f40a703f0/src/policy.mjs#L1-L63) |
| [**notque/vexjoy-agent**](https://github.com/notque/vexjoy-agent) | 给 VexJoy 的任务分派增加一条 Jev 路线。输入需求后，判断该选哪位专长 Agent、哪项技能和哪条工作流。 | Python | 425 | MIT | [固定提交](https://github.com/notque/vexjoy-agent/blob/ab51ee7da567e84f72f76d73b6e7b83cec5ef060/scripts/jev-route.py) |
| [**WrongStack/WrongStack**](https://github.com/WrongStack/WrongStack) | 给 WrongStack 编程 Agent 增加一个可选分派助手。遇到多个相近的专长 Agent 时，用 Jev 判断谁更适合当前任务。 | TypeScript | 358 | MIT | [固定提交](https://github.com/WrongStack/WrongStack/blob/4cf97c0aa4f855751949ee8e99c719d06f4c26e0/packages/core/src/coordination/typesafe-dispatch-classifier.ts) |
| [**BillionsBobby/JevRouter**](https://github.com/BillionsBobby/JevRouter) | 把模型、Subagent、Skill、MCP 和 CLI 能力放进候选集，由 Jev 选择下一步用哪个。 | — | 357 | MIT | [固定提交](https://github.com/BillionsBobby/JevRouter/blob/715970774ae8070e958e83ac9b1a780b32a9184c/src/provider.ts#L72) |
| [**0xNatoshi/jev-codex-router**](https://github.com/0xNatoshi/jev-codex-router) | 每轮先让 Jev 判断任务类型与难度，再由本地策略为 Codex 选模型、思考深度和速度档。 | Python | 274 | MIT | [固定提交](https://github.com/0xNatoshi/jev-codex-router/blob/8292b519659280884627a962c826ac7721136a64/server/jev_server.py) |
| [**kitze/skillbox**](https://github.com/kitze/skillbox) | 自建一个有版本管理的 Agent 技能库，还能选配 Jev 推荐：告诉它当前任务，从你有权限使用的技能里挑更相关的。 | TypeScript | 256 | MIT | [固定提交](https://github.com/kitze/skillbox/blob/d83ba4ecd254c8dfa6a759d1feb5141384e26a9e/src/server/recommendations.ts) |
| [**Bodila51/grok-bot-jev**](https://github.com/Bodila51/grok-bot-jev) | 该项目为 Grok Bot 提供一个 Python 路由器，它在执行高成本操作前调用 Jev 对请求分类并返回明确的路由动作，同时附带可供 Grok Bot 技能使用的模板和示例。 | — | 92 | MIT | 已核验 |
| [**bladedevoff/stuntd**](https://github.com/bladedevoff/stuntd) | stuntd 是一个本地代理，用于记录应用向 Jev 兼容服务或 OpenAI 兼容服务发出的类型化决策请求，并为每个决策点在冻结的 Laya 编码器上训练小的模型头，在置信度足够时本地作答，否则回退到上游服务。 | — | 61 | Apache-2.0 | 已核验 |
| [**yusukebe/hono-jev-router**](https://github.com/yusukebe/hono-jev-router) | Hono 的实验性 HTTP 语义路由器，让请求描述决定走哪个处理函数。 | TypeScript | 51 | MIT | [固定提交](https://github.com/yusukebe/hono-jev-router/blob/04f6e103e1397bca659ab85c042011a1f14b679d/src/index.ts) |
| [**wundercorp/loki**](https://github.com/wundercorp/loki) | Loki 可选接入 Jev：提供类型化判断工具，并在新会话开始时从当前 gateway 的模型中选择档位。 | Python | 25 | MIT | [固定提交](https://github.com/wundercorp/loki/blob/5f1aea7c786f5ea8c5f9b9f2db2b791ec326c535/agent/jev_auto_router.py) |
| [**Bodila51/muse-jev-playbook**](https://github.com/Bodila51/muse-jev-playbook) | 该仓库提供在 Agent 执行高成本操作前使用 Jev 进行分流、分类、评分和门控的决策层 playbook，包含置信度策略、问题模板和参考路由。 | — | 24 | MIT | 已核验 |
| [**zjunlp/JevLoop**](https://github.com/zjunlp/JevLoop) | **你的 agent loop 里每一个岔路口都是一次完整的大模型调用。而它们没有一个是「生成」。** | — | 22 | Apache-2.0 | 已核验 |
| [**mejiasd3v/pi-jev-router**](https://github.com/mejiasd3v/pi-jev-router) | 面向 Pi 编程助手的自动模型路由器：通过 Vercel AI Gateway 集成 Jev，自动为不同编码任务分配合适模型。 | — | 16 | MIT | 已核验 |
| [**ruban-24/switchboard**](https://github.com/ruban-24/switchboard) | Switchboard 是面向 Claude Code 和 Codex 的本地模型路由工具，它用 Jev 评估新对话任务并按置信度规则选择模型与推理强度，然后在后续对话、工具调用和恢复会话中固定该选择。 | — | 16 | Apache-2.0 | 已核验 |
| [**vizuh/sabi**](https://github.com/vizuh/sabi) | Sabi 位于编码 harness 与模型提供方之间。harness 保持自己原有的 agent 循环；Sabi 决定每一轮推理由哪个模型、哪一级推理强度（reasoning effort）和哪个提供方来服务——贯穿整条轨迹持续决策，而不只在第一次提示时决定。 | — | 15 | MIT | 已核验 |
| [**DECRUX9812/typesafe-skill-router**](https://github.com/DECRUX9812/typesafe-skill-router) | 一个默认关闭的 Hermes Agent 插件，先用 Jev 从可用 Skill 中挑出与当前请求相关的一项建议。 | Python | 14 | MIT | [固定提交](https://github.com/DECRUX9812/typesafe-skill-router/blob/e6cdac26f9ed588b4a94b8a2f7f9f026e1b9faf3/typesafe_router/client.py) |
| [**prismhq/jev-router**](https://github.com/prismhq/jev-router) | 基于 LiteLLM 与 Jev 构建的开源模型路由器：根据输入任务复杂度与上下文自动选择性价比最高的大模型。 | — | 14 | MIT | 已核验 |
| [**emirbartu/jev-for-all**](https://github.com/emirbartu/jev-for-all) | 该仓库把 Jev 接入 OpenCode、Claude Code 和 Hermes，共用同一决策约定来决定加载哪个 skill、每步使用哪些工具以及 browser_task 中的每次操作。 | — | 11 | MIT | 已核验 |
| [**idovmamane/dejevu**](https://github.com/idovmamane/dejevu) | dejevu：给任务分类或评估难度，由本地策略决定模型与处理路径。 | — | 11 | MIT | 已核验 |
| [**yibie/laya-jev-lab**](https://github.com/yibie/laya-jev-lab) | 该仓库对比 Jev 与 Laya 在中文客服工单分类上的测量结果，并提供本地优先的 cascade 实验脚本。 | — | 11 | MIT | 已核验 |
| [**assistant-ui/jevia**](https://github.com/assistant-ui/jevia) | jevia：给任务分类或评估难度，由本地策略决定模型与处理路径。 | — | 10 | MIT | 已核验 |
| [**rajdhakad9826/jev-router**](https://github.com/rajdhakad9826/jev-router) | 基于 Jev 评分概率与期望损失最小化（Expected Loss Minimization）实现的成本敏感型大模型路由器。 | — | 10 | MIT | 已核验 |
| [**robertn702/opencode-jev-router**](https://github.com/robertn702/opencode-jev-router) | opencode-jev-router：给任务分类或评估难度，由本地策略决定模型与处理路径。 | — | 9 | MIT | 已核验 |
| [**AlexPEClub/Jev-Model-Router-Claude-Code**](https://github.com/AlexPEClub/Jev-Model-Router-Claude-Code) | Jev-Model-Router-Claude-Code 先判断任务难度，再选择要调用的模型。 | — | 8 | Unknown | 已核验 |
| [**dirien/jev-router**](https://github.com/dirien/jev-router) | jev-router：给任务分类或评估难度，由本地策略决定模型与处理路径。 | — | 8 | Apache-2.0 | 已核验 |
| [**miniLV/Jev-Auto-Router**](https://github.com/miniLV/Jev-Auto-Router) | 架构中，Jev 负责每次调用的模型与推理档位选择；本地 Responses 代理负责保持 Codex 会话和工具循环连续；任务结束后独立验收。Router Compass 把选路、实际用量和验收结果放在一起，回答一个问题：**少用旗舰模型之后，任务是否仍然正确完成，整体开销是否真的下降？** | — | 8 | Apache-2.0 | 已核验 |
| [**hemanth/tool-prune**](https://github.com/hemanth/tool-prune) | 该项目为 AI Agent 提供校准化的工具选择与 schema 裁剪功能，可在调用 LLM 前筛选出相关候选工具，并支持离线 TurboQuant 与云端 TypeSafe System One（Jev）双引擎。 | — | 7 | MIT | 已核验 |
| [**Akramovic1/jev-pilot**](https://github.com/Akramovic1/jev-pilot) | 这是一个 Claude Code 插件，在每轮对话前调用 Jev 来决定推理强度、子代理模型、执行策略和所需技能。 | — | 6 | Unknown | 已核验 |
| [**WXK-AI/jev-opus**](https://github.com/WXK-AI/jev-opus) | 在 Claude Code（Opus 5.5）每一轮推理及工具调用后，调用 Jev（/v1/systemone 端点）动态决策 Reasoning Effort 等级，保持提示词缓存完整。 | — | 5 | MIT | 已核验 |
| [**aaronshaf/opencode-jev-orchestrator**](https://github.com/aaronshaf/opencode-jev-orchestrator) | OpenCode 编排器：会话停在廉价父模型上，Jev 判定本轮偏难时才通过工具拉起更强的子 Agent。 | TypeScript | 4 | MIT | [固定提交](https://github.com/aaronshaf/opencode-jev-orchestrator/blob/ffe76fed66b3d544f218cacff1947fc191688c3a/src/jev.ts#L1-L193) |
| [**Charlyhno-eng/jev-codex-pilot**](https://github.com/Charlyhno-eng/jev-codex-pilot) | JEV Codex Pilot 将待办任务转为受控开发流程，由 JEV 评估任务并推荐 Codex 模型与推理深度，同时提供 Kanban 看板、实时进度、Token 用量和 AGENTS.md 上下文管理。 | — | 4 | MIT | 已核验 |
| [**rmosleydb/jev-smart-router**](https://github.com/rmosleydb/jev-smart-router) | 这是一个 Databricks App，它使用 JEV 为每条消息选择最合适的路由选项，然后在对应的 Databricks Foundation Model API 端点上执行推理并返回回复。 | — | 4 | MIT | 已核验 |
| [**satviksinha/jev-model-router**](https://github.com/satviksinha/jev-model-router) | 这是一个用于 Claude Code 的模型路由器，每轮对话前用 Jev 选择层级和思考强度并把请求路由到对应模型。 | — | 4 | MIT | 已核验 |
| [**suenot/codex-jev-router**](https://github.com/suenot/codex-jev-router) | Jev judges a short Codex subagent task summary, then local confidence rules select a model and reasoning tier or fall back to Sol. 基于 Jev 判断 Codex 子代理任务摘要，由本地规则选择模型与推理档位。 | — | 4 | MIT | 已核验 |
| [**trietphan/jev-claw**](https://github.com/trietphan/jev-claw) | 该插件为 OpenClaw Agent 提供类型化模型路由，先用 Jev 对任务分类，再通过代码中的策略决定路由。 | — | 4 | MIT | 已核验 |
| [**gholtzap/jev-codex-model-and-effort-router**](https://github.com/gholtzap/jev-codex-model-and-effort-router) | 该项目在每次 Codex 消息时由 Jev 按请求复杂度选择 model 和 effort，并提供 macOS 菜单栏应用来管理路由偏好与可选池。 | — | 3 | Unknown | 已核验 |
| [**iamvatsalpatel/tiershift**](https://github.com/iamvatsalpatel/tiershift) | 基于 YAML 声明策略的模型分级路由工具，在约 180 毫秒内通过 Jev 将请求路由到满足要求的最低成本模型。 | TypeScript | 3 | MIT | [固定提交](https://github.com/iamvatsalpatel/tiershift/blob/16a0826b9f62eba6699240c4b53a7237a8c41617/bench/experiments/gate-experiment.ts#L1-L83) |
| [**maker-KK/todo-jev**](https://github.com/maker-KK/todo-jev) | 结合 skill 条件和环境检查的任务路由实验，推荐规则、skill 或大模型处理路径。 | Python | 3 | MIT | [固定提交](https://github.com/maker-KK/todo-jev/blob/08c8a1e744c311e9f88721b414e636d7eb7c156c/app/classifier.py) |
| [**mcftira/jev-route**](https://github.com/mcftira/jev-route) | jev-route 是按任务难度和数据敏感度做路由的路由器，先用 Jev 云端决策并记录完整决策日志，再从日志中蒸馏出本地路由模型。 | — | 3 | Apache-2.0 | 已核验 |
| [**Chandler-Sun/chat2jev**](https://github.com/Chandler-Sun/chat2jev) | 把 OpenAI 兼容的 Chat Completions 请求转换成 TypeSafe System One（Jev）的 **State / Questions**，对照文字生成与结构化判断的结果，并把可复用的问题发布为代理路由。 | — | 2 | MIT | 已核验 |
| [**FirasSX914/Janus**](https://github.com/FirasSX914/Janus) | 模型适用性测量与路由框架，评估业务数据在 Jev 与传统大模型之间的收益边界并执行最优动态分发。 | Python | 2 | MIT | [固定提交](https://github.com/FirasSX914/Janus/blob/9cb66c488cf884e5997356a0de45f75aa3148774/src/janus/providers/typesafe.py#L1-L60) |
| [**Flam1ngFir3ball/jev-claude-router**](https://github.com/Flam1ngFir3ball/jev-claude-router) | jev-claude-router：给任务分类或评估难度，由本地策略决定模型与处理路径。 | — | 2 | MIT | 已核验 |
| [**herval/openclaw-jev-plugin**](https://github.com/herval/openclaw-jev-plugin) | 该插件在语言模型运行前使用 Jev 概率判断群聊消息是否需要回复，并按工作量和风险为 Agent 选择轻量、标准或重量模型档位。 | — | 2 | Unknown | 已核验 |
| [**hugo-alves/jev-router-playground**](https://github.com/hugo-alves/jev-router-playground) | 模型路由实验页：让 Jev 从候选模型中选择，再由你比较各模型的实际回答。 | — | 2 | MIT | [固定提交](https://github.com/hugo-alves/jev-router-playground/blob/c2eb6ccf68b793d4ad99fb0ff1cc29edf11d9a93/app.js#L56) |
| [**itscloud0/codex-jev-native-router**](https://github.com/itscloud0/codex-jev-native-router) | codex-jev-native-router：给任务分类或评估难度，由本地策略决定模型与处理路径。 | — | 2 | MIT | 已核验 |
| [**lucianfialho/jev-model-router**](https://github.com/lucianfialho/jev-model-router) | 该库使用 Jev 对请求进行分类，并从 OpenRouter 实时模型目录中筛选出满足约束的最便宜可用模型。 | — | 2 | MIT | 已核验 |
| [**onlyjq04/jev-agent-hooks**](https://github.com/onlyjq04/jev-agent-hooks) | jev-agent-hooks：给任务分类或评估难度，由本地策略决定模型与处理路径。 | — | 2 | MIT | 已核验 |
| [**ourines/hermes-jev**](https://github.com/ourines/hermes-jev) | `jev_evaluate` 支持自定义问题和三个快速预设：`task_triage`（任务分类与风险信号）、`next_step`（下一步建议）、`relevance`（资料相关性）。新增 `jev_route`：让 Jev 在 2–32 个候选模型配置中选出更适合当前任务的一个，返回顶层 `selected_model`、`confidence`… | — | 2 | MIT | 已核验 |
| [**peterwanghot/jev-cc-codex-router**](https://github.com/peterwanghot/jev-cc-codex-router) | 它是 Codex 和上游之间的一个本地代理：每来一个新任务，就让 Jev 判断难度，把请求改用 luna、terra、sol、astra 里够用的最便宜的模型，遇到上游偶发的 400 和 502 还会自动重试。 | — | 2 | MIT | 已核验 |
| [**sherajdev/jev-research**](https://github.com/sherajdev/jev-research) | 一份 Jev 与 Herdr 协作指南，附有把任务分给不同 Agent 的路由原型。 | TypeScript | 2 | MIT | [固定提交](https://github.com/sherajdev/jev-research/blob/23da0defeebe5dae232ba1aaa7ee3c0c3842cb8e/jev-router.ts) |
| [**TokenTrim/jev-routing-experiment**](https://github.com/TokenTrim/jev-routing-experiment) | 该仓库把 Jev 用作 LLM 路由器，在 RouterArena 和 LLMRouterBench 查询上为每个查询选择模型并用各自官方评分方法计分。 | — | 2 | Apache-2.0 | 已核验 |
| [**zkjoie/jevbus**](https://github.com/zkjoie/jevbus) | 这是一个流式事件总线，为每个事件向 Jev 请求概率判断，并据此决定订阅路由、投递、复核或丢弃，同时记录 Ledger、重试、熔断与死信。 | — | 2 | Apache-2.0 | 已核验 |
| [**atulify/omp-plugin-jev-router**](https://github.com/atulify/omp-plugin-jev-router) | omp-plugin-jev-router：给任务分类或评估难度，由本地策略决定模型与处理路径。 | — | 1 | Unknown | 已核验 |
| [**david96182/cribrix**](https://github.com/david96182/cribrix) | cribrix：给候选记录判断相关性或打分，再由本地程序筛选和排序。 | — | 1 | MIT | 已核验 |
| [**Pasblinn/jev-lab**](https://github.com/Pasblinn/jev-lab) | jev-lab：给任务分类或评估难度，由本地策略决定模型与处理路径。 | — | 1 | MIT | 已核验 |
| [**punkcanyang/hermes-jev-router**](https://github.com/punkcanyang/hermes-jev-router) | 1. **模型路由**：每轮调用前用 TypeSafe **Jev** 选模型（简单走便宜、复杂／工具重／长上下文走更强），失败或低置信回退主模型。 2. **先裁再压**：上下文引擎 `trim_compress` 强制 **trim → compress**，禁止不裁直接压。 | — | 1 | MIT | 已核验 |
| [**ReallyArtificial/stuntdouble**](https://github.com/ReallyArtificial/stuntdouble) | stuntdouble 是一个零依赖 Node 代理，转发应用发往 Jev 的请求并同步询问 Kev、Laya 等本地模型，然后记录所有回答并生成两者决策是否一致的替换评估报告。 | — | 1 | MIT | 已核验 |
| [**shyamsridhar123/JudgeJev**](https://github.com/shyamsridhar123/JudgeJev) | JudgeJev：给任务分类或评估难度，由本地策略决定模型与处理路径。 | — | 1 | MIT | 已核验 |
| [**VyetGokyra/jev-codex-factory**](https://github.com/VyetGokyra/jev-codex-factory) | jev-codex-factory：给任务分类或评估难度，由本地策略决定模型与处理路径。 | — | 1 | Apache-2.0 | 已核验 |
| [**kuldeepsinh19/jev-decision-gateway**](https://github.com/kuldeepsinh19/jev-decision-gateway) | 把是否继续、用哪个工具、要不要校验交给 Jev，只有策略允许时才调用生成式 LLM。 | TypeScript | 0 | MIT | [固定提交](https://github.com/kuldeepsinh19/jev-decision-gateway/blob/67111792e840e150239d12337a1d939be68be0e6/packages/core/src/jev/adapter.ts) |
| [**minghanminghan/jev-demo**](https://github.com/minghanminghan/jev-demo) | Jev 客服分流演示：先批量回答路由问题，再沿分类结果处理用户请求。 | TypeScript | 0 | Unknown | [固定提交](https://github.com/minghanminghan/jev-demo/blob/b6892294f97384bca86d68af9b56e0ea705d7893/app/api/jev/[...path]/route.ts) |
| [**TexasOct/jev-gateway**](https://github.com/TexasOct/jev-gateway) | 制定不同的模型使用策略，达到控制模型成本/更高效的agent工作效率。 | — | 0 | AGPL-3.0 | 已核验 |

## SDK & Decision Frameworks

| 项目 | 简介 | 语言 | ⭐ | 许可证 | 证据 |
|---|---|---:|---:|---:|---|
| [**ComposioHQ/composio**](https://github.com/ComposioHQ/composio) | Composio 的可选 TypeSafe provider，用 Jev 从工具与有限参数选项中做判断。 | TypeScript | 30400 | MIT | [固定提交](https://github.com/ComposioHQ/composio/blob/4b5920bf7aa55c8a44657b060d4bd25ce7b13a9a/ts/packages/providers/typesafe/src/decide.ts) |
| [**vercel/ai**](https://github.com/vercel/ai) | AI SDK 中的 TypeSafe provider，让 TypeScript 应用通过统一 evaluate 接口调用 Jev。 | TypeScript | 27088 | Unknown | [固定提交](https://github.com/vercel/ai/blob/73ec7015edd4f04ca9144ce93a8a037a731e5db8/packages/typesafe-ai/src/typesafe-ai-evaluation-model.ts) |
| [**elizaOS/eliza**](https://github.com/elizaOS/eliza) | Eliza 源码中的可选 TypeSafe HTTP 适配器，默认没有注册到 Agent 运行时。 | TypeScript | 19536 | MIT | [固定提交](https://github.com/elizaOS/eliza/blob/ebc808e3a67fb941e29153d89fc896524d32fe3c/packages/agent/src/services/typesafe/client.ts) |
| [**langchain-ai/langchainjs**](https://github.com/langchain-ai/langchainjs) | LangChain.js 的可选 TypeSafeClassifier 集成，把状态和预设问题交给 Jev。 | TypeScript | 18245 | MIT | [固定提交](https://github.com/langchain-ai/langchainjs/blob/206d8b992bcf90ce7d46f2158f1ad85fc1d826c0/libs/providers/langchain-typesafe/src/classifier.ts) |
| [**0xPlaygrounds/rig**](https://github.com/0xPlaygrounds/rig) | Rig 仓库中的实验性 TypeSafe crate，用 Rust 类型组织 Jev 的问题与答案。 | Rust | 8794 | MIT | [固定提交](https://github.com/0xPlaygrounds/rig/blob/2d16c1b25f6749b3a2cd841beddf767106495069/crates/rig-typesafeai/src/wire.rs#L40) |
| [**feder-cr/jev**](https://github.com/feder-cr/jev) | jevos 是与 Jev 兼容的开源 yes/no 决策服务，在笔记本 CPU 上通过单次模型前向计算返回 P(yes)，仅支持 noul 类型问题。 | — | 1181 | MIT | 已核验 |
| [**razorback16/openjev**](https://github.com/razorback16/openjev) | 一个兼容 Jev System One 接口的独立决策服务，使用开源 DiffusionGemma 模型运行。 | Python | 591 | Apache-2.0 | [固定提交](https://github.com/razorback16/openjev/blob/91d5005effcf8cc0ecccaa9538ceabbb130fef59/openjev/api.py) |
| [**agentjido/req_llm**](https://github.com/agentjido/req_llm) | ReqLLM 的 TypeSafe provider，让 Elixir 应用通过 evaluate 接口调用 Jev。 | Elixir | 589 | Apache-2.0 | [固定提交](https://github.com/agentjido/req_llm/blob/9cb0ee7a0fea5f3520fc953911d352c93193615e/lib/req_llm/providers/typesafe.ex) |
| [**featherless-ai/simple-jev**](https://github.com/featherless-ai/simple-jev) | 将任意开源大语言模型转化为分类器与 Jev 兼容端点的适配服务，无需额外训练专用分类头。 | Python | 580 | Apache-2.0 | [固定提交](https://github.com/featherless-ai/simple-jev/blob/0dd5396ffce671ab7c4bfc031506d8e558cf8d23/demos/jevpilot/src/simple-jev-api.js#L1-L85) |
| [**wuyoscar/jev-skill**](https://github.com/wuyoscar/jev-skill) | 该项目是 Jev 用例、工作流和 Agent Skills 的集合，并提供基于标准库的 Python 决策封装脚本。 | — | 559 | MIT | 已核验 |
| [**cognesy/instructor-php**](https://github.com/cognesy/instructor-php) | Instructor PHP 的 Polyglot 模块内置 TypeSafe Decision 驱动。 | PHP | 328 | MIT | [固定提交](https://github.com/cognesy/instructor-php/blob/bb1160ce2360dcf1434788c46ee97809fe782ea3/packages/polyglot/src/Decision/Drivers/TypeSafe/TypesafeDriver.php) |
| [**hr98w/jev-visual**](https://github.com/hr98w/jev-visual) | 在 Apple Silicon Mac 本地跑的视觉版 Jev 实验。对单张图片做选择、打分与是非判断，自带 3 个本地视觉游戏 Demo。 | — | 303 | MIT | 已核验 |
| [**monotykamary/pi-fabric**](https://github.com/monotykamary/pi-fabric) | 给 Pi 的工具运行时加上可编程的 Jev 决策循环。先写好观察、判断和执行步骤，再让它按预算在前台或后台运行。 | TypeScript | 278 | MIT | [固定提交](https://github.com/monotykamary/pi-fabric/blob/2e5fcdd94cc364445b115756edefcaab24f68928/src/jev/client.ts) |
| [**typesafe-ai/typesafe-sdk-js**](https://github.com/typesafe-ai/typesafe-sdk-js) | TypeSafe 组织发布的 JavaScript 与 TypeScript SDK，提供 Jev 请求和回答类型。 | TypeScript | 266 | MIT | [固定提交](https://github.com/typesafe-ai/typesafe-sdk-js/blob/66880ccded6cb642dc1809620c2b108c33730214/src/client.ts) |
| [**typesafe-ai/typesafe-sdk-python**](https://github.com/typesafe-ai/typesafe-sdk-python) | TypeSafe 官方 Python SDK，提供 Jev System One 的同步、异步客户端及问题和回答类型。 | Python | 262 | MIT | [固定提交](https://github.com/typesafe-ai/typesafe-sdk-python/blob/2ce5c65f13646cab6e6f782328194c9d85f3300a/src/typesafe_sdk/_core/client/sync/client.py#L206-L221) |
| [**cequence-io/openai-scala-client**](https://github.com/cequence-io/openai-scala-client) | 让 Scala 应用也能接入 Jev。这个多模型客户端新增了独立 TypeSafe 模块，用状态和判断题获取结构化答案。 | Scala | 255 | MIT | [固定提交](https://github.com/cequence-io/openai-scala-client/blob/cfabe8842344da713615d0121a7804840649eb46/typesafe-client/src/main/scala/io/cequence/openaiscala/typesafe/service/impl/TypeSafeServiceImpl.scala) |
| [**Devin-AXIS/jev-dsh-decision**](https://github.com/Devin-AXIS/jev-dsh-decision) | Jev DSH 决策引擎｜面向 Agent Harness 的结构化决策插件。原生支持 DeepSeek Harness，通过 iPolloWork 支持 OpenCode、Codex Harness。 | — | 252 | Unknown | 已核验 |
| [**fstandhartinger/jevbench**](https://github.com/fstandhartinger/jevbench) | 该仓库提供 JevBench 基准，向 Jev 类决策模型输入状态和有界评分规则，并对返回的类型化答案按 Intelligence、Calibration、Speed 和 Cost 四个维度计分。 | — | 200 | MIT | 已核验 |
| [**Michaelliv/runline**](https://github.com/Michaelliv/runline) | Runline 的 TypeSafe 插件，把 Jev 判断作为 Agent JavaScript 可调用的动作。 | TypeScript | 164 | Unknown | [固定提交](https://github.com/Michaelliv/runline/blob/6bdddfa82cd95b6b9a07e57fd93a271ae83a0d1b/packages/runline-plugins/typesafe/src/shared.ts) |
| [**hackclub/ai**](https://github.com/hackclub/ai) | Hack Club AI 代理中的 Jev 转发接口，复用已有鉴权、限额和用量记录。 | TypeScript | 135 | Unknown | [固定提交](https://github.com/hackclub/ai/blob/a76ea2cb159f707a60107935a5b2e0dbdc7455f5/src/routes/proxy/v1/jev.ts) |
| [**cobusgreyling/Jev**](https://github.com/cobusgreyling/Jev) | 该仓库是 Jev 的非官方展示与操作实验台，用智能家居演示、交互实验、示例脚本、TypeScript harness CLI 和 Agent skills 说明 Choice、Score、Noul 并行判断与置信度路由的用法。 | — | 130 | MIT | 已核验 |
| [**danieljvdm/effect-agent**](https://github.com/danieljvdm/effect-agent) | Effect Agent 的 TypeSafe 决策 provider，支持类型化问题集与可选模型选择。 | TypeScript | 130 | MIT | [固定提交](https://github.com/danieljvdm/effect-agent/blob/88005e497e9b627eeb16d670f278903c57601da9/packages/ai-typesafe/src/TypeSafeClient.ts) |
| [**pithings/advocaat**](https://github.com/pithings/advocaat) | 用简短的 TypeScript 调用向 Jev 提问。把同一份数据里的多个判断一次写好，直接拿到概率、选项和分数。 | TypeScript | 96 | MIT | [固定提交](https://github.com/pithings/advocaat/blob/bc46287fc1102b95852a81d679c6e34a2c44f4a2/src/api.ts) |
| [**andududu/jeview**](https://github.com/andududu/jeview) | Jeview 是一个本地网关，把代码发往 Jev 的每次调用转发出去，存入本地 SQLite 数据库，并在实时地图上展示。 | — | 61 | MIT | 已核验 |
| [**obie/ruby_decision_model**](https://github.com/obie/ruby_decision_model) | Ruby 决策模型客户端，可通过 TypeSafe 原生接口或 OpenRouter 调用 Jev。 | Ruby | 51 | MIT | [固定提交](https://github.com/obie/ruby_decision_model/blob/f79a890ce4eaa8f83d8220727319ee7b11416e01/lib/ruby_decision_model/providers/typesafe.rb) |
| [**hunkim/solar-mini4-jev**](https://github.com/hunkim/solar-mini4-jev) | 该项目提供兼容 Jev System One 接口形态的封装，通过统一的状态与问题结构调用 Solar Mini4 处理 noul、choice 和 score 类型问题。 | — | 45 | Unknown | 已核验 |
| [**mattn/go-jev**](https://github.com/mattn/go-jev) | 这是为 Jev 提供结构化判定结果的 Go SDK 和命令行工具，可请求 yes/no、choice 和 score 类型的答案。 | — | 41 | MIT | 已核验 |
| [**shantanugoel/ask-jev-skill**](https://github.com/shantanugoel/ask-jev-skill) | Hermes Agent 与通用智能体的 Jev 技能扩展：为代理提供封闭选项评估与置信度不足时的升级决策机制。 | — | 41 | MIT | 已核验 |
| [**dannote/jev**](https://github.com/dannote/jev) | 把 Jev 接成 Elixir/OTP 异步进程，在 GenServer 中用模式匹配处理返回结果。 | — | 35 | MIT | [固定提交](https://github.com/dannote/jev/blob/09fbb6cbaf32257924c08ba993ca8631adc16056/lib/jev/http.ex#L3) |
| [**TypeLLM/pijev**](https://github.com/TypeLLM/pijev) | pijev：由业务代码定义问题，客户端负责提交 Jev 请求并解析结构化结果。 | — | 34 | Apache-2.0 | 已核验 |
| [**Zaious/jev-capability-atlas**](https://github.com/Zaious/jev-capability-atlas) | **機制上**：它很快、很便宜，只能做「選一個選項/打個分/回答是非」這種窄判斷，不會寫文字解釋自己在想什麼。因為答案空間是你自己先定義好的，它**結構上不可能吐出選項清單以外的東西**——這跟自由生成文字的模型偶爾格式跑掉、甚至生出一個你沒列的分類，是不同等級的保證，不是機率低，是型別上不可能（但這只保證答案落在清單裡，不保證選到的那個是對的，細節見… | — | 26 | MIT | 已核验 |
| [**zeredy879/minojev**](https://github.com/zeredy879/minojev) | 独立实现的 System-1 决策模型：一次前向传播输出 Choice、Noul(Boolean)、Score 的校准概率分布，全程零输出 token，可在笔记本 CPU 上离线训练。 | — | 25 | MIT | 已核验 |
| [**6Mikao9/jev-agent-design-with-topk-logits-choices**](https://github.com/6Mikao9/jev-agent-design-with-topk-logits-choices) | 实验主线使用逻辑空间 10/100/1K/10K/100K、resident K=8/16/32，在删除正确 coarse candidate 后比较 argmax、repropose、full LLM handoff、helper top1、helper topK+Jev、`+EXPAND_K`、`+BACKTRACK/LOOKUP/CLARIFY`… | — | 22 | Unknown | 已核验 |
| [**csskrtao/jev-to-answer**](https://github.com/csskrtao/jev-to-answer) | 把困惑写下来，让大模型整理可能，让 Jev 给出一个方向。 | — | 20 | Unknown | 已核验 |
| [**Ray-Hughes/jevalyn**](https://github.com/Ray-Hughes/jevalyn) | Jevalyn 是 Rails 应用的决策层，封装 Jev System One API，用 noul、choice 和 score 三种类型化问题返回结构化判定，并提供 Guardrail 和 Router 辅助控制流程。 | — | 19 | MIT | 已核验 |
| [**yijunyu/jev-rs**](https://github.com/yijunyu/jev-rs) | 这是一个 Rust 编写的 Jev 兼容引擎，可在一次 prefill 中让任意 LLM 返回关于一段 state 的 noul、choice 和 score 类型判断及其概率，并可作为 MCP 工具供 Agent 调用。 | — | 17 | Apache-2.0 | 已核验 |
| [**ainame/swift-typesafe**](https://github.com/ainame/swift-typesafe) | 社区 Swift TypeSafe 客户端，提供类型化问题、动态问题与响应解析。 | Swift | 16 | MIT | [固定提交](https://github.com/ainame/swift-typesafe/blob/c990db869c10030b98af02e1219f5bca1e2c7cc2/Sources/TypeSafe/TypeSafeClient.swift) |
| [**d-date/swift-jev**](https://github.com/d-date/swift-jev) | 为 TypeSafe AI Jev 提供 Swift 类型安全库与可从终端调用的 JSON 命令行工具。 | — | 16 | MIT | 已核验 |
| [**doeixd/discern**](https://github.com/doeixd/discern) | Effect 的语义控制流库：把 Jev 的 Choice / Noul / Score 答案变成带类型的分支。阈值由调用方提供，低于阈值的答案走显式的 `Uncertain` 分支（编译器强制处理），而不是被四舍五入成最高分标签；procedure 路由先用确定性谓词筛选候选，只剩一个时完全跳过模型调用。 | — | 15 | MIT | 已核验 |
| [**harshithsunku/learn-jev-end-to-end**](https://github.com/harshithsunku/learn-jev-end-to-end) | 这是一个免费的动手教程项目，用 12 个 Notebook 教你用 Jev 快脑加 LLM 慢脑构建 13 种 AI 工具。 | — | 14 | MIT | 已核验 |
| [**Kevthetech143/super-jev**](https://github.com/Kevthetech143/super-jev) | 一个 TypeScript 决策执行框架，把证据、Jev 判断、允许的动作和结果记录串起来。 | Python | 14 | MIT | [固定提交](https://github.com/Kevthetech143/super-jev/blob/69bb082587459aa2e78245fbb713aac54d53a204/src/jev.ts) |
| [**Twister915/typesafe-ai**](https://github.com/Twister915/typesafe-ai) | 一个 Rust TypeSafe 客户端，提供异步 reqwest 或阻塞 ureq 后端，并可观察重试过程。 | Rust | 13 | Apache-2.0 | [固定提交](https://github.com/Twister915/typesafe-ai/blob/d4455efb1d061ae6aac47b40c42ef390182201b1/src/reqwest_client.rs) |
| [**ali-master/usejev**](https://github.com/ali-master/usejev) | usejev：由业务代码定义问题，客户端负责提交 Jev 请求并解析结构化结果。 | — | 12 | Unknown | 已核验 |
| [**saibimajdi/typesafeai-dotnet-sdk**](https://github.com/saibimajdi/typesafeai-dotnet-sdk) | 适用于 .NET 8+ 的 TypeSafe AI / Jev 客户端 SDK，支持 Choice、Score 与 Noul 决策原语与强类型响应解析。 | C# | 12 | MIT | [固定提交](https://github.com/saibimajdi/typesafeai-dotnet-sdk/blob/6be669e0d0b116b76e85136c4f6eaa44fadcecab/src/TypeSafe.Sdk/TypeSafeClient.cs#L1-L283) |
| [**Premo-Cloud/typesafe-sdk-java**](https://github.com/Premo-Cloud/typesafe-sdk-java) | 社区维护的 Java TypeSafe 客户端，并提供 Spring Boot Starter 来配置 Jev 调用。 | Java | 11 | MIT | [固定提交](https://github.com/Premo-Cloud/typesafe-sdk-java/blob/833893bc46aa3de2e07352a729ff618ea07b6350/typesafe-sdk/src/main/java/io/github/premocloud/typesafe/TypeSafeClient.java) |
| [**TannerMidd/SpecPi**](https://github.com/TannerMidd/SpecPi) | Pi 编码 Agent 的配置与扩展集合，包含可选 Jev 顾问，用于能力建议和工作流检查。 | JavaScript | 11 | MIT | [固定提交](https://github.com/TannerMidd/SpecPi/blob/55c4c55e9d8d5c2a5ae803d7f4e5ebd5427a45c3/extensions/jev-advisor/client.mjs) |
| [**jmanhype/jev-dspy-lab**](https://github.com/jmanhype/jev-dspy-lab) | 该项目为 DSPy 工作流中的 Jev 决策提供可离线复现的校准、置信度门控和选择风险基准测试。 | — | 10 | MIT | 已核验 |
| [**vercel-labs/jev-ai-sdk-form-router**](https://github.com/vercel-labs/jev-ai-sdk-form-router) | jev-ai-sdk-form-router：由业务代码定义问题，客户端负责提交 Jev 请求并解析结构化结果。 | — | 10 | MIT | 已核验 |
| [**Tangerg/typesafe-sdk-go**](https://github.com/Tangerg/typesafe-sdk-go) | 一个 Go TypeSafe SDK，用 Go 数据类型定义问题并读取 Jev 的选择、分数与概率。 | Go | 9 | MIT | [固定提交](https://github.com/Tangerg/typesafe-sdk-go/blob/e2f9f8353974fce1d2d2e4dd4283d5e306e8c2a8/client.go) |
| [**ajensenwaud/hermes-jev-plugin**](https://github.com/ajensenwaud/hermes-jev-plugin) | 该插件为 Hermes Agent 提供四个基于 TypeSafe Jev 的决策工具，分别用于二元判断、选项路由、评分和批量评估。 | — | 8 | MIT | 已核验 |
| [**devbackend/jevgo**](https://github.com/devbackend/jevgo) | jevgo：由业务代码定义问题，客户端负责提交 Jev 请求并解析结构化结果。 | — | 8 | MIT | 已核验 |
| [**endomorphosis/JevOps**](https://github.com/endomorphosis/JevOps) | JevOps 是一个 TypeSafe / Jev 内核，提供门控、缓存、任务网格和 Lean IR 相关模块，但本身不编写 Lean 代码。 | — | 8 | AGPL-3.0 | 已核验 |
| [**jomatsu/zod-jev**](https://github.com/jomatsu/zod-jev) | 为 Zod 校验增加语义规则，例如描述是否匹配或文本是否包含个人信息。 | TypeScript | 8 | MIT | [固定提交](https://github.com/jomatsu/zod-jev/blob/700bd256fe94541a2d21044027cc2dbf5036b396/src/judge.ts) |
| [**dougsong/jev-android**](https://github.com/dougsong/jev-android) | 这是一个 Kotlin Android UI 自动化 SDK，由 TypeSafe Jev 或 DeepSeek 从当前屏幕控件中选择操作并通过无障碍服务执行，并附带示例应用。 | — | 7 | MIT | 已核验 |
| [**gilljon/typesafe-ai-rs**](https://github.com/gilljon/typesafe-ai-rs) | 独立维护的 Rust SDK，提供异步与阻塞客户端、重试和响应元数据。 | Rust | 7 | MIT | [固定提交](https://github.com/gilljon/typesafe-ai-rs/blob/06f52208c22f63326226446926859174c538e296/src/client.rs#L78) |
| [**inanna-malick/jev-dsl**](https://github.com/inanna-malick/jev-dsl) | 一个早期 Haskell DSL，用表达式描述带标签的 Jev 问题，生成请求并解析对应答案。 | Haskell | 7 | MIT | [固定提交](https://github.com/inanna-malick/jev-dsl/blob/f16f1363b4d389d6e34f9d695fbd254ca0735f2e/scripts/example.sh) |
| [**joshmn/typesafe-sdk**](https://github.com/joshmn/typesafe-sdk) | TypeSafe System One 的社区 Ruby 客户端，默认使用 jev-latest。 | Ruby | 7 | MIT | [固定提交](https://github.com/joshmn/typesafe-sdk/blob/abde35d2ebae5d7dda900d1aa122ea5b653f1d9e/lib/typesafe/sdk/client.rb) |
| [**Kiln-AI/jev_jsonschema**](https://github.com/Kiln-AI/jev_jsonschema) | 该库将 JSON Schema 转换为 Jev 问题集，调用 SystemOne API 后再将答案解码为符合原 Schema 的 JSON。 | — | 7 | MIT | 已核验 |
| [**NicolaiLassen/open-bonsai-jev**](https://github.com/NicolaiLassen/open-bonsai-jev) | 该仓库把字母选项的选择题交给模型，并从一次前向传播的下一个 Token 分布中直接读出 Jev 风格的类型化概率判定。 | — | 7 | MIT | 已核验 |
| [**docxology/daf-jev**](https://github.com/docxology/daf-jev) | 把 Jev 常用零件装成一个 Python 工具箱：提问、批量跑样本、看校准情况，再把结果接到程序或 MCP。 | Python | 6 | MIT | [固定提交](https://github.com/docxology/daf-jev/blob/ff7b28515d7f60c9f7182b128b76b90fbfcba66f/src/daf_jev/client.py) |
| [**h0j5bz0adh0-stack/jev-pilot**](https://github.com/h0j5bz0adh0-stack/jev-pilot) | 该项目是基于 TypeSafe Jev 的自主 Agent 快速决策与仲裁安全引擎，提供候选方案选择、操作拦截、循环检测、事实核验和意图路由功能。 | — | 6 | MIT | 已核验 |
| [**scienthoon/jev-ood-calibration**](https://github.com/scienthoon/jev-ood-calibration) | 该仓库用规则生成的客服工单和三个公开基准来检验 Jev 返回概率的校准情况，并提供数据生成、评测与复现脚本及原始结果。 | — | 6 | MIT | 已核验 |
| [**Stumble/jev-go**](https://github.com/Stumble/jev-go) | 社区 Go SDK 与命令行，支持 TypeSafe 直连和 Vercel AI Gateway。 | — | 6 | MIT | [固定提交](https://github.com/Stumble/jev-go/blob/a475dc925ba68602be93f4478e1381cf5ec27ee4/client.go#L23) |
| [**thehan-co/jevriel**](https://github.com/thehan-co/jevriel) | 这是一个帮助 AI Agent 使用 TypeSafe JEV 构建决策点、升级现有 LLM 工作流并测量效果的 skill 和插件。 | — | 6 | Apache-2.0 | 已核验 |
| [**bensyverson/goodall**](https://github.com/bensyverson/goodall) | Go Agent 库中的可选 TypeSafe 包，允许把 Jev 当工具或路由判断使用，而不替代对话模型。 | Go | 5 | MIT | [固定提交](https://github.com/bensyverson/goodall/blob/a612f04a712cf6c68926b780bd98e5087c687224/typesafe/client.go) |
| [**Bring-AI/jev-numeric**](https://github.com/Bring-AI/jev-numeric) | **本质都是多叉决策树，十进制逐位解码是其中的十叉形式。** 在对齐的十进制网格上，两种表示可以对应完全相同的分支与叶节点，只是提示词不同。数字是 **Choice 选项**，不是词表 token；选项概率由 Jev 直接返回。 | — | 5 | Unknown | 已核验 |
| [**Gaurav-Gosain/jev-go**](https://github.com/Gaurav-Gosain/jev-go) | Go 版 TypeSafe System One 客户端，提供类型化问题、答案与批量调用辅助。 | Go | 5 | MIT | [固定提交](https://github.com/Gaurav-Gosain/jev-go/blob/c9867e4afad0ddfaf4b9deb31038218495712fd0/client.go#L20) |
| [**gudcks0305/jev-java**](https://github.com/gudcks0305/jev-java) | 该项目是 TypeSafe Jev、OpenRouter 和 Vercel AI Gateway 的非官方 Java SDK，可将应用状态作为 Choice、Noul 和 Score 类型化问题批量提交并返回类型化 Jev 判断结果，同时提供 Spring Boot 自动配置和 WebClient 传输支持。 | — | 5 | MIT | 已核验 |
| [**jamesward/zio-typesafe-ai**](https://github.com/jamesward/zio-typesafe-ai) | Scala 3 / ZIO 的 Jev 客户端：用 NamedTuple 一次提交多个 Noul、Choice、Score，答案按同样字段名返回。 | Scala | 5 | Apache-2.0 | [固定提交](https://github.com/jamesward/zio-typesafe-ai/blob/38082e8712b49ce239ae628557619347909165dc/src/main/scala/com/jamesward/zio_typesafe_ai/TypeSafeAI.scala#L1-L571) |
| [**kataras/jev**](https://github.com/kataras/jev) | jev：由业务代码定义问题，客户端负责提交 Jev 请求并解析结构化结果。 | — | 5 | MIT | 已核验 |
| [**luigivis/jev-sdk-java**](https://github.com/luigivis/jev-sdk-java) | jev-sdk-java：由业务代码定义问题，客户端负责提交 Jev 请求并解析结构化结果。 | — | 5 | MIT | 已核验 |
| [**nitoba/questions**](https://github.com/nitoba/questions) | TypeScript 决策库：用 Zod 或原生问题描述判断，默认请求 TypeSafe Jev，也可改用 Vercel 或生成式适配器。 | TypeScript | 5 | MIT | [固定提交](https://github.com/nitoba/questions/blob/37501199437e3f3be11e185c157d30fa7a00601a/src/providers/typesafe.ts) |
| [**noplan-inc/limpet**](https://github.com/noplan-inc/limpet) | 编程智能体专用 Stop Hook 门禁：防止 Coding Agent 过早宣布完工，用 Jev 依据自然语言规则客观裁定完成度。 | — | 5 | MIT | 已核验 |
| [**nshkrdotcom/typesafe_sdk**](https://github.com/nshkrdotcom/typesafe_sdk) | 面向 Elixir 的 TypeSafe SDK，把 Jev 的类型化问题与概率答案接到 Elixir 应用。 | Elixir | 5 | MIT | [固定提交](https://github.com/nshkrdotcom/typesafe_sdk/blob/deaedd63882045ea0d8e9273002280a20809e170/lib/typesafe_sdk/generated/system_one.ex) |
| [**replynodes/jev-web-analyzer**](https://github.com/replynodes/jev-web-analyzer) | jev-web-analyzer：由业务代码定义问题，客户端负责提交 Jev 请求并解析结构化结果。 | — | 5 | Apache-2.0 | 已核验 |
| [**sumanmichael/jevlang**](https://github.com/sumanmichael/jevlang) | 该项目为 Python 提供 .jev 语言扩展，将 ~ 提问和 jev/case 分支在导入时改写为对 TypeSafe Jev 分类器的调用。 | — | 5 | MIT | 已核验 |
| [**virolea/jev**](https://github.com/virolea/jev) | 该 Gem 是 Typesafe Jev 模型 API 的 Ruby 客户端，可在一次查询中并行提出多个问题并读取 noul、choice 和 score 类型的答案。 | — | 5 | MIT | 已核验 |
| [**ajanm007/jevrag**](https://github.com/ajanm007/jevrag) | 该项目为 RAG 流程提供可插拔的决策层，通过统一的 state → Decision → confidence → action 接口实现检索停止、分块、上下文选择、回答拒答和缓存信任五类决策，并以 Jev 作为首个可替换后端，同时提供校准评估工具。 | — | 4 | MIT | 已核验 |
| [**Rajmeet/jev-phone**](https://github.com/Rajmeet/jev-phone) | jev-phone：由业务代码定义问题，客户端负责提交 Jev 请求并解析结构化结果。 | — | 4 | MIT | 已核验 |
| [**typakon4/jev-layer**](https://github.com/typakon4/jev-layer) | jev-layer 只负责路由有界决策并记录证据；host 保留执行、权限、审批、重试、恢复和最终结果的所有权。 | — | 4 | MIT | 已核验 |
| [**waynesutton/ask-jev-ai**](https://github.com/waynesutton/ask-jev-ai) | ask-jev-ai：由业务代码定义问题，客户端负责提交 Jev 请求并解析结构化结果。 | — | 4 | Unknown | 已核验 |
| [**ZTRRTUO/Jev-PhoneControl**](https://github.com/ZTRRTUO/Jev-PhoneControl) | **v0.0.1 · 源码可见的 Android 视觉控制原型。** 输入任务指令后，系统观察手机截图、规划下一步，再通过 JEV 从候选动作中做判断，最后由 ADB 执行。项目包含本地网页和后台 API。 | — | 4 | Unknown | 已核验 |
| [**ArmanJR/Jev-Persian-Benchmark**](https://github.com/ArmanJR/Jev-Persian-Benchmark) | Jev-Persian-Benchmark：由业务代码定义问题，客户端负责提交 Jev 请求并解析结构化结果。 | — | 3 | Unknown | 已核验 |
| [**codeitlikemiley/typesafe-sdk-rust**](https://github.com/codeitlikemiley/typesafe-sdk-rust) | TypeSafe API 的 Rust 客户端，提供异步与可选阻塞调用，以及带类型的问题和答案封装。 | Rust | 3 | MIT | [固定提交](https://github.com/codeitlikemiley/typesafe-sdk-rust/blob/e7050df6baa611bc9088f1a361b4b90e8571929d/src/client.rs) |
| [**collapseindex/jev-builder**](https://github.com/collapseindex/jev-builder) | 这是一个在浏览器中填写文本和问题来生成 Jev 请求、复制请求并多次运行查看答案稳定性的表单工具。 | — | 3 | Unknown | 已核验 |
| [**GenieRobot/typesafe-ai-rails**](https://github.com/GenieRobot/typesafe-ai-rails) | Ruby on Rails 官方风格集成插件，为 ActiveModel/ActiveRecord 模型引入 Jev 分类、评分与决策策略支持。 | Ruby | 3 | MIT | [固定提交](https://github.com/GenieRobot/typesafe-ai-rails/blob/fbac64470904fef7c4e68da172813daf0840f31f/lib/typesafe/rails/client.rb#L1-L148) |
| [**getainode/jebadiah**](https://github.com/getainode/jebadiah) | 该仓库提供开放 System One 决策模型 Jebadiah 的训练器、数据构建工具、评测工具以及全部运行配置与结果记录。 | — | 3 | Apache-2.0 | 已核验 |
| [**jvsteiner/jevex**](https://github.com/jvsteiner/jevex) | Jev 指挥工具循环的 Agent 实验，聊天模型负责参数与最终文字，MCP 工具执行操作。 | Python | 3 | MIT | [固定提交](https://github.com/jvsteiner/jevex/blob/dd22ffd958d56ad118bb6dd585f1c913c96c5fd3/src/jevex/jev.py) |
| [**KantaHayashiAI/jev-does-not-play-dice**](https://github.com/KantaHayashiAI/jev-does-not-play-dice) | 该项目对公平随机事件和预测文档上Jev概率输出的可复现离线评测与校准分析。 | — | 3 | MIT | 已核验 |
| [**laguagu/jev-skills**](https://github.com/laguagu/jev-skills) | 该仓库为使用 Jev 构建应用的 Agent 提供实用技能与示例，涵盖 API 设置、决策模式、路由、排序与证据检查。 | — | 3 | MIT | 已核验 |
| [**legacybridge-tech/pi-typesafe-jev**](https://github.com/legacybridge-tech/pi-typesafe-jev) | 为 Pi 扩展注入 TypeSafe Jev 的 5 种窄域判断工具：把决策权交给模型的同时将动作阈值保留给宿主应用。 | — | 3 | Unknown | 已核验 |
| [**nanami-0713/dsh-jev-decide**](https://github.com/nanami-0713/dsh-jev-decide) | DSH plugin: register TypeSafe Jev (System One decision model) as an agent tool — jev_decide returns calibrated probabilities (noul/choice/score) for routing/triage/guardrail jud… | — | 3 | MIT | 已核验 |
| [**qingshungLI/everything-about-jev**](https://github.com/qingshungLI/everything-about-jev) | 这里整理了 Jev 的使用方法、示例代码、社区项目和讨论。如果你刚听说这个模型，可以先读下面的介绍，再选一个 demo 跑起来。 | — | 3 | MIT | 已核验 |
| [**SoundBlaster/Jev4Mellea**](https://github.com/SoundBlaster/Jev4Mellea) | 这是一个将 Jev 语义检查接入 Mellea 的 Python 适配器，用于验证文本、分类文本或按有序量表评分。 | — | 3 | Apache-2.0 | 已核验 |
| [**YidiDev/jev-benchmark**](https://github.com/YidiDev/jev-benchmark) | 该仓库提供基于评分规则的零样本分类、链式决策执行和考试评分基准，用于比较 Jev、Claude 和 OpenJev 并跟踪价格。 | — | 3 | MIT | 已核验 |
| [**yzxoi/RSI-Jev-Slay-the-Spire-2**](https://github.com/yzxoi/RSI-Jev-Slay-the-Spire-2) | 这是一个公开的、以证据驱动的《杀戮尖塔 2》智能体实验仓库。目标是用确定性计算处理规则与风险，让廉价的 Jev 做大量选择，只在关键且不确定的局面调用 Astra，最终提高多角色、高进阶的整局胜率。 | — | 3 | Unknown | 已核验 |
| [**zhirschtritt/typesafe-go**](https://github.com/zhirschtritt/typesafe-go) | 无第三方依赖的非官方 Go 客户端，支持 System One 请求和模型列表。 | Go | 3 | MIT | [固定提交](https://github.com/zhirschtritt/typesafe-go/blob/a4062e525d1ad23aa739d3454247bcec52486a57/client.go#L18) |
| [**2389-research/typesafe-go**](https://github.com/2389-research/typesafe-go) | 只依赖 Go 标准库的 TypeSafe System One 客户端，用于提交 Jev 问题并读取结构化答案。 | Go | 2 | MIT | [固定提交](https://github.com/2389-research/typesafe-go/blob/1f9ac50bab4921862327dadc45871bc24b381b3e/typesafe.go) |
| [**AboveColin/jevclient**](https://github.com/AboveColin/jevclient) | Jev 的异步 Python 客户端，一次请求可提交多个结构化判断问题。 | Python | 2 | MIT | [固定提交](https://github.com/AboveColin/jevclient/blob/d568f25717c5b956022f5dc0fcfcb905c7533a05/jevclient/client.py) |
| [**Butochnikov/typesafe-sdk-php**](https://github.com/Butochnikov/typesafe-sdk-php) | 面向 PHP 8.2+ 的社区 TypeSafe SDK，提供同步调用与基于 Guzzle 的异步请求。 | PHP | 2 | MIT | [固定提交](https://github.com/Butochnikov/typesafe-sdk-php/blob/d44db82dbf4ff601b123731b517fba1ca9092278/src/TypeSafeClient.php#L32) |
| [**fgn/jevgo**](https://github.com/fgn/jevgo) | 社区 Go 客户端，核心只依赖标准库，另有可选 Langfuse 追踪模块。 | — | 2 | MIT | [固定提交](https://github.com/fgn/jevgo/blob/ff7a543dda89cbd93e44d6d6535b1a7a62ffb882/client.go#L18) |
| [**g0runmezadam/jev-architecture-research**](https://github.com/g0runmezadam/jev-architecture-research) | 该仓库是针对 Jev 决策模型的黑盒逆向工程研究档案，整理实验记录、证据矩阵与架构分析文档。 | — | 2 | MIT | 已核验 |
| [**hamakyo/jev-starter**](https://github.com/hamakyo/jev-starter) | 在 TypeSafe SDK 上补充决策阈值、备用路径、人工复核和评测模式的 TypeScript 工具集。 | — | 2 | MIT | [固定提交](https://github.com/hamakyo/jev-starter/blob/fb0fae07d1f3052f28af630b942c16b2a7bd8c88/src/providers/jev-provider.ts#L43) |
| [**ItBayMax/typesafe-ai-jev-example**](https://github.com/ItBayMax/typesafe-ai-jev-example) | 想快速搞明白「System One 模型到底怎么用」「值不值得接进我的项目」， 从这里开始比读文档快。 | — | 2 | MIT | 已核验 |
| [**olivier-motium/jev-doom**](https://github.com/olivier-motium/jev-doom) | jev-doom：由业务代码定义问题，客户端负责提交 Jev 请求并解析结构化结果。 | — | 2 | MIT | 已核验 |
| [**qddegtya/qualm**](https://github.com/qddegtya/qualm) | TypeScript 的 Jev 判断封装，把不确定结果作为显式 unsure 分支处理。 | TypeScript | 2 | MIT | [固定提交](https://github.com/qddegtya/qualm/blob/e1aacf6844f312ba95eb6a1bd26fad15575a7173/src/provider.ts) |
| [**rajivkuriakose/typesafe-jev-examples**](https://github.com/rajivkuriakose/typesafe-jev-examples) | 该仓库提供通过 OpenRouter 调用 Jev 完成工单分类和文章重排序的可运行示例。 | — | 2 | MIT | 已核验 |
| [**ReallyArtificial/jev-by-example**](https://github.com/ReallyArtificial/jev-by-example) | 该仓库提供十个可运行的 JavaScript 示例，用小型 Jev 判断结合应用逻辑演示 Agent 决策。 | — | 2 | MIT | 已核验 |
| [**SamratDuttaOfficial/WaterSheep**](https://github.com/SamratDuttaOfficial/WaterSheep) | 开源权重的 Jev 兼容服务端，本地提供 /v1/systemone 决策接口与多原语概率推理。 | — | 2 | Apache-2.0 | 已核验 |
| [**Solido/jev_dart**](https://github.com/Solido/jev_dart) | 这是 Jev 的纯 Dart 客户端，用于发送状态和类型化问题并返回可供代码分支的结构化答案，可用于 CLI、服务端和 Flutter 应用。 | — | 2 | MIT | 已核验 |
| [**0xjba/jev-swap**](https://github.com/0xjba/jev-swap) | jev-swap：由业务代码定义问题，客户端负责提交 Jev 请求并解析结构化结果。 | — | 1 | MIT | 已核验 |
| [**AbdelStark/typesafe-rs**](https://github.com/AbdelStark/typesafe-rs) | Jev 的社区 Rust 客户端，支持异步请求、可选阻塞接口及本地 mock 测试。 | Rust | 1 | MIT | [固定提交](https://github.com/AbdelStark/typesafe-rs/blob/8e8b7a2ae1af5bf7d3e5d831e634fdf328b2fbcc/crates/typesafe-rs/src/client.rs) |
| [**ajayk/jev-go-sdk**](https://github.com/ajayk/jev-go-sdk) | jev-go-sdk：由业务代码定义问题，客户端负责提交 Jev 请求并解析结构化结果。 | — | 1 | Apache-2.0 | 已核验 |
| [**anilsenay/jev**](https://github.com/anilsenay/jev) | jev：由业务代码定义问题，客户端负责提交 Jev 请求并解析结构化结果。 | — | 1 | MIT | 已核验 |
| [**ashafizullah/jev-triage**](https://github.com/ashafizullah/jev-triage) | jev-triage：由业务代码定义问题，客户端负责提交 Jev 请求并解析结构化结果。 | — | 1 | MIT | 已核验 |
| [**chrishan17/claude-jev-mod**](https://github.com/chrishan17/claude-jev-mod) | 1. 在 `~/.claude/settings.json` 的 `env` 里打开函数式 hooks：    `"CLAUDE_CODE_ENABLE_FUNCTION_HOOKS": "1"` 2. 会话里执行： 3. 在同一个 `env` 块里填上你手上任意一家的密钥（上表任选一行），重启 Claude Code。 | — | 1 | MIT | 已核验 |
| [**cole-gillespie/typesafe-go**](https://github.com/cole-gillespie/typesafe-go) | 非官方 Go SDK，支持类型化答案、重试和 context 取消。 | Go | 1 | MIT | [固定提交](https://github.com/cole-gillespie/typesafe-go/blob/188247d639e8aacecd7a0d1aceaf8a4c66f8fa57/client.go#L21) |
| [**copyleftdev/jev-labs**](https://github.com/copyleftdev/jev-labs) | 该项目在 Jev 周围构建共识内核，用 5 个 Agent 投票、稳定性门限和 quorum 机制对药房场景做出决定或升级，并包含 TLA+ 规约、Rust 内核与仿真工具。 | — | 1 | MIT | 已核验 |
| [**guillemus/jev-go**](https://github.com/guillemus/jev-go) | 接口精简的非官方 Go SDK，可调用 Jev 并列出可用模型。 | — | 1 | Unknown | [固定提交](https://github.com/guillemus/jev-go/blob/06df95fe081e8b05bf4c0db8292ceefd995fee84/jev.go#L18) |
| [**hemanth/jevish**](https://github.com/hemanth/jevish) | jevish 是一个 JavaScript 语义模式匹配与零样本判断库，使用 Jev 的 Choice 做标签分类、使用 Noul 做布尔判定，并支持本地与云端 Jev 协同执行。 | — | 1 | MIT | 已核验 |
| [**hnegishi/typesafe-ai-ruby**](https://github.com/hnegishi/typesafe-ai-ruby) | 无第三方运行时依赖的 Ruby 客户端，把 Choice / Score / Noul 发到 TypeSafe System One。 | Ruby | 1 | MIT | [固定提交](https://github.com/hnegishi/typesafe-ai-ruby/blob/4ab8c243fbd9e9d5526b59186595d0534785d963/lib/typesafe/client.rb) |
| [**ItzSupra13/jev-is-not-odd**](https://github.com/ItzSupra13/jev-is-not-odd) | jev-is-not-odd：由业务代码定义问题，客户端负责提交 Jev 请求并解析结构化结果。 | — | 1 | Unknown | 已核验 |
| [**JGalego/Jevs-Garage**](https://github.com/JGalego/Jevs-Garage) | 该仓库收录多个小型可查看示例，用 Jev 把现实状态转为类型化判断，再由 Python 策略决定下一步操作。 | — | 1 | Unknown | 已核验 |
| [**JYeswak/jev_playground**](https://github.com/JYeswak/jev_playground) | 该仓库用 Jev 对给定状态做类型化提问并返回概率与置信度，提供二十个可一键运行的示例、统一失败处理的客户端封装和可复算的测量记录，用于判断哪些场景值得用模型分数驱动代码。 | — | 1 | MIT | 已核验 |
| [**litshing/jevcore**](https://github.com/litshing/jevcore) | JEV core 是向 Jev 发起有界批量判断请求的纯标准库客户端，包含成本守卫、缓存、校准、Harness 与命令行工具。 | — | 1 | Unknown | 已核验 |
| [**llt22/jev-lab**](https://github.com/llt22/jev-lab) | Jev 把自然语言状态转换成带类型的决策：**Noul** 做是/否判断，**Choice** 从候选项中选择，**Score** 做有序评分。本仓库既是 Jev 生态导航，也是一个独立实验室，提供原始数据、负面结果和完整复现脚本。 | — | 1 | Unknown | 已核验 |
| [**marandaneto/typesafe-sdk-swift**](https://github.com/marandaneto/typesafe-sdk-swift) | 使用 Swift Package Manager、Swift 并发和 URLSession 调用 TypeSafe 的实验性 Swift SDK。 | Swift | 1 | MIT | [固定提交](https://github.com/marandaneto/typesafe-sdk-swift/blob/5a8565791b56d6ba874de9f7ea206b8a1a53c794/Sources/TypeSafe/TypeSafeClient.swift) |
| [**proshunsuke/jev-tab-order**](https://github.com/proshunsuke/jev-tab-order) | jev-tab-order：由业务代码定义问题，客户端负责提交 Jev 请求并解析结构化结果。 | — | 1 | MIT | 已核验 |
| [**q93304989-bit/jev-lab**](https://github.com/q93304989-bit/jev-lab) | 最简 Jev 调用演示器：单页分类器，把请求 JSON、概率分布、confidence、耗时与 token 都摊开给你看 | — | 1 | MIT | 已核验 |
| [**royalpinto007/jev-msw**](https://github.com/royalpinto007/jev-msw) | 该仓库为 Jev API 提供基于 MSW 的模拟处理器，让测试无需真实请求即可确定性地返回决策结果。 | — | 1 | MIT | 已核验 |
| [**Sanoy24/jevpolicy**](https://github.com/Sanoy24/jevpolicy) | JevPolicy 是一个 TypeScript 决策运行时，它把来自 Jev 的概率性判断转换为版本化、确定性、可重放且可观测的应用决策。 | — | 1 | Apache-2.0 | 已核验 |
| [**zerodegress/jevinf**](https://github.com/zerodegress/jevinf) | Jev 这一系决策模型的推理引擎：每条候选路径按分段前向计算并复用前缀，上面架一层符合 Jev wire 契约的服务。目前接上的后端是 NanoJev。 | — | 1 | MIT | 已核验 |
| [**DotNetVibeCoderz/Vibe_SDK**](https://github.com/DotNetVibeCoderz/Vibe_SDK) | 非官方 .NET 客户端向 TypeSafe `/v1/systemone` 发送 state 与 typed questions；父仓库还混有与 Jev 无关的 SDK。 | C# | 0 | MIT | [固定提交](https://github.com/DotNetVibeCoderz/Vibe_SDK/blob/09c77029c00df6aa707b059e560512f17896b059/TypeSafeSDK/TypeSafeSdk/TypeSafeClient.cs) |

## SDK & Integrations

| 项目 | 简介 | 语言 | ⭐ | 许可证 | 证据 |
|---|---|---:|---:|---:|---|
| [**langchain-ai/langchain**](https://github.com/langchain-ai/langchain) | 给 Python LangChain 流程加一个可选 Jev 分类节点，返回类别、概率和等级评分。 | Python | 147387 | MIT | [固定提交](https://github.com/langchain-ai/langchain/blob/eba445b7563d1709427bd8072892975a6ea59fdc/libs/partners/typesafe/langchain_typesafe/classifier.py) |
| [**pydantic/pydantic-ai**](https://github.com/pydantic/pydantic-ai) | Pydantic AI 的可选 Jev 模型：把输出模型里的布尔和枚举字段变成问题，拿回符合类型的判断。 | Python | 20362 | MIT | [固定提交](https://github.com/pydantic/pydantic-ai/blob/c4898abb54dc25ae6f6aef208a4c0661b30a455e/pydantic_ai_slim/pydantic_ai/models/typesafe.py) |
| [**ax-llm/ax**](https://github.com/ax-llm/ax) | Ax 框架提供 TypeSafe 接口，可用布尔或有限类别签名调用 Jev，也可读原生答案。 | — | 2958 | Apache-2.0 | [固定提交](https://github.com/ax-llm/ax/blob/5c43344f9ef3016db576fa2c3b59d48ef21b4d71/src/ax/ai/typesafe/client.ts#L1) |
| [**kieranklaassen/ruby_llm-typesafe**](https://github.com/kieranklaassen/ruby_llm-typesafe) | 为 RubyLLM 2 添加 TypeSafe provider，通过结构化输出接口调用 Jev 的三类判断。 | Ruby | 18 | MIT | [固定提交](https://github.com/kieranklaassen/ruby_llm-typesafe/blob/33e680115a43d584b1c0dcff385816f459a4bc71/lib/ruby_llm/providers/typesafe.rb) |
| [**Butochnikov/laravel-typesafe-jev**](https://github.com/Butochnikov/laravel-typesafe-jev) | 把 Jev 接入 Laravel，提供配置、依赖注入、Facade 和可记录请求的测试替身。 | PHP | 3 | MIT | [固定提交](https://github.com/Butochnikov/laravel-typesafe-jev/blob/4d70f5e1b059aac2f63105e72626802247a51f45/src/Jev.php) |
| [**Vicente-MD/jev-resilience**](https://github.com/Vicente-MD/jev-resilience) | 给 Spring WebFlux 检查“HTTP 200 但正文其实报错”的响应。 | Java | 2 | Unknown | [固定提交](https://github.com/Vicente-MD/jev-resilience/blob/c490e0dc7830758f84bd9d5acb806655e327113e/src/main/java/ai/jev/resilience/client/JevEvaluationService.java) |

## Security & Guardrails

| 项目 | 简介 | 语言 | ⭐ | 许可证 | 证据 |
|---|---|---:|---:|---:|---|
| [**agentgateway/agentgateway**](https://github.com/agentgateway/agentgateway) | Agentgateway 仓库里的 Jev 护栏示例，通过 webhook 检查模型请求和回复。 | Rust | 5144 | Apache-2.0 | [固定提交](https://github.com/agentgateway/agentgateway/blob/6b0270efd25b5255932943e48b5ca47583d3ad28/examples/llm-guardrail-jev/guardrail.ts) |
| [**AgentiLoop/Agent**](https://github.com/AgentiLoop/Agent) | 原生 macOS Agent 内的可选 Jev 命令风险顾问，配有 TypeSafeKit 客户端。 | Swift | 640 | Unknown | [固定提交](https://github.com/AgentiLoop/Agent/blob/078f87ceca1d1190cc73706ac8ec16442e766a27/Agent/Services/JevAdvisor.swift) |
| [**dabit3/jev-experiments**](https://github.com/dabit3/jev-experiments) | 一组 Jev 开发工具实验，其中 Commit Sentry 对暂存 diff 的片段进行语义风险检查。 | TypeScript | 396 | Unknown | [固定提交](https://github.com/dabit3/jev-experiments/blob/ed07e87c24822b9258dfd95c63e3d5f436d95b1a/commit-sentry/src/jev.ts) |
| [**kitze/unclutter**](https://github.com/kitze/unclutter) | 用 Jev 帮浏览器扩展识别网页中的广告、促销与订阅弹窗，并保存可复用的隐藏规则。 | TypeScript | 348 | MIT | [固定提交](https://github.com/kitze/unclutter/blob/9ef9beccc1e57b4e3115ae68644b8fc9c19c29f6/lib/jev.ts) |
| [**QuentinCody/interlinked-cli**](https://github.com/QuentinCody/interlinked-cli) | Interlinked 在编程 Agent 的本地检查之外，提供可选 Jev 判断与证据检查。 | — | 177 | MIT | [固定提交](https://github.com/QuentinCody/interlinked-cli/blob/207330d8131c5203ecc74e9fd4c24ba416463718/src/harness/jev/client.ts#L14) |
| [**DevMortimer/pi-warden**](https://github.com/DevMortimer/pi-warden) | 给 Pi Agent 加项目规则、越界操作、重复失败和完成声明的检查。 | TypeScript | 156 | MIT | [固定提交](https://github.com/DevMortimer/pi-warden/blob/e6c801679464b1a9624225114eb5fb443c27d823/src/guard.ts) |
| [**y0usaf/pi-jev**](https://github.com/y0usaf/pi-jev) | Pi 编码 Agent 扩展：执行前提示工具风险，执行后检查秘密泄露与失败类型。 | TypeScript | 154 | MIT | [固定提交](https://github.com/y0usaf/pi-jev/blob/b3478fd4ca1ac8ffcb703f6dc8d6069b555f531e/src/client.ts) |
| [**aaddrick/building-with-typesafe-jev**](https://github.com/aaddrick/building-with-typesafe-jev) | 把 Jev 的结构化判断接进程序；具体用途与决策流程请查看项目源码。 | — | 127 | MIT | 已核验 |
| [**openlayer-ai/jevals**](https://github.com/openlayer-ai/jevals) | 把 Jev 的结构化判断接进程序；具体用途与决策流程请查看项目源码。 | — | 103 | MIT | 已核验 |
| [**CaptainCore/captaincore**](https://github.com/CaptainCore/captaincore) | WordPress 运维工具 CaptainCore 的 Jev 命令，可询问结构化问题，并给恶意代码扫描结果排复核优先级。 | Go | 74 | MIT | [固定提交](https://github.com/CaptainCore/captaincore/blob/f54e0669350707b2f4f4c67a0130fdd6574bd0b5/cmd/typesafe.go) |
| [**jonathanavis96/jev-kit**](https://github.com/jonathanavis96/jev-kit) | 该仓库为 Claude Code 提供运行 TypeSafe 的 Jev 所需的工具调用防护、Tier Guard、文件搜索、浏览器 Agent、代码评审、复核与压缩等组件及安装器。 | — | 55 | MIT | 已核验 |
| [**leepokai/jev-guard**](https://github.com/leepokai/jev-guard) | 在编程 Agent 调工具前后加一道检查：操作是否危险、是不是用户要求的、返回内容里有没有诱导 Agent 越界的指令。 | JavaScript | 53 | MIT | [固定提交](https://github.com/leepokai/jev-guard/blob/94996ea80b6b308327ac2077706a29ce6abd3ba0/src/jev.js) |
| [**brainstormity/Jev-Moderation-Bot**](https://github.com/brainstormity/Jev-Moderation-Bot) | 一个 Discord 审核机器人，让 Jev 检查垃圾消息和诈骗链接，并按本地规则逐级警告或禁言。 | Python | 46 | MIT | [固定提交](https://github.com/brainstormity/Jev-Moderation-Bot/blob/1629ac80bea758883ee7541ffc654c83acfae4b6/typesafe/__init__.py) |
| [**kiwi0719/jev-edge**](https://github.com/kiwi0719/jev-edge) | 该项目是在 nginx/OpenResty 等网关入口处运行的三层请求过滤器，用 TypeSafe Jev 判断提示注入和滥用，并具备 fail-open、缓存和热更新能力。 | — | 41 | Apache-2.0 | 已核验 |
| [**luantak/is-malicious**](https://github.com/luantak/is-malicious) | 命令行代码库恶意行为扫描器，在运行未知代码前利用 Jev 分析源码、CI 配置与构建脚本的可疑行为。 | TypeScript | 32 | MIT | [固定提交](https://github.com/luantak/is-malicious/blob/b6052465eb47cf85f347596385954aa06532718a/src/jev.ts#L1-L181) |
| [**jomatsu/pi-jev-auto-mode**](https://github.com/jomatsu/pi-jev-auto-mode) | 给 Pi 的命令和文件操作增加规则检查，再由 Jev 评估需要进一步判断的操作。 | TypeScript | 30 | MIT | [固定提交](https://github.com/jomatsu/pi-jev-auto-mode/blob/06a56043088124ed650471a8589fddd8139708f4/src/jev/transport.ts) |
| [**anpicasso/hermes-jev-approvals**](https://github.com/anpicasso/hermes-jev-approvals) | Hermes 的实验性命令审批插件，只替换 auxiliary.approval 判断任务。 | Python | 19 | MIT | [固定提交](https://github.com/anpicasso/hermes-jev-approvals/blob/c41d81de23a79d8d69397cef81c4de99b3f987c5/plugin/__init__.py) |
| [**PanAchy/jevvy**](https://github.com/PanAchy/jevvy) | 为 OpenCode 等编码Agent自动放行无害的 shell 命令，对不确定命令保留人工审核。 | — | 19 | MIT | 已核验 |
| [**dark-hxx/jev-safety-gateway**](https://github.com/dark-hxx/jev-safety-gateway) | 位于 nginx 与大模型后端之间的前置过滤反向代理：逐请求提取用户输入交给 JEV 判定，有害拦截、正常透明放行 | — | 13 | AGPL-3.0 | 已核验 |
| [**harshwasan/pi-jev-sentinel**](https://github.com/harshwasan/pi-jev-sentinel) | 这是一个 Pi coding-agent 扩展，用 Jev 检查工具调用的意图和风险，并筛查工具输出和回复中的注入指示，同时隐去密钥后再发送。 | — | 12 | MIT | 已核验 |
| [**win4r/jev-security-scan**](https://github.com/win4r/jev-security-scan) | 输出文件和行号、脱敏后的证据、风险类别、模型概率及未扫描范围。支持 Codex、Claude Code，也可以作为独立 Python 命令行工具使用。 | — | 12 | MIT | 已核验 |
| [**codejunkie99/jev-engineering**](https://github.com/codejunkie99/jev-engineering) | 该仓库提供关于在 Agent 工作流中使用 Jev 类型化决策的技术论文、图表和离线示例，说明观察、模型判断、确定性策略与结果验证的分离。 | — | 10 | Unknown | 已核验 |
| [**HexyeDEV/JevPR**](https://github.com/HexyeDEV/JevPR) | JevPR 是一个 GitHub App，它接收拉取请求 webhook 并把整理后的上下文发送给 Jev，再根据返回的 LOW、NORMAL 或 SPECIALIST 等决策映射为批准、请求评审或更新检查等操作。 | — | 10 | Apache-2.0 | 已核验 |
| [**caiovicentino/jev-risk-check-provider**](https://github.com/caiovicentino/jev-risk-check-provider) | 把 Jev 的结构化判断接进程序；具体用途与决策流程请查看项目源码。 | — | 9 | MIT | 已核验 |
| [**erkamyaman/jev-enforce**](https://github.com/erkamyaman/jev-enforce) | jev-enforce：Jev 针对每条 CLAUDE.md 规则判定当前回复或代码编辑是否违反该规则。 | — | 9 | MIT | 已核验 |
| [**metalbear-co/jev-auto-approve**](https://github.com/metalbear-co/jev-auto-approve) | 这是一个 GitHub Action，调用 Jev 并行询问多个是否问题，仅当所有置信度达标时自动批准 PR，否则跳过并评论分数。 | — | 9 | MIT | 已核验 |
| [**zhangxaochen/dsh-jev**](https://github.com/zhangxaochen/dsh-jev) | 它补上 dsh 自己没有的那一层语义判断：引入 ~150ms 极低延迟的非生成式决策原语（Noul、Choice、Score），做**动态工具剪枝**（省 Prompt Token、降首字延迟）、**语义死循环阻断**与**高危执行安全门禁**。判定走 System One 而非生成式采样，所以快、可复现，且成本可忽略：**每次判定 ≈ $0.0001… | — | 9 | MIT | 已核验 |
| [**JoaquinRuiz/medula**](https://github.com/JoaquinRuiz/medula) | medula：对输入文本做分类或打分，交给本地规则继续处理。 | — | 8 | MIT | 已核验 |
| [**anisselbd/jev-phishing-bench**](https://github.com/anisselbd/jev-phishing-bench) | jev-phishing-bench：Jev 负责判断每封邮件是否为钓鱼邮件、链接是否可点击，并对五个钓鱼信号给出概率。 | — | 7 | Unknown | 已核验 |
| [**muratcakmak/jev-guard**](https://github.com/muratcakmak/jev-guard) | 把 Jev 的结构化判断接进程序；具体用途与决策流程请查看项目源码。 | — | 7 | MIT | 已核验 |
| [**ufec/jev-block-android-ad**](https://github.com/ufec/jev-block-android-ad) | Android 通知与短信过滤实验：先执行本地验证码等规则，再让 Jev 判断消息是否是广告噪声。 | Kotlin | 7 | MIT | [固定提交](https://github.com/ufec/jev-block-android-ad/blob/8da22d212a3392468686d21a020eb8ae06afe320/core/decision/src/commonMain/kotlin/me/ethanxu/jevnoisegate/core/decision/TypeSafeBackend.kt) |
| [**HyunjunJeon/jev-judgment**](https://github.com/HyunjunJeon/jev-judgment) | 给编程 Agent 增加授权、操作风险和失败原因的判断检查。 | Python | 6 | MIT | [固定提交](https://github.com/HyunjunJeon/jev-judgment/blob/f6056e7cd31d467d6773a0737731c85939499e5e/skills/jev-judgment/scripts/jev.py) |
| [**andrelandgraf/safer-with-jev**](https://github.com/andrelandgraf/safer-with-jev) | 给 HTTP 请求装一道内容门禁。Jev 先检查注入指令或不安全内容，通过了再转发到指定地址。 | TypeScript | 5 | Unknown | [固定提交](https://github.com/andrelandgraf/safer-with-jev/blob/b4fb82b129caa46480de6a66387ea2ff053c6511/src/lib/judge.ts) |
| [**eugeniughelbur/jev-engineering**](https://github.com/eugeniughelbur/jev-engineering) | 该项目提供基于 Jev 的工具调用门禁和评审路由等示例，根据输入内容决定放行、拦截或提示确认。 | — | 5 | MIT | 已核验 |
| [**ickma2311/jev-baselines-eval**](https://github.com/ickma2311/jev-baselines-eval) | 把 Jev 的结构化判断接进程序；具体用途与决策流程请查看项目源码。 | — | 5 | MIT | 已核验 |
| [**kaustav1996/reflex**](https://github.com/kaustav1996/reflex) | 这是一个基于 Pi coding Agent 的编码助手与个人助理，Jev 会检查每次工具调用、对话轮次和语音转录，代码据此决定放行、询问或拦截、选择模型档位并核验完成状态。 | — | 5 | MIT | 已核验 |
| [**NicolasMontone/jev-tool-permissions**](https://github.com/NicolasMontone/jev-tool-permissions) | 为 Vercel AI SDK 提供工具调用审批与工具列表筛选。 | TypeScript | 5 | Unknown | [固定提交](https://github.com/NicolasMontone/jev-tool-permissions/blob/4c57dd6b0251213353ca01ec74e2a44e04fa42e0/src/gate.ts) |
| [**Reindeer-AI/pi-jev-guard**](https://github.com/Reindeer-AI/pi-jev-guard) | 该 Pi 扩展在写入前使用 TypeSafe Jev 检查提议的代码修改是否违反 Markdown 规则，并返回违规规则原文与行号范围。 | — | 5 | Unknown | 已核验 |
| [**carlosedm10/agi-jev-containment**](https://github.com/carlosedm10/agi-jev-containment) | 该项目是本地 Agent 监控栈，用 Jev 和 Sentinel 对工具调用链评分并触发只升级的 L1–L5 处置，同时将事件存入 Neo4j 并在 AngryRobot 仪表盘展示。 | — | 4 | Unknown | 已核验 |
| [**lgy1027/jevshield**](https://github.com/lgy1027/jevshield) | 该项目是基于 Jev 的 Agent 工具调用安全门，通过单次 Choice/Noul/Score 评估拦截高风险操作，并提供本地启发式兜底和 LangChain 集成。 | — | 4 | Apache-2.0 | 已核验 |
| [**Thanh-Mathieu95/jev-model-tokengate**](https://github.com/Thanh-Mathieu95/jev-model-tokengate) | 该项目是一个 OpenAI 兼容的流式代理，在Token到达用户前用滑动缓冲加并行评估进行拦截，实现零泄漏的内容过滤。 | — | 4 | MIT | 已核验 |
| [**alexj11324/open-jev-approvals**](https://github.com/alexj11324/open-jev-approvals) | agent 要执行工具时，hook 会拦住这次调用，交给 TypeSafe Jev 审查，再由 本地政策给出 `allow` 或 `deny`。走第三方 API 时，harness 自带的审批往往 不可用，这个门就是那种场景下的 auto mode。Jev 负责审查，本地政策负责 裁决。Jev 给不出结论时放行——拒绝必须有「这个动作确实危险」的正面证据。 | — | 3 | MIT | 已核验 |
| [**bojansandhaus/jev-decisions**](https://github.com/bojansandhaus/jev-decisions) | 该插件为 Hermes 等 Agent 提供 Jev 评审工具，用于审查风险操作、核对证据支持以及记录本地决策历史。 | — | 3 | MIT | 已核验 |
| [**ClemensSchartmueller/jev-guard**](https://github.com/ClemensSchartmueller/jev-guard) | jev-guard 是适用于 Claude Code、Codex CLI 和 Antigravity 的跨 Agent 安全门插件，可在工具调用执行前进行本地边界与敏感文件检查并调用 Jev 模型评估。 | — | 3 | MIT | 已核验 |
| [**coo-quack/jev-pii-checker**](https://github.com/coo-quack/jev-pii-checker) | 把文本交给 TypeSafe Jev 做 PII 类别 Noul 和敏感度 Score，再用正则与分词标出跨度。 | TypeScript | 3 | MIT | [固定提交](https://github.com/coo-quack/jev-pii-checker/blob/6ad02cdc0d7ca563897ce9eff881b7a7b017d426/src/judge.ts) |
| [**muse0509/jev-preflight**](https://github.com/muse0509/jev-preflight) | jev-preflight：Jev 对行为回归、鉴权等八个风险轴一次性打分，判断本轮变更是否达到需复查的高风险阈值。 | — | 3 | MIT | 已核验 |
| [**OpeOginni/oc-plugins**](https://github.com/OpeOginni/oc-plugins) | OpenCode 插件集合中的 oc-auto-perms，用 Jev 按自然语言规则检查工具操作意图。 | TypeScript | 3 | Unknown | [固定提交](https://github.com/OpeOginni/oc-plugins/blob/237f814908a56eb188c33af298c61531e72dbfe0/packages/oc-auto-perms/src/index.ts) |
| [**shikaizhong-design/ego-jev-ultrafast**](https://github.com/shikaizhong-design/ego-jev-ultrafast) | 核心机制不变：DOM 快照 → 编号动作表 → TypeSafe (Jev) 一次请求同时选 「操作 + 目标元素」（实测中位 0.6–1.9s/步，见 `bench/BENCHMARK.md`）， 小模型只在需要打字时生成字段文本。 | — | 3 | Unknown | 已核验 |
| [**0xwhrari/grok-jev-guard**](https://github.com/0xwhrari/grok-jev-guard) | 该项目是在 Grok Bot 工具操作执行前进行本地硬性检查和 Jev 类型化判断并返回明确执行动作的预检与审批层。 | — | 2 | MIT | 已核验 |
| [**CogFlux/opencode-jev-guard**](https://github.com/CogFlux/opencode-jev-guard) | 这是一个 OpenCode 2 插件，将本地和远端 shell 命令先送给 Jev 评估，仅在属于项目内普通操作且无风险时放行，否则触发确认提示。 | — | 2 | MIT | 已核验 |
| [**dr-dimitru/claude-jev-plugin**](https://github.com/dr-dimitru/claude-jev-plugin) | 把 Jev 的结构化判断接进程序；具体用途与决策流程请查看项目源码。 | — | 2 | BSD-3-Clause | 已核验 |
| [**newuser7171/antivirus**](https://github.com/newuser7171/antivirus) | 从文件静态特征构造状态，让 Jev 给出裁决、0–4 严重度和若干是非指标，再由本地规则决定隔离、放行或复核。 | — | 2 | Unknown | 已核验 |
| [**omkarghugarkar007/actiongate-jev**](https://github.com/omkarghugarkar007/actiongate-jev) | ActionGate 是面向 AI Agent 工具调用的授权网关，结合确定性策略与 Jev 评估提议动作，并对获批的精确动作签发一次性许可，在 MCP 与 HTTP 执行边界进行核销。 | — | 2 | Apache-2.0 | 已核验 |
| [**Red5d/jev-cvss**](https://github.com/Red5d/jev-cvss) | 用 Jev 从漏洞描述中选择 CVSS 指标，再由 Python 计算 v3.0、v3.1 或 v4.0 分数。 | Python | 2 | MIT | [固定提交](https://github.com/Red5d/jev-cvss/blob/b0fdc446e4b9ef070abd570db347a277e496d70c/cvss3_jev.py) |
| [**teyhouse/jev-secret-detection**](https://github.com/teyhouse/jev-secret-detection) | 利用 Jev 模型检验代码片段中的真实凭据泄露：评估小模型在代码安全门禁与敏感密钥识别中的表现。 | — | 2 | Unknown | 已核验 |
| [**4rays/profanity-checker**](https://github.com/4rays/profanity-checker) | profanity-checker：Jev 判断输入文本是否含亵渎语言，以及用户名是否含字面或伪装（谐音/形近）的亵渎内容。 | — | 1 | MIT | 已核验 |
| [**AndreuVM/jev-reasoning-navigator**](https://github.com/AndreuVM/jev-reasoning-navigator) | jev-reasoning-navigator：Jev 对候选推理块评估是否存在幻觉/循环、首个发散步骤位置、缺陷类型以及进度与新颖性评分。 | — | 1 | Unknown | 已核验 |
| [**bismawy/pi-jev-eye**](https://github.com/bismawy/pi-jev-eye) | pi-jev-eye：评估内容是否满足安全或证据要求，由本地策略放行或拦截。 | — | 1 | MIT | 已核验 |
| [**brianluby/momus-review**](https://github.com/brianluby/momus-review) | Momus对Git变更或指定目录下的源文件按正确性、安全性、可靠性、兼容性和测试缺口五个维度做分阶段评审，并对强信号补充证据定位、类型判定、严重程度评分和负责人分派，其中Jev只负责有界的判断问答。 | — | 1 | MIT | 已核验 |
| [**cgbarlow/jev-test**](https://github.com/cgbarlow/jev-test) | 把 Jev 的结构化判断接进程序；具体用途与决策流程请查看项目源码。 | — | 1 | Unknown | 已核验 |
| [**connectedGraph/claude-jev-warden**](https://github.com/connectedGraph/claude-jev-warden) | 该项目为 Claude Code 提供 PreToolUse 钩子，在 Write 与 Edit 落盘前用 TypeSafe Jev 评估草稿并拦截未达标的写入，同时附带命令行审计工具和 SVG 对比示例。 | — | 1 | MIT | 已核验 |
| [**gavansmyth-arch/jev-chrome-extension**](https://github.com/gavansmyth-arch/jev-chrome-extension) | 把 Jev 的结构化判断接进程序；具体用途与决策流程请查看项目源码。 | — | 1 | Unknown | 已核验 |
| [**hemanth/traffic-guard**](https://github.com/hemanth/traffic-guard) | 该项目是为传入 HTTP 请求提供流量分类与拦截判断的网关，提供 Node.js 与 Python 实现，并可选用 TypeSafe System One 通过 Noul、Choice 和 Score 进行语义评估。 | — | 1 | Unknown | 已核验 |
| [**taman-spirit/guardrail-chatbot-jev**](https://github.com/taman-spirit/guardrail-chatbot-jev) | 这是一个聊天机器人内容安全库，用 Jev 对用户输入、模型回复和多轮对话按同一策略文件给出可执行的裁决。 | — | 1 | Unknown | 已核验 |
| [**xienda/dsh-jev-verify**](https://github.com/xienda/dsh-jev-verify) | Jev 不生成文本：给定 \`state\` 与类型化问题，它用**一次并行 API 调用**返回**带校准概率的类型化判定**（官方宣称 ~70–500ms）。本插件把它封装成 Agent 工具，附加可选的**自动护栏**（风险/循环检测），并且坚持「验证过的才叫有效」： | — | 1 | MIT | 已核验 |
| [**hemanth/pkg-gate**](https://github.com/hemanth/pkg-gate) | pkg-gate 是在安装前评估 npm 生命周期脚本的门禁工具，它使用 TypeSafe System One 以 Choice 判断意图、以 Score 评估威胁严重程度、以 Noul 判断机密访问和远程执行，并输出 allow、warn 或 block 的判定结果。 | — | 0 | MIT | 已核验 |
| [**pateti-hub/laya-browser-guard**](https://github.com/pateti-hub/laya-browser-guard) | laya-browser-guard：对输入文本做分类或打分，交给本地规则继续处理。 | — | 0 | Apache-2.0 | 已核验 |

## Voice & Conversation

| 项目 | 简介 | 语言 | ⭐ | 许可证 | 证据 |
|---|---|---:|---:|---:|---|
| [**uezo/aiavatarkit**](https://github.com/uezo/aiavatarkit) | AIAvatarKit 的可选 Jev 组件根据转写内容判断用户是否结束发言。 | — | 686 | Apache-2.0 | [固定提交](https://github.com/uezo/aiavatarkit/blob/38b617b8b9269939734e70ef503d7ea6976acdbd/aiavatar/sts/vad/turn_end_gates/jev.py#L172) |
| [**Knuckles92/OpenWhisper**](https://github.com/Knuckles92/OpenWhisper) | 语音听写与会议记录应用，可选用 Jev 检查话题变化、面向记录助手的指令和敏感文本。 | Python | 198 | MIT | [固定提交](https://github.com/Knuckles92/OpenWhisper/blob/9e83653df183096104769e302a3c907cb277c551/services/typesafe.py) |
| [**haseeb-heaven/jev-system-one**](https://github.com/haseeb-heaven/jev-system-one) | 终端问答界面由 OpenAI 写回答，Jev 决定回答方式、检查草稿并判断是否重写。 | — | 5 | MIT | [固定提交](https://github.com/haseeb-heaven/jev-system-one/blob/66bbfb66556e6daa0f091a04b4e33c3a314eec28/src/jev_system_one/jev.py#L164) |
| [**luxus/ha-conversation-jev**](https://github.com/luxus/ha-conversation-jev) | Home Assistant 的对话扩展：简单灯光指令走设备服务，其余请求交给 Grok。 | Python | 3 | Unknown | [固定提交](https://github.com/luxus/ha-conversation-jev/blob/a405366b66b8c8dc5d73b32333043befdbbe2287/custom_components/jev_assist/jev_client.py) |

---

发现遗漏？请提交 Issue，并附上仓库地址与 JEV 使用位置。
