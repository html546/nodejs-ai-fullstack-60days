# Node.js 60 天：从零基础到 AI 协作全栈

基于 [原版 Node.js 60 天课程](https://xiguadev.com/node-60days) 的日序与公开主题，重新编写讲解、练习和项目。原来只放在附录里的 NestJS、PostgreSQL、Prisma、认证、Redis、队列、Docker、部署与 SaaS 综合项目，在这一版都进入正文。保留每天的原课入口，便于对照。覆盖原课程的 **60 个日主题**，并补充 Next.js、tRPC 与 React Query 对照实验；主项目沿用 Nest REST，再配 React 页面，原课各技术的实现细节与深入程度并非逐段等量复刻。

**本版文件与验证范围：**离线页与 Markdown 是完整的 60 天讲义；`60天配套/基础实验` 提供第 01—05 天独立实验，`60天配套/day54-web` 提供已构建验证的首屏前端，`60天配套/blog-api` 与 `60天配套/board-api` 提供第 16–53 天完整代码块的源码快照（不含脚手架与迁移历史，按正文补齐后才能运行）；`60天配套/docker-compose.prod.yml` 供第 55 天本机发布演练静态核对。其余片段按正文标注放进对应工程，不是已经打包完成的整套 SaaS 仓库。本机已运行基础实验、执行前端类型检查与构建，并检查 60 天目录和链接；PostgreSQL、Redis、Docker、OIDC、CI 和云端部署没有全部实测，不将预期结果当作通过记录。

## 从这里开始

不要求会 JavaScript、不要求先办云账号，也不要求购买 AI 工具。先把代码跑通，再做当天练习。初学者可把一天拆成两到三个学习时段：读懂一个小例子、动手修改、跑完验收。60 天是 60 个学习单元，不是必须连续打卡的工期。环境安装、数据库和部署单元留更多时间；不能只因跳过了操作就给自己勾选完成。

本路线适合想把 AI 当开发搭档、逐渐能独立交付全栈项目的人。“AI 协作全栈”不等于必须接大模型 API：结课目标是你能解释数据流、做技术取舍、验证 AI 修改并为交付负责。课程不保证仅学完就能胜任所有全栈岗位。

### 六阶段与过关产物

| 阶段 | 学习内容 | 可以演示的产物 |
| --- | --- | --- |
| 01–15 · Node 基础 | JavaScript 补课、模块和 npm、文件与流、异步、HTTP、TS、调试 | 在本机发请求，完成原生任务 API；能在错误栈中定位自己的代码 |
| 16–30 · 框架和数据 | Nest、请求生命周期、DTO、SQL、索引、建模、Prisma、事务 | 带数据库的博客 API，重启数据仍在，有分页和输入验收 |
| 31–40 · 认证和后台工作 | Session/JWT、角色、OIDC、上传、Redis、队列 | 分清登录、权限、资源归属，完成可测试的博客第二版 |
| 41–45 · 交付 | Docker、Compose、CI/CD、发布、日志和健康检查 | 从干净环境启动服务，能验证发布并说清回滚方案 |
| 46–55 · 全栈综合 | 项目设计、前端基础、团队、任务看板、实时通知、统计和联调 | 一条完整用户流程：登录 → 进入团队 → 操作任务 → 页面显示结果 |
| 56–60 · 工程能力与求职 | 测试、可测量优化、系统设计、作品陈述、复盘 | 可复现的作品 README、测试清单、改进前后证据及项目讲解 |

### 读每一天的顺序

1. **今日先学**：圈出一个新概念，尝试用一句话解释。尚未理解可以重跑前一单元，不需要继续背术语。
2. **跟做**：按文件名放代码，用终端执行对应命令，记录实际输出。命令、程序和预期输出是三种不同内容，不混贴。
3. **练习**：先写自己预测的结果，再修改一个地方。课程使用的并非每个代码块都能独立运行；标注替换或追加的片段要放进指明的文件中。已做过的练习不要覆盖主线代码；单独保留，下一天照说明继承。
4. **参考答案与验收**：先检查失败路径，再检查成功路径。网页默认折叠答案。进度勾选只保存在当前浏览器，不上传数据。
5. **AI 搭档**：请 AI 解释或审查当天一个具体问题。提交自己的假设、上下文和实际结果；不直接让 AI 代写整章。

看到 `node xxx.mjs`、`npm run ...` 就在终端运行；代码块内的脚本或配置，按文件名写在编辑器中。一个目录一个项目。早期示例用 `127.0.0.1`，打不开先查当前目录、Node 版本、终端输出和端口。服务器仍在运行时不要在同一个终端输入客户端命令；要另开一个终端，或先按 `Ctrl+C` 停止。Windows PowerShell 若拦截 `npm.ps1`，可以用 `npm.cmd`、`npx.cmd` 或切换到命令提示符，不必改全局安全设置。

### 三个工程的关系

- 开头的**原生任务 API**用 JavaScript 和 Node 内置能力看清底层。处理的是字符串 id 的任务，状态为 `todo`、`doing` 或 `done`。
- 中段的**博客 API**按原课程里程碑推进。用文章、作者练习模块分层、SQL、迁移、认证、任务、缓存与部署；不是与任务 API 强行共用数据表。
- 最终的**协作任务板**把模块组织、数据库、认证与交付方法迁移到团队、项目、任务实体。页面、API、数据库和队列各有职责。不要直接把博客库当作任务板库；新建项目和数据库。

### 术语表

全文统一使用以下叫法，遇到旧名按这里对照：

| 本文用词 | 含义 | 也曾写作 |
|---|---|---|
| 原生任务 API | 第 01–15 天用 Node 内置能力做的字符串 id 任务服务 | 任务清单、任务板（基础阶段） |
| 博客 API | 第 16–45 天用 Nest + PostgreSQL 做的文章/作者服务 | mini-blog、博客后端 |
| 协作任务板 | 第 46–55 天团队/项目/任务的完整全栈项目 | SaaS 项目、任务看板 |
| Nest | NestJS 框架 | NestJS（仅阶段表保留全称） |
| Prisma 6.19.x | 固定使用的 Prisma 版本 | Prisma 6.19.0、Prisma 6 |
| liveness / readiness | 存活探针 / 就绪探针 | 活性检查 / 健康检查（泛指时） |

「任务板」单独出现时指基础阶段的原生任务 API；「协作任务板」才指最后的全栈项目。两者不是同一个工程。

### 环境安装分批做

| 到哪一天才需要 | 工具 | 用途与边界 |
| --- | --- | --- |
| 01 | Node.js 22 / 24 / 26 LTS（新项目优先 26）、npm、VS Code 或其他文本编辑器 | 用 `node -v` 和 `npm -v` 检查；前段不依赖数据库 |
| 11、16 | TypeScript、Nest 11 | 按讲义在项目目录安装，不要求提前学完框架 |
| 21、25 | PostgreSQL 16、Prisma 6 | 首次练 SQL 只需要自己的练习库；Prisma 6 教学命令不要混用 v7 文档 |
| 36、38 | Redis、BullMQ | 用本机/隔离学习实例；不要对公网暴露 Redis 或使用生产实例 |
| 41 | Docker 和 Compose | 本地镜像与服务编排，不要求提前安装；Windows 的 WSL2 及 Docker Desktop 需要系统支持 |
| 43、44 | Git 仓库、可选云账号 | 累计到这一步再发布；云端实操前先评估费用、配置和回滚，全文不代为部署 |
| 46–55 | TypeScript 前端与 Vite | 浏览器、HTML 和 HTTP 先学清再接后端，数据库访问只在后端 |

软件版本和云服务界面会变化。教程中的预期输出用于自己验收，不表示所有第三方服务已经在本机逐条运行。账户、数据库、Docker、CI、云部署需要你的学习环境与授权。针对无法安装的工具，可以先读图、走无依赖示例并在日志注明「未实测」，等环境可用再验收。

## AI 协作：先定义验收，再让工具帮忙

### AI 搭档提问的四阶段递进

每天的「AI 搭档」不是同一句提示词套 60 次，而是随能力增长换问题类型。按阶段主动调整提问方式：

| 阶段 | 让 AI 做什么 | 不让 AI 做什么 | 你要自己交的证据 |
|---|---|---|---|
| 基础期（01–15） | 解释概念、预测一段代码的输出、出一个变形题 | 不代写完整程序 | 你先写预测，再运行 `node` 对照 |
| HTTP / Nest 期（16–30） | 预测状态码、审查 DTO 边界、解释生命周期顺序 | 不编造实测结果 | 用 `curl` 记录真实的请求与响应 |
| 数据与权限期（31–45） | 检查 SQL 与索引、找越权路径、设计失败用例 | 不碰真实凭据或生产库 | 断言片段或 SQL 计划截图（脱敏） |
| 综合与交付期（46–60） | 生成验收清单、扮演面试官追问故障场景 | 不替你画完整架构图或做部署决策 | 自己画的数据流图与回滚条件 |

共同底线不变：只给脱敏上下文，不接受凭空报告的"通过"，改完先在本地复现再采纳。

### 一段所有日子都能用的提示词

```text
我今天要完成：[本课目标]。只讨论 [文件/接口/错误]，不要重写项目。
技术环境：[Node 版本、包版本、操作系统]。我已学到：[前置知识]。
我做了：[最小复现命令]。预期：[输出/状态/数据]。实际：[脱敏结果]。
先帮我解释差异，请给两个可以排除原因的小检查，再提最小修改。
补一个能失败的验收用例；不要加未说明的依赖，也不要执行部署。
```

使用 AI 前先删去 `.env`、数据库连接串、令牌、真实业务数据和账号信息。不要让工具自动安装陌生依赖、执行破坏性命令或把代码发布到外部。本地先审查差异，再分小步运行命令；改了权限就验收允许和拒绝两类，改了数据库就用测试库先复现。只留下自己能讲清楚的代码。

### 从第 01 天开始记工程日志

```text
日期 / 第几天 / 我做出的功能：
我原来以为：
AI 建议：
我接受或拒绝的理由：
我运行的命令与实际结果：
我还不能解释的问题：
```

作品集只使用能展示的事实：功能截图或录屏、测试输出、发布记录、可复现的性能数据。没有部署就写本地可运行，没有多用户数据就用合成样本，不虚构生产经验。

### 参考与补课

- [原课程 60 天目录](https://xiguadev.com/node-60days) · [原课程开源仓库](https://github.com/crisweb1994/60-days-nodejs)
- [MDN JavaScript 指南](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Guide) · [Node.js 教程](https://nodejs.org/en/learn) · [TypeScript 官方手册](https://www.typescriptlang.org/docs/handbook/intro.html)
- [NestJS 文档](https://docs.nestjs.com/) · [PostgreSQL 16 教程](https://www.postgresql.org/docs/16/tutorial.html) · [Prisma 文档](https://www.prisma.io/docs)
- [React 基础](https://react.dev/learn) · [Vite 指南](https://vite.dev/guide/) · [Docker 文档](https://docs.docker.com/)
- 若前几天还不熟悉变量、数组、函数和终端，优先用上面「参考与补课」里的 MDN JavaScript 指南和 Node.js 官方教程按主题补课；本包不含另一套旧版编号，不要去找 `lesson-XX` 之类的目录。


# 第 01 天：安装 Node.js，运行第一份任务清单
原课：<https://xiguadev.com/node-60days/day-01>

## 今日先学

Node.js 可以在浏览器之外运行 JavaScript。本课程使用受支持的 Node.js LTS 版本（22 / 24 / 26 均可，新项目优先 26）。到 Node.js 官网下载相应版本，安装后重新打开终端。Windows 读者使用 Git Bash，macOS 和 Linux 读者可以用自带的终端。讲义统一把命令和代码分开，命令粘贴到终端，JavaScript 存成文件再用 `node` 运行。<https://nodejs.org/>

在**原生任务 API** 里，一条任务有三个字段。（「协作任务板」专指第 46–55 天的团队全栈项目，见术语表；本阶段只是本机原生任务 API。）`id` 是字符串编号，`title` 是字符串标题，`status` 只能填 `todo`、`doing` 或 `done`。本阶段由一位用户在自己的电脑操作，先从终端输出开始，之后再把同一份任务结构用于 HTTP。

## 跟做

```bash
node --version
npm --version
mkdir task-board
cd task-board
```

第一条应显示 `v22.x.x`、`v24.x.x` 或 `v26.x.x`。第二条应显示 npm 的版本号，具体数字随安装包而变。如果终端找不到 `node`，先重开终端，再确认安装时已将 Node.js 加入 `PATH`。用编辑器打开刚建的 `task-board`，把下面的内容存成 `day01.mjs`。`.mjs` 表示这个文件按 JavaScript 的 ES 模块方式运行。

```js
const tasks = [
  { id: 't1', title: '整理需求', status: 'todo' },
  { id: 't2', title: '准备示例', status: 'doing' },
]
let doneCount = 0

for (const task of tasks) {
  if (task.status === 'done') {
    doneCount += 1
  }
  console.log(`[${task.status}] ${task.title}`)
}
console.log(`已完成 ${doneCount} / ${tasks.length}`)
```

`const` 声明无需重新赋值的名字，`let` 声明后面会改写的名字。`{}` 围出对象，`[]` 围出数组。`task.title` 读取对象的标题，`tasks.length` 读取数组的长度。`for...of` 每轮取出一个任务，`if` 只在条件满足时运行它的代码块。`===` 比较两边的值和类型，`+= 1` 把计数加一。反引号中的 `${...}` 会把表达式的值放进文本。

```bash
node day01.mjs
```

应先看到 `[todo] 整理需求` 和 `[doing] 准备示例`，再看到 `已完成 0 / 2`。遇到找不到文件的提示，用 `pwd` 确认当前目录，并检查编辑器有没有把文件保存成 `day01.mjs.txt`。

## 练习

给清单增加一条编号为 `t3`、标题为「确认范围」的已完成任务，保留原来的两条。

## 参考答案与验收

在数组的 `]` 之前加一行 `{ id: 't3', title: '确认范围', status: 'done' },`。重新运行 `node day01.mjs`，第三行应为 `[done] 确认范围`，最后一行应为 `已完成 1 / 3`。再把新任务改成 `todo`，确认计数回到零。

## AI 搭档

提示词「用 `t1`、`t2` 两条虚构任务，逐轮解释 `for...of` 如何改变 `doneCount`。给我一道改状态后预测输出的题，等我回答后再公布答案。」只粘贴虚构任务和脱敏报错，最后自己运行命令核对。

# 第 02 天：拆分 ES 模块，用 npm 保存运行命令
原课：<https://xiguadev.com/node-60days/day-02>

## 今日先学

昨天的脚本同时存放任务和打印逻辑。今天把「根据状态计数」提到独立模块，让入口负责准备数据和展示结果。模块里通过 `export` 公开名字，调用方用 `import` 引用。以 `./` 开头的是相对当前文件的路径，在 Node.js ESM 中导入本地文件时要写完整扩展名。npm 随 Node.js 一起安装，能管理第三方包，也能在 `package.json` 里保存运行命令。

## 跟做

回到 `task-board`。先生成项目配置，再安装一个体积小的终端配色包。本例把颜色关闭，让不同终端的验收文字一致，同时保留一次真实的安装和导入过程。

```bash
npm init -y
npm install --save-exact picocolors@1.1.1
npm pkg set 'scripts.day02=node day02.mjs'
```

新建 `task-stats.mjs`。`function` 声明函数，括号里的 `tasks` 和 `status` 是参数，调用时由外部传入。函数内部的 `count` 每次调用都从零开始。`return` 将结果交还调用处。

```js
export function countByStatus(tasks, status) {
  let count = 0
  for (const task of tasks) {
    if (task.status === status) {
      count += 1
    }
  }
  return count
}
```

再建 `day02.mjs`。包名 `picocolors` 由 Node.js 到依赖目录解析。本地模块公开了 `countByStatus`，因此用带花括号的具名导入。`pc.createColors(false)` 调用包提供的函数，`colors.green(...)` 返回一段可直接打印的文本。

```js
import pc from 'picocolors'
import { countByStatus } from './task-stats.mjs'

const colors = pc.createColors(false)
const tasks = [
  { id: 't1', title: '整理需求', status: 'todo' },
  { id: 't2', title: '准备示例', status: 'done' },
]
const doneCount = countByStatus(tasks, 'done')
console.log(colors.green(`已完成 ${doneCount} / ${tasks.length}`))
```

```bash
npm run day02
npm ls picocolors
```

第一条会先回显脚本命令，再打印 `已完成 1 / 2`。第二条的依赖树里应有 `picocolors@1.1.1`。`package.json` 记录项目所需的包和脚本，`package-lock.json` 记录解析后的依赖版本，`node_modules` 保存已经安装到本机的文件。把项目交给同伴时，保留两份 JSON 配置，对方可以在项目目录用 `npm ci` 按锁文件安装。遇到 `ERR_MODULE_NOT_FOUND`，先分清缺少的是依赖包还是本地文件，再查安装结果或路径拼写。

## 练习

保留完成数，再打印一行待办数。给数组增加一条 `doing` 任务，预测两个数字再运行。

## 参考答案与验收

在入口末尾加上 `console.log('待办', countByStatus(tasks, 'todo'))`。添加 `{ id: 't3', title: '确认范围', status: 'doing' },` 后重跑 `npm run day02`，应看到 `已完成 1 / 3` 和 `待办 1`。分别改动一条任务的状态，确认函数确实使用传入的状态参数。

## AI 搭档

提示词「我有一个具名导出的 `countByStatus`。基于这两条虚构任务，出一道导入路径排错题，再提供一个可手算的计数用例。」只分享示例模块和脱敏路径，分别跑 `npm run day02` 和 `npm ls picocolors` 验收。

# 第 03 天：用 fs、path 和 os 保存任务
原课：<https://xiguadev.com/node-60days/day-03>

## 今日先学

进程结束后，脚本内的任务数组会随之消失。今天先用同步文件函数观察「数组 → 文件 → 数组」的过程。`node:fs` 读写文件，`node:path` 负责拼接文件路径，`node:os` 能查看操作系统信息。JSON 是便于保存和交换的数据文本。JavaScript 对象可以用单引号和省略键名的引号，JSON 里的字符串和键名要用双引号，最后一项后面也不能留逗号。

`JSON.stringify(value, null, 2)` 把值转为文本，用两个空格缩进。`JSON.parse(text)` 将合法 JSON 转回 JavaScript 值。能解析的 JSON 可能只是一个字符串或一个数字，要用 `Array.isArray()` 检查这里读到的是不是数组。

## 跟做

在 `task-board` 新建 `day03.mjs`。项目根目录会生成 `data/tasks.json`。`path.join()` 把路径片段连起来，`path.resolve()` 以终端当前目录为起点算出绝对路径，因此运行前要在项目目录。`mkdirSync` 的 `recursive: true` 允许目录已存在。示例文件存在时直接读取，避免每次演示都覆盖自己的修改。

```js
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs'
import path from 'node:path'
import os from 'node:os'

const seed = [{ id: 't1', title: '整理需求', status: 'todo' }]
const dataDir = path.resolve('data')
const file = path.join(dataDir, 'tasks.json')

try {
  mkdirSync(dataDir, { recursive: true })
  if (!existsSync(file)) {
    writeFileSync(file, JSON.stringify(seed, null, 2), 'utf8')
  }
  const text = readFileSync(file, 'utf8')
  const tasks = JSON.parse(text)
  if (!Array.isArray(tasks)) {
    throw new Error('任务文件需要包含数组')
  }
  console.log(`任务数 ${tasks.length}`)
  console.log(`系统 ${os.platform()}，文件 ${file}`)
} catch (error) {
  console.error('读取任务失败：', error.message)
  process.exitCode = 1
}
```

`try` 包住可能失败的操作。`throw` 抛出一个错误，`catch (error)` 接到异常后可用 `error.message` 取得说明。这里用 `process.exitCode = 1` 让终端知道本次命令失败。读取时指定 `'utf8'`，就能得到能传给 `JSON.parse` 的字符串。

```bash
node day03.mjs
```

在首次运行、文件还不存在时，应看到 `任务数 1`。第二行的系统值和文件路径随电脑而变，例如 Windows 上的 `os.platform()` 返回 `win32`。

## 练习

手动给 `data/tasks.json` 增加一条已完成任务。再暂时把整份文件改为 `{}`，观察错误并恢复。

## 参考答案与验收

合法的完整内容如下。每次修改后都运行 `node day03.mjs`。

```json
[
  { "id": "t1", "title": "整理需求", "status": "todo" },
  { "id": "t2", "title": "准备示例", "status": "done" }
]
```

应看到 `任务数 2`。改成 `{}` 后，终端应显示 `读取任务失败： 任务文件需要包含数组`，且 `node day03.mjs` 后立刻执行 `echo $?` 应得到 `1`。恢复上述数组并确认数量回到 `2`。

## AI 搭档

提示词「区分两种错误：JSON 有尾逗号，以及 JSON 合法但顶层是对象。根据我给出的最小虚构样例，分别指出程序会在哪一步失败。」只传模拟文件和脱敏路径，亲自运行两个输入验证。

# 第 04 天：理解事件、流和 Buffer
原课：<https://xiguadev.com/node-60days/day-04>

## 今日先学

文件中的中文和标点都以字节保存。`Buffer` 表示一段字节，`Buffer.from(text, 'utf8')` 将文本编码成字节，`buffer.toString('utf8')` 把完整的字节序列解码。字符串的 `length` 按 UTF-16 代码单元计数，`Buffer` 的 `length` 按字节计数。例如「任务」的字符串长度是 `2`，UTF-8 字节数是 `6`。

流分块处理输入和输出，适合在文件增长后逐段复制或传输。流也会发出事件。对 `EventEmitter` 调用 `on` 可登记监听函数，调用 `emit` 会在当下按登记顺序执行对应监听函数。今天给任务文件做一份流式备份，复制完成后才发出自定义事件。先跑过第 03 天，确保 `data/tasks.json` 已存在。

## 跟做

新建 `day04.mjs`。`(参数) => { ... }` 是箭头函数，可像普通函数一样接收参数。它出现在 `on()` 中时，表示把函数交给事件对象保存，等事件发生才调用。`pipeline()` 把读流和写流连起来，在写入端来不及处理时协调读取速度，并将完成或失败交给最后的回调。

```js
import { EventEmitter } from 'node:events'
import { createReadStream, createWriteStream } from 'node:fs'
import { pipeline } from 'node:stream'

const board = new EventEmitter()
const target = 'data/tasks.backup.json'

board.on('backup:done', (file) => {
  console.log(`已备份 ${file}`)
})

const label = '任务'
const bytes = Buffer.from(label, 'utf8')
console.log(label.length, bytes.length, bytes.toString('utf8'))

pipeline(
  createReadStream('data/tasks.json'),
  createWriteStream(target),
  (error) => {
    if (error) {
      console.error('备份失败：', error.code ?? error.message)
      process.exitCode = 1
      return
    }
    board.emit('backup:done', target)
  },
)
```

`return` 单独一行可以提前结束当前函数。`??` 在左侧为 `null` 或 `undefined` 时才取右侧，因此这里优先打印错误代码。有些读取块会恰好切在一个汉字的多个字节中间。此处直接复制字节，可保留原文件里的中文。目标文件已存在时，这段代码会重新写它。

```bash
node day04.mjs
cmp data/tasks.json data/tasks.backup.json
```

第一条应先打印 `2 6 任务`，再打印 `已备份 data/tasks.backup.json`。`cmp` 会逐字节比较两个文件。内容一致时它不输出文本，退出码为 `0`。

## 练习

给事件登记第二个监听者，输出 `请抽查备份`。再把脚本里的源文件暂时改为 `data/missing-demo.json`，比较两次输出。

## 参考答案与验收

在原监听者下面加 `board.on('backup:done', () => console.log('请抽查备份'))`，成功时两条事件消息按登记顺序出现。源文件不存在时应看到 `备份失败： ENOENT`，两条成功消息都不会出现。恢复源文件名，重跑脚本并用 `cmp` 验证备份。

## AI 搭档

提示词「用虚构任务标题解释一个 UTF-8 汉字被拆到两个读取块会发生什么。再给我一条判断备份失败时事件是否正确的检查。」只提交虚构标题和脱敏错误，自己运行成功与失败两个分支。

# 第 05 天：看懂事件循环的输出顺序
原课：<https://xiguadev.com/node-60days/day-05>

## 今日先学

昨天的事件监听函数在 `emit()` 调用时立即运行，流的完成回调则要等读写结果回来。Node.js 执行当前这一段 JavaScript 时，回调要等当前调用栈清空才能获得执行机会。调用栈记录正在执行的函数。微任务是一类会在检查点先排空的队列，`queueMicrotask()` 和已经兑现的 Promise 的 `.then()` 都可把工作放进去。定时器会在达到最短等待时间后等待执行机会，`setTimeout(fn, 0)` 依然要排队。

Promise 表示将来可以拿到的成功值，或者将来可以处理的失败原因。`Promise.resolve(value)` 创建一个已兑现的 Promise，`.then(fn)` 登记成功后执行的函数，即使值已经就绪，`fn` 仍然进入微任务队列。明天再用 `await` 取出同一种结果。

## 跟做

把下面的代码保存为 `day05.mjs`。先用纸写出六行顺序，执行后再逐行对照。字符串是任务板启动时的虚构日志。

```js
import { EventEmitter } from 'node:events'

const board = new EventEmitter()
board.on('ready', () => console.log('2 同步事件'))

console.log('1 开始')
setTimeout(() => console.log('6 定时器'), 0)
board.emit('ready')
Promise.resolve('4 Promise 已兑现').then((message) => {
  console.log(message)
})
queueMicrotask(() => console.log('5 普通微任务'))
console.log('3 同步结束')
```

```bash
node day05.mjs
```

预期按编号输出 `1` 到 `6`。登记定时器时没有马上执行其回调，所以第二行来自同步 `emit()`。同步段结束后，先登记的 `.then()` 回调先执行，接着是 `queueMicrotask()` 回调，最后才轮到定时器。真实程序里的文件读写何时完成会受系统和负载影响，多个来源的回调要分开观察。给同一任务安排先后依赖时，可以把后续操作放进成功回调，避免猜测延时。

## 练习

交换 `.then()` 整段与 `queueMicrotask()` 的位置，保留日志编号。再用一个普通函数替代 Promise 的回调实验，观察它被直接调用时排在哪。

## 参考答案与验收

只交换登记位置后，预期顺序为 `1、2、3、5、4、6`。接下来用 `function printLoaded() { console.log('4 直接调用') }` 和紧跟的 `printLoaded()` 替换交换后的 Promise 语句。再次运行，预期为 `1、2、4、3、5、6`。虽然登记微任务发生得早，直接调用的函数会先在同步段中执行。

## AI 搭档

提示词「只用这份任务板启动日志，让我分别圈出同步调用、微任务和定时器，给一个交换两行登记语句的预测题。」只提供虚构日志和例子，先记下自己的预测，再通过 `node day05.mjs` 核验。


# 第 06 天：用 Promise 和 async/await 读写任务
原课：<https://xiguadev.com/node-60days/day-06>

## 今日先学

昨天看到，`.then()` 登记的回调会在当前同步代码之后执行。Promise 把将来才有的结果表示成对象：成功时进入兑现状态并带有一个值，失败时进入拒绝状态并带有一个原因。`async` 函数总会返回 Promise；在函数内部写 `await promise`，会暂停这个函数，直到 Promise 成功或失败，再把值交给后面的语句。`await` 不会阻塞整个 Node.js 进程。

`node:fs/promises` 提供基于 Promise 的文件 API。今天将第 03 天的种子任务保存到文件，再读回来计算数量。整个过程使用虚构数据；重复运行会重置 `data/tasks-async.json`，不要把个人资料写入这个示例。

## 跟做

在项目目录建立 `day06.mjs`。`await mkdir()` 创建目录，`writeFile()` 写 JSON 文本，`readFile()` 读回 UTF-8 字符串。保存和读取按顺序发生，后一个调用只有在前一个完成后才继续。`try/catch` 能接住 `await` 过程中拒绝的 Promise。

```js
import { mkdir, readFile, writeFile } from 'node:fs/promises'
import path from 'node:path'

const tasks = [
  { id: 't1', title: '整理需求', status: 'todo' },
  { id: 't2', title: '准备示例', status: 'done' },
]
const file = path.resolve('data', 'tasks-async.json')

async function main() {
  try {
    await mkdir(path.dirname(file), { recursive: true })
    await writeFile(file, JSON.stringify(tasks, null, 2), 'utf8')
    const text = await readFile(file, 'utf8')
    const loaded = JSON.parse(text)
    console.log(`异步读回 ${loaded.length} 条任务`)
  } catch (error) {
    console.error('文件操作失败：', error.message)
    process.exitCode = 1
  }
}

main()
```

`main()` 返回 Promise，但这里可以直接调用，因为 Node.js 会等待尚未完成的文件操作。若一个异步函数的调用结果需要给另一段代码使用，可以写 `await main()` 或为它接上 `.then()`。不要把 `await` 写在普通函数体中；它只能用于 `async` 函数体，或支持顶层 await 的 ES 模块。

```bash
node day06.mjs
```

应显示 `异步读回 2 条任务`，并在 `data` 下看到 `tasks-async.json`。用编辑器打开文件，观察它是格式化的标准 JSON。若遇到拒绝，先读错误消息里的路径或代码，再判断是目录、权限还是 JSON 解析问题。

## 练习

把 `tasks` 增加为三条任务，再运行。然后暂时把输出目录名字改成无效路径，观察 `catch` 是否接住错误，最后恢复。

## 参考答案与验收

增加 `{ id: 't3', title: '确认范围', status: 'doing' },` 后，应显示 `异步读回 3 条任务`，且 JSON 文件含有三项。把 `file` 改为项目目录下的 `data/missing-parent/tasks-async.json` 并删除或注释掉 `await mkdir(...)`，目录不存在时应显示 `文件操作失败：` 和系统给出的错误信息，进程退出码为 `1`。恢复目录创建后重新运行，输出恢复为 3 条。

## AI 搭档

提示词「只用两条虚构任务，逐行说明 `await writeFile` 为什么必须在 `await readFile` 前完成。给我一道模拟拒绝的题，不要替我改文件。」只提供脱敏代码和报错；自己执行 `node day06.mjs`，检查内容和退出码。

# 第 07 天：用原生 HTTP 返回任务
原课：<https://xiguadev.com/node-60days/day-07>

## 今日先学

Node.js 内建 `node:http`，不安装 Web 框架也能建立 HTTP 服务器。服务器收到请求时调用回调，回调能读取请求的方法和路径，并写入响应状态码、响应头和响应体。HTTP 头告诉客户端响应内容类型；响应体若是 JSON，先用 `JSON.stringify()` 转为文本，再以 UTF-8 发送。`127.0.0.1` 是本机回环地址，只接受本机访问，适合学习和验收。

## 跟做

新建 `day07.mjs`。这里暂时仅支持 `GET /tasks`，返回内存中的两条示例任务。`server.listen(port, '127.0.0.1', callback)` 开始监听本机端口。请求处理函数是同步的，收到每个请求后立即生成一个 JSON 响应。

```js
import { createServer } from 'node:http'

const tasks = [
  { id: 't1', title: '整理需求', status: 'todo' },
  { id: 't2', title: '准备示例', status: 'doing' },
]

const server = createServer((req, res) => {
  if (req.method === 'GET' && req.url === '/tasks') {
    res.writeHead(200, { 'content-type': 'application/json; charset=utf-8' })
    res.end(JSON.stringify(tasks))
    return
  }
  res.writeHead(404, { 'content-type': 'application/json; charset=utf-8' })
  res.end(JSON.stringify({ error: 'Not Found' }))
})

server.listen(3000, '127.0.0.1', () => {
  console.log('任务板已启动：http://127.0.0.1:3000')
})
```

```bash
node day07.mjs
```

保持服务器终端运行，另开一个终端测试：

```bash
curl -i http://127.0.0.1:3000/tasks
curl -i http://127.0.0.1:3000/unknown
```

第一条应有 `HTTP/1.1 200 OK`、`content-type: application/json; charset=utf-8` 和两条任务。第二条应有 `404` 和 `{"error":"Not Found"}`。结束服务器时，回到服务器终端按 `Ctrl+C`。若启动提示 `EADDRINUSE`，说明端口被占用，可把代码里的 `3000` 和 curl 地址里的 `3000` 一起改成 `3001`。

## 练习

增加 `GET /health`，它应响应 `{"ok":true}`。给不存在的路径保留 404。

## 参考答案与验收

在 `/tasks` 的判断之后、404 之前加入：

```js
if (req.method === 'GET' && req.url === '/health') {
  res.writeHead(200, { 'content-type': 'application/json; charset=utf-8' })
  res.end(JSON.stringify({ ok: true }))
  return
}
```

重启服务并运行 `curl -i http://127.0.0.1:3000/health`，应见 `200 OK` 和 `{"ok":true}`。再访问 `/other`，仍应是 404。

## AI 搭档

提示词「对照这段原生 HTTP 服务器，用虚构请求路径出一道判断 200 或 404 的题。提醒我只绑定 `127.0.0.1`，不要增加外网监听。」只粘贴脱敏请求和响应；自己启动服务器并用 curl 验收。

# 第 08 天：实现原生 REST 上半场：列出、新建和查单条
原课：<https://xiguadev.com/node-60days/day-08>

## 今日先学

今天继续使用 `node:http`，不加入框架、数据库或登录系统。REST 是一种设计 HTTP 资源接口的风格，URL 表示资源，HTTP 方法表达操作：`GET` 读取，`POST` 创建。统一资源路径 `/tasks` 用来表示任务集合，`/tasks/<ID>` 表示单条任务。**注意 ID 方案从今天起切换**：第 01–07 天示例用 `t1`/`t2` 这类手写编号，今天起由服务端用 `randomUUID()` 生成 UUID；以前保存的 `/tasks/t1` 在今天的程序里会返回 404，请用创建响应里的 `id` 访问。集合先放在服务器进程的内存里，所以服务重启后改动会丢失。本阶段仅供一位用户在本机练习。

HTTP 请求体是一段数据流。Node 的请求对象实现可读流接口，可用 `for await...of` 逐块读取；拼成文本后用 `JSON.parse()`。任何客户端输入都要先解析、再校验，不能直接假定它一定是合法 JSON 或符合任务格式。

## 跟做

用下面代码新建 `day08.mjs`。服务器提供列举所有任务、按 ID 查一项、创建任务。新建只接收标题，服务端生成 ID 和状态，避免客户端伪造这些字段。同步的 `for...of` 适合循环数组，`for await...of` 则逐段等待 HTTP 请求体。读取请求体时先把每个 Buffer 收集起来，最后用 `Buffer.concat` 一次性解码；逐块 `toString()` 会把恰好跨块的汉字切成替换字符（第 04 天讲过这个坑）。**`createServer` 的回调是 async，但 `node:http` 不会处理它返回的 Promise**：任何未捕获的异常都会变成 unhandled rejection 让进程退出，所以整个回调外面要包一层 `try/catch`，与第 12/14 天的统一错误处理一致；第 09 天的同一结构也要照此处理。

```js
import { randomUUID } from 'node:crypto'
import { createServer } from 'node:http'

const tasks = []

async function readJson(req) {
  const chunks = []
  for await (const chunk of req) chunks.push(chunk)
  return JSON.parse(Buffer.concat(chunks).toString('utf8'))
}

function send(res, status, body) {
  res.writeHead(status, { 'content-type': 'application/json; charset=utf-8' })
  res.end(JSON.stringify(body))
}

const server = createServer(async (req, res) => {
  try {
    const url = new URL(req.url, 'http://127.0.0.1:3000')
    if (req.method === 'GET' && url.pathname === '/tasks') {
      return send(res, 200, tasks)
    }
    if (req.method === 'POST' && url.pathname === '/tasks') {
      try {
        const body = await readJson(req)
        if (typeof body.title !== 'string' || body.title.trim() === '') {
          return send(res, 400, { error: 'title is required' })
        }
        const task = { id: randomUUID(), title: body.title.trim(), status: 'todo' }
        tasks.push(task)
        return send(res, 201, task)
      } catch {
        return send(res, 400, { error: 'invalid JSON' })
      }
    }
    const match = url.pathname.match(/^\/tasks\/([^/]+)$/)
    if (req.method === 'GET' && match) {
      const task = tasks.find((item) => item.id === match[1])
      return task ? send(res, 200, task) : send(res, 404, { error: 'Task not found' })
    }
    return send(res, 404, { error: 'Not Found' })
  } catch (error) {
    console.error(error)
    return send(res, 500, { error: 'internal error' })
  }
})

server.listen(3000, '127.0.0.1', () => console.log('任务板：http://127.0.0.1:3000'))
```

`new URL()` 将路径解析为 URL；`pathname` 不含查询字符串。正则表达式只匹配 `/tasks/` 后恰好一段路径。`find()` 找到第一个符合条件的任务，否则返回 `undefined`。在服务端运行：

```bash
node day08.mjs
```

另开终端，使用 curl 发送 JSON。双引号的写法适用于 Git Bash、macOS 和 Linux shell：

```bash
curl -i http://127.0.0.1:3000/tasks
curl -i -X POST http://127.0.0.1:3000/tasks -H 'content-type: application/json' -d '{"title":"整理需求"}'
```

空集合响应 `[]`。创建响应为 `201 Created`，其中有自动生成的 `id` 和 `todo` 状态。复制返回的 ID 替换 `ID`，查询单条：

```bash
curl -i http://127.0.0.1:3000/tasks/ID
```

## 练习

尝试提交空标题、畸形 JSON 和不存在的 ID，记录每个状态码。

## 参考答案与验收

`{"title":"  "}` 应返回 `400` 和 `title is required`。`{bad}` 应返回 `400` 和 `invalid JSON`。查一个不存在的 ID 应返回 `404` 和 `Task not found`。重启进程后再次列举，应回到 `[]`，确认今天的数据只存在内存中。

## AI 搭档

提示词「只用虚构标题，逐个帮我预测 `GET /tasks`、`POST /tasks` 和 `GET /tasks/:id` 的状态码。给一条畸形 JSON 练习，不要要求我分享真实数据。」自己执行 curl 并核对 HTTP 状态码和响应体。

# 第 09 天：实现原生 REST 下半场：更新和删除
原课：<https://xiguadev.com/node-60days/day-09>

## 今日先学

对已经存在的任务，需要修改状态或删除记录。`PATCH /tasks/:id` 表示对单条资源做局部更新，`DELETE /tasks/:id` 表示删除。更新请求只接收允许修改的 `status`，其值必须在 `todo`、`doing`、`done` 三个选项内。合法 JSON 也可能包含错误数据，因此语法检查和业务校验都要做。找不到资源时返回 `404`，输入不符合约定时返回 `400`。

下面是在第 08 天的 `day08.mjs` 基础上修改的完整版本，便于直接运行。所有任务都仍然只存内存中。更新与删除会修改当前数组的内容，浏览器或终端发出的下一次请求将看到更改。

## 跟做

把 `day08.mjs` 替换为下面版本。`findIndex()` 找到任务下标，没有找到时返回 `-1`。`splice(index, 1)` 从数组里移除一项。`Array.includes()` 检查输入状态是否出现在允许列表中。

```js
import { randomUUID } from 'node:crypto'
import { createServer } from 'node:http'

const tasks = []
const statuses = ['todo', 'doing', 'done']

async function readJson(req) {
  const chunks = []
  for await (const chunk of req) chunks.push(chunk)
  return JSON.parse(Buffer.concat(chunks).toString('utf8'))
}
function send(res, status, body) {
  res.writeHead(status, { 'content-type': 'application/json; charset=utf-8' })
  res.end(JSON.stringify(body))
}

const server = createServer(async (req, res) => {
  try {
    const url = new URL(req.url, 'http://127.0.0.1:3000')
    if (req.method === 'GET' && url.pathname === '/tasks') return send(res, 200, tasks)
    if (req.method === 'POST' && url.pathname === '/tasks') {
      try {
        const body = await readJson(req)
        if (typeof body.title !== 'string' || !body.title.trim()) {
          return send(res, 400, { error: 'title is required' })
        }
        const task = { id: randomUUID(), title: body.title.trim(), status: 'todo' }
        tasks.push(task)
        return send(res, 201, task)
      } catch {
        return send(res, 400, { error: 'invalid JSON' })
      }
    }
    const match = url.pathname.match(/^\/tasks\/([^/]+)$/)
    if (match && req.method === 'GET') {
      const task = tasks.find((item) => item.id === match[1])
      return task ? send(res, 200, task) : send(res, 404, { error: 'Task not found' })
    }
    if (match && req.method === 'PATCH') {
      try {
        const body = await readJson(req)
        if (!statuses.includes(body.status)) return send(res, 400, { error: 'invalid status' })
        const task = tasks.find((item) => item.id === match[1])
        if (!task) return send(res, 404, { error: 'Task not found' })
        task.status = body.status
        return send(res, 200, task)
      } catch {
        return send(res, 400, { error: 'invalid JSON' })
      }
    }
    if (match && req.method === 'DELETE') {
      const index = tasks.findIndex((item) => item.id === match[1])
      if (index === -1) return send(res, 404, { error: 'Task not found' })
      tasks.splice(index, 1)
      res.writeHead(204)
      return res.end()
    }
    return send(res, 404, { error: 'Not Found' })
  } catch (error) {
    console.error(error)
    return send(res, 500, { error: 'internal error' })
  }
})

server.listen(3000, '127.0.0.1', () => console.log('任务板：http://127.0.0.1:3000'))
```

按第 08 天方法新建任务并复制其 ID，再运行：

```bash
curl -i -X PATCH http://127.0.0.1:3000/tasks/ID -H 'content-type: application/json' -d '{"status":"doing"}'
curl -i -X DELETE http://127.0.0.1:3000/tasks/ID
curl -i http://127.0.0.1:3000/tasks
```

PATCH 返回 `200` 和更新后的任务，DELETE 返回 `204 No Content`（无响应体），最后的列表为 `[]`。同一条已删除 ID 再查，应返回 `404`。

## 练习

提交一个不存在的状态，再 PATCH 一个不存在的 ID。说明两者为什么不同，并用 DELETE 移除一条存在的任务。

## 参考答案与验收

`{"status":"blocked"}` 不在允许列表中，返回 `400 invalid status`。`{"status":"done"}` 格式合法，但若该 ID 不存在，就返回 `404 Task not found`。DELETE 成功返回 `204`，随后列表不再包含该条任务。若客户端试图通过 PATCH 改标题，本实现会忽略标题而只更改 `status`；这是刻意收窄更新字段的做法。

## AI 搭档

提示词「基于原生任务 API 和虚构 ID，出一道辨认 `400`、`404`、`204` 的 PATCH/DELETE 题。解释校验与资源查找的区别，不要要求数据库或认证。」手动发请求确认状态和数组变化。

# 第 10 天：里程碑：验收本机任务板 API
原课：<https://xiguadev.com/node-60days/day-10>

## 今日先学

到此里程碑，任务板可以接受 `GET /tasks`、`POST /tasks`、`GET /tasks/:id`、`PATCH /tasks/:id` 和 `DELETE /tasks/:id`。这足以练习资源建模、HTTP 方法、JSON 输入输出和状态码，但它还不是可供团队使用的产品：数据在内存、没有持久化、认证或输入大小上限，也没有完整测试。本课以命令行做一次可重复的端到端手工验收，明确项目目前做到哪一步。

建议在服务端终端启动第 09 天的版本，在另一个终端执行操作。每次启动都是新进程，数据从空数组开始。命令中的 `-i` 显示 HTTP 状态和响应头；响应的 ID 由服务端生成，因此必须读取结果后再填入后续命令。不要假设 ID 固定。

## 跟做

```bash
node day08.mjs
```

如果已经按第 09 天替换代码，这个文件就是包含全部方法的更新版本。再开一个终端，从空集合开始验证：

```bash
curl -i http://127.0.0.1:3000/tasks
curl -i -X POST http://127.0.0.1:3000/tasks -H 'content-type: application/json' -d '{"title":"里程碑验收"}'
```

确认列表是 `200` 和 `[]`。POST 是 `201`，复制返回 JSON 中的 `id`。下面以 `ID` 作为占位符，发送前必须替换成实际值：

```bash
curl -i http://127.0.0.1:3000/tasks/ID
curl -i -X PATCH http://127.0.0.1:3000/tasks/ID -H 'content-type: application/json' -d '{"status":"done"}'
curl -i -X DELETE http://127.0.0.1:3000/tasks/ID
curl -i http://127.0.0.1:3000/tasks/ID
```

依序应该得到 `200`、`200`、`204`、`404`。最后用 `GET /tasks` 确认列表为空。整个操作都发生在 `127.0.0.1`，没有把示例服务暴露到局域网或公网。

## 练习

在服务器重启前后各执行一次 `GET /tasks`。再提交一个缺少 `title` 的新建请求，检查状态和错误文本。

## 参考答案与验收

首次 GET 为 `200 []`。成功新建后列表有一项；服务器 `Ctrl+C` 结束并重新启动后，列表回到 `[]`，这验证了内存存储的范围。提交 `-d '{}'` 应返回 `400` 和 `title is required`。若答案不同，检查是否运行了本机的正确端口、启动的是第 09 天版本，并确认请求方法和路径拼写。

## AI 搭档

提示词「给我一张针对本机任务 API 的手工验收清单，逐个核对方法、路径、预期状态码及是否有响应体。使用虚构数据，不要声称我已经运行任何命令。」自己逐项执行，并记录实际结果。不要向 AI 粘贴身份信息、令牌或真实用户任务。


# 第 11 天：用 TypeScript 描述任务类型
原课：<https://xiguadev.com/node-60days/day-11>

## 今日先学

前十天用 JavaScript 的 `.mjs` 文件运行。TypeScript 在 JavaScript 上增加静态类型检查，可以在执行前发现一部分形状不一致的问题，但 Node.js 仍需要 JavaScript。今天开始写 `.ts`，使用 `tsx` 开发运行器，在命令行运行类型检查，并保留任务板的类型约定：`id` 和 `title` 是字符串，`status` 只能是 `todo`、`doing` 或 `done`。类型会在编译阶段检查，不会自动验证外部传来的 JSON；外部数据仍然必须在运行时校验。

## 跟做

在 `task-board` 根目录安装开发工具。Node 22 / 24 / 26 均适用（新项目优先 26）。`--save-dev` 表示这些工具只用于开发，不是任务板的运行时功能。

```bash
npm install --save-dev --save-exact typescript@5.8.3 tsx@4.19.3 @types/node@22
npx tsc --init
npm pkg set 'scripts.typecheck=tsc --noEmit'
npm pkg set 'scripts.day11=tsx day11.ts'
```

编辑 `tsconfig.json`，确保 `compilerOptions` 中包含以下设置（`npx tsc --init` 生成了其他选项时可以保留）。`@types/node` 提供 `node:http`、`Buffer` 和 `process` 等类型；这里使用 Node 22 的类型基线，后续示例也可在 Node 24 上运行。`types` 明确加载这份类型声明，不会代替运行时安装 Node.js：

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "types": ["node"],
    "strict": true,
    "noEmit": true,
    "skipLibCheck": true
  }
}
```

在 `day11.ts` 声明 `Task` 类型。联合类型用 `|` 列出有限选项。`: Task[]` 表明 `tasks` 是 Task 数组。函数的参数和返回值都写明类型，编辑器和 `tsc` 就能核对使用方式。

```ts
type Task = {
  id: string
  title: string
  status: 'todo' | 'doing' | 'done'
}

const tasks: Task[] = [
  { id: 't1', title: '整理需求', status: 'todo' },
  { id: 't2', title: '准备示例', status: 'doing' },
]

function countByStatus(items: Task[], status: Task['status']): number {
  return items.filter((task) => task.status === status).length
}

console.log(`待办任务 ${countByStatus(tasks, 'todo')}`)
```

```bash
npm run typecheck
npm run day11
```

类型检查应正常结束，脚本输出 `待办任务 1`。`filter()` 返回符合条件的新数组，`.length` 读取数量。若把状态拼成 `'blocked'` 或把 ID 改成数字，严格模式下 `tsc` 应报告类型错误。编辑器里的类型提示不是运行时校验，也不能阻止有人直接用 HTTP 发送错误 JSON。

## 练习

增加一条已完成任务，再增加函数 `countAll(items: Task[]): number` 返回任务总数，并在主流程用 `console.log` 打印 `总数 3`；只写函数不调用是看不到输出的。故意把一条状态改成 `'waiting'`，观察检查器报告。

## 参考答案与验收

可使用 `function countAll(items: Task[]): number { return items.length }`。添加任务后，`npm run day11` 应打印 `待办任务 1`，再打印总数 `3`。状态改成 `'waiting'` 后，`npm run typecheck` 应失败并指出该值不能赋给允许的联合类型；恢复为 `'done'` 后应通过。该验收只覆盖 TypeScript 类型检查和 tsx 执行，不代表已验证 HTTP 的运行时输入。

## AI 搭档

提示词「只针对虚构的 Task 类型，给我一个合法状态和一个类型错误状态，让我先判断 `tsc` 结果。提醒我 TypeScript 类型不负责校验 HTTP JSON。」不要分享真实任务，自己分别运行类型检查和脚本。

# 第 12 天：按 REST 约定改进错误和输入边界
原课：<https://xiguadev.com/node-60days/day-12>

## 今日先学

REST 风格接口要让资源路径、方法、状态码和响应表示保持一致。`GET /tasks` 表示读取集合；`POST /tasks` 创建资源并返回 `201 Created`；`GET /tasks/:id` 读取单项；`PATCH` 更新允许修改的字段；`DELETE` 成功删除可返回 `204 No Content`。错误响应应使用一致的 JSON 形状，并说明请求哪里不符合契约。请求体是外部输入，既要限制大小，也要处理畸形 JSON 与错误字段。

今天重做 API 为 TypeScript 单文件版本并加入 body 大小上限，仍然只监听 `127.0.0.1`。该内存 API 只供单用户本机练习，不包含认证、持久化、速率限制或多人协作安全性。

## 跟做

保存为 `api.ts`。将请求体上限设为 16 KiB，避免无界地拼接数据。`ApiError` 携带 HTTP 状态，异步请求处理最外层统一转为 JSON 错误响应。超限时不销毁 socket，而是抛出 `ApiError(413)`，由最外层 `catch` 返回客户端确实能收到的 413 响应。

```ts
import { randomUUID } from 'node:crypto'
import { createServer, type IncomingMessage, type ServerResponse } from 'node:http'

type Task = { id: string; title: string; status: 'todo' | 'doing' | 'done' }
class ApiError extends Error {
  constructor(public status: number, message: string) { super(message) }
}
const tasks: Task[] = []
const statuses = ['todo', 'doing', 'done'] as const

async function readJson(req: IncomingMessage): Promise<unknown> {
  const chunks: Buffer[] = []
  let bytes = 0
  for await (const chunk of req) {
    bytes += Buffer.byteLength(chunk)
    if (bytes > 16 * 1024) {
      req.resume()   // 丢弃剩余请求体，但不销毁共享 socket
      throw new ApiError(413, 'request body too large')
    }
    chunks.push(chunk as Buffer)
  }
  const text = Buffer.concat(chunks).toString('utf8')
  try { return JSON.parse(text) as unknown }
  catch { throw new ApiError(400, 'invalid JSON') }
}
function send(res: ServerResponse, status: number, body: unknown): void {
  res.writeHead(status, { 'content-type': 'application/json; charset=utf-8' })
  res.end(JSON.stringify(body))
}
function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value)
}

const server = createServer(async (req, res) => {
  try {
    const url = new URL(req.url ?? '/', 'http://127.0.0.1:3000')
    if (req.method === 'GET' && url.pathname === '/tasks') return send(res, 200, tasks)
    if (req.method === 'POST' && url.pathname === '/tasks') {
      const body: unknown = await readJson(req)
      if (!isRecord(body) || typeof body.title !== 'string' || !body.title.trim()) {
        throw new ApiError(400, 'title is required')
      }
      const task: Task = { id: randomUUID(), title: body.title.trim(), status: 'todo' }
      tasks.push(task)
      res.setHeader('location', `/tasks/${task.id}`)
      return send(res, 201, task)
    }
    const match = url.pathname.match(/^\/tasks\/([^/]+)$/)
    if (match && req.method === 'GET') {
      const task = tasks.find((item) => item.id === match[1])
      if (!task) throw new ApiError(404, 'task not found')
      return send(res, 200, task)
    }
    if (match && req.method === 'PATCH') {
      const body: unknown = await readJson(req)
      if (!isRecord(body) || !statuses.includes(body.status as typeof statuses[number])) {
        throw new ApiError(400, 'status must be todo, doing, or done')
      }
      const task = tasks.find((item) => item.id === match[1])
      if (!task) throw new ApiError(404, 'task not found')
      task.status = body.status as Task['status']
      return send(res, 200, task)
    }
    if (match && req.method === 'DELETE') {
      const index = tasks.findIndex((item) => item.id === match[1])
      if (index < 0) throw new ApiError(404, 'task not found')
      tasks.splice(index, 1)
      res.writeHead(204)
      return res.end()
    }
    throw new ApiError(404, 'route not found')
  } catch (error) {
    if (res.destroyed) return
    const status = error instanceof ApiError ? error.status : 500
    const message = error instanceof Error ? error.message : 'internal error'
    return send(res, status, { error: message })
  }
})
server.listen(3000, '127.0.0.1', () => console.log('任务板：http://127.0.0.1:3000'))
```

在 `package.json` 增加脚本并检查：

```bash
npm pkg set 'scripts.api=tsx api.ts'
npm run typecheck
npm run api
```

开另一个终端测列举和创建：

```bash
curl -i http://127.0.0.1:3000/tasks
curl -i -X POST http://127.0.0.1:3000/tasks -H 'content-type: application/json' -d '{"title":"检查 REST 响应"}'
curl -i -X POST http://127.0.0.1:3000/tasks -H 'content-type: application/json' -d '{bad}'
```

预期依次为 `200` 和 `[]`、`201` 且响应包含 `location: /tasks/<新 ID>`、`400` 和 `{"error":"invalid JSON"}`。新建标题需要非空字符串。请求体超过 16 KiB 时由外层 `catch` 统一返回 `413`，客户端确实能收到响应；这里不能用 `req.destroy()`，它会连共享 socket 一起销毁，使 413 无法送达。限制和异常处理可减少误用，但不是完整的生产安全方案。

## 练习

发送 `{"title":" "}` 和 `{"title":"边界","status":"done"}`。观察空标题的错误以及服务端是否采用客户端传来的状态。

## 参考答案与验收

空标题返回 `400` 和 `title is required`。第二个请求创建 `201`，返回的状态是 `todo`，因为服务端只接收标题，并自行设置初始状态。运行 `npm run typecheck` 应通过。这里的真实验收范围是 TypeScript 编译检查及手工 curl；没有测试超大请求，也没有声称经过自动化测试。

## AI 搭档

提示词「仅用虚构任务，检查这个 API 对畸形 JSON、空标题和非法状态的预期错误状态码。指出类型声明为何不等于运行时校验，不要编造实测结果。」自己运行 typecheck 和 curl 并记录实际输出；不要粘贴身份令牌或真实数据。

# 第 13 天：了解 Node 进程与 Worker
原课：<https://xiguadev.com/node-60days/day-13>

## 今日先学

Node.js 的进程对象 `process` 提供当前进程信息、命令行参数、环境变量和退出状态。API 服务在一个进程内运行；关闭或重启会清空当前的内存任务数组。环境变量适合把端口等配置从代码分开，但不要把秘密值放进示例或聊天。

JavaScript 默认在主线程执行。`worker_threads` 能把 CPU 密集型工作交给 Worker 执行，不是所有异步文件或网络任务的必备工具。Worker 有独立执行上下文，可以通过 `parentPort` 和创建它的线程交换消息。今天用小型计算演示：主线程提交数字，Worker 计算平方和后返回结果。

## 跟做

在项目根目录创建 `square-worker.mjs`：

```js
import { parentPort } from 'node:worker_threads'

parentPort.once('message', (limit) => {
  let sum = 0
  for (let value = 1; value <= limit; value += 1) sum += value * value
  parentPort.postMessage(sum)
  parentPort.close()
})
```

这是单次计算，Worker 用 `parentPort.once()` 只接收一条任务，发回结果后用 `parentPort.close()` 关闭消息端口，让 Worker 自然结束；主线程只接收一次结果并不会自动关闭 Worker。创建 `day13.mjs`。`new URL(..., import.meta.url)` 以当前模块文件的位置定位 Worker 脚本，不依赖从哪个目录执行命令。`worker.once('message', ...)` 只监听一次结果。`worker.once('error', ...)` 接住 Worker 启动或执行错误。`process.argv` 的前两项通常是 Node 可执行文件和脚本路径，因此自定义参数从下标 2 开始。

```js
import { Worker } from 'node:worker_threads'

const limit = Number(process.argv[2] ?? 100)
if (!Number.isInteger(limit) || limit < 1 || limit > 100000) {
  console.error('请输入 1 到 100000 之间的整数')
  process.exitCode = 1
} else {
  const worker = new Worker(new URL('./square-worker.mjs', import.meta.url))
  worker.once('message', (sum) => {
    console.log(`平方和 1..${limit} = ${sum}`)
  })
  worker.once('error', (error) => {
    console.error('Worker 错误：', error.message)
    process.exitCode = 1
  })
  worker.postMessage(limit)
}
```

```bash
node --version
node day13.mjs 10
node day13.mjs 0
```

第一条应显示已安装的兼容版本。第二条应显示 `平方和 1..10 = 385`，随后自行退出并回到终端提示符，退出码为 `0`，无需按 `Ctrl+C`。第三条应显示范围提示，进程退出状态为失败。这个极小计算仅用于观察消息传递；小任务创建 Worker 的开销可能大于直接计算的成本。

## 练习

把上限改为 `20` 再运行，手算 1 到 3 的平方和核对。试着不传参数，观察默认值。

## 参考答案与验收

`node day13.mjs 20` 应输出 `平方和 1..20 = 2870`。`node day13.mjs` 使用默认值 100，应该输出平方和 `338350`。结果可用公式 `n(n+1)(2n+1)/6` 复核。本示例没有基准测试，也没有把任务板的 HTTP 请求迁移到 Worker。

## AI 搭档

提示词「用 1 到 10 的虚构数字解释 Worker 消息从主线程发出到结果返回的步骤。再给我一个输入边界预测题，不要声称运行过代码。」用本机命令验算结果，不要分享个人系统信息或环境变量内容。

# 第 14 天：集中处理异常，用调试器定位问题
原课：<https://xiguadev.com/node-60days/day-14>

## 今日先学

错误不是都应该被悄悄忽略。可预期的输入问题要返回准确的 4xx 状态；意料之外的程序故障要记录必要上下文，并返回通用 500 信息，避免向客户端泄露堆栈或本机路径。`try/catch` 应围住可能失败的边界，在可恢复的位置处理错误；捕获后若没有恢复，就用明确的错误响应结束请求。Promise 异步失败也需要 `await` 所在的 `try/catch` 来接住。

Node 内建调试器可以单步检查变量。用 `--inspect-brk` 启动会暂停程序，等待调试客户端连接。不要将调试端口暴露到网络，也不要把秘密、身份令牌或含个人信息的请求体输出到日志。

## 跟做

新建 `debug-demo.mjs`。这段程序模拟从客户端收到空标题后，经过校验抛出可预期异常；`catch` 读取错误消息并返回可操作的退出状态。`error instanceof Error` 判断捕获值是否为标准错误对象。

```js
function createTask(title) {
  if (typeof title !== 'string' || !title.trim()) {
    throw new Error('title is required')
  }
  return { id: 'demo-1', title: title.trim(), status: 'todo' }
}

try {
  const task = createTask('   ')
  console.log('创建成功：', task)
} catch (error) {
  if (error instanceof Error) {
    console.error('输入未通过校验：', error.message)
  } else {
    console.error('发生未知错误')
  }
  process.exitCode = 1
}
```

```bash
node debug-demo.mjs
node --inspect-brk debug-demo.mjs
```

第一条应打印 `输入未通过校验： title is required`，退出码为 `1`。第二条会打印调试器 WebSocket 地址并暂停，按 `Ctrl+C` 结束。需要调试时，把 `node --inspect-brk` 后显示的地址复制到本机浏览器 DevTools 的 Remote Target，或使用支持 Node 的编辑器附加调试器；设置断点后单步运行并查看 `title`。普通验收不需要启动调试器。若已安装 `tsx`，也可在任务板 API 上运行 `node --inspect-brk ./node_modules/tsx/dist/cli.mjs api.ts`，但本课不要求同时连接外部调试工具。

## 练习

将 `'   '` 改成 `'检查错误路径'`，再次运行。保留校验分支，再尝试令 `createTask` 接收 `undefined`。

## 参考答案与验收

合法标题应打印 `创建成功` 和一个 `todo` 任务，命令退出码为 `0`。用 `createTask(undefined)` 时，`typeof` 校验为假，应该进入相同错误分支而非访问 `.trim()` 崩溃。先前的空字符串同样进入可预期异常路径。这个练习验证本地函数行为，不代表 API 的所有分支已被测试。

## AI 搭档

提示词「只用这段虚构的 `createTask`，按执行顺序解释错误从抛出到 catch 的路径。给我一条能触发边界错误的输入，不需要真实日志或系统信息。」自己运行两组输入；日志中只保留必要错误信息。

# 第 15 天：复盘并独立验收任务板
原课：<https://xiguadev.com/node-60days/day-15>

## 今日先学

前十五天从 JavaScript 基础过渡到 Node.js：变量、对象、数组、函数、条件和循环；模块及 npm；`fs`、`path`、`os`；事件、流和 `Buffer`；事件循环、Promise 与 `async/await`；原生 HTTP 和 REST；TypeScript、进程、Worker、异常与调试。如今的任务板以 `Task { id: string, title: string, status: 'todo' | 'doing' | 'done' }` 为核心，HTTP 服务器只绑定 `127.0.0.1`，只适合一位用户本机练习。

这一课不引入未教过的存储或框架功能，而是把关键步骤串起来做一次小型手工验收。当前 API 为 TypeScript 版本 `api.ts`，用 `tsx` 启动，数据只在内存中。开始前确认 `package.json` 已有 `api` 和 `typecheck` 脚本，且 `api.ts` 与第 12 天示例一致。

## 跟做

在项目终端运行类型检查，再启动服务：

```bash
npm run typecheck
npm run api
```

`typecheck` 应成功结束，服务端应显示任务板地址。开另一个终端执行列举和新建。所有数据都是虚构的示例内容：

```bash
curl -i http://127.0.0.1:3000/tasks
curl -i -X POST http://127.0.0.1:3000/tasks -H 'content-type: application/json' -d '{"title":"完成 Day 15 验收"}'
```

确认空集合为 `200`。新建为 `201`，响应里的 `status` 初值应为 `todo`，`location` 头中含该条资源路径（代码里用 `res.setHeader('location', ...)` 写的是小写，`curl -i` 原样输出小写，HTTP 头名本就不区分大小写）。复制响应里的 ID，替换以下命令中的 `ID`：

```bash
curl -i http://127.0.0.1:3000/tasks/ID
curl -i -X PATCH http://127.0.0.1:3000/tasks/ID -H 'content-type: application/json' -d '{"status":"doing"}'
curl -i -X PATCH http://127.0.0.1:3000/tasks/ID -H 'content-type: application/json' -d '{"status":"done"}'
curl -i -X DELETE http://127.0.0.1:3000/tasks/ID
curl -i http://127.0.0.1:3000/tasks/ID
```

预期依序得到 `200`、`200`、`200`、`204`、`404`。再发 `POST` 空标题应得到 `400`，畸形 JSON 也应得到 `400`。结束服务器进程，重新启动后 GET 集合应为 `[]`。这验证了当前阶段的 REST 行为，并明确证明重启清空数据是内存存储的既定限制。

## 练习

不参考前面的命令，写下每种请求的方法、资源路径和预期状态码。执行后为每一步记录实际状态码，并解释 `200` 和 `201` 的用途区别，以及重启后任务为什么消失。

## 参考答案与验收

列集合 `GET /tasks` 为 `200`；创建 `POST /tasks` 为 `201`；读取单项 `GET /tasks/:id` 为 `200`；状态更新 `PATCH /tasks/:id` 为 `200`；删除 `DELETE /tasks/:id` 为 `204`；删除后再读为 `404`；无效输入为 `400`。`201` 表示新资源已创建，`200` 表示请求成功并有响应表示，`204` 表示成功且没有响应体。数据在进程内存中，进程重启后自然回到空数组。上面是预期结果，不代表已经代替读者执行；本讲义实际验证范围仅为保存时的内容编写，具体运行结果由读者在本机按命令验收。

## AI 搭档

提示词「请以代码审阅者身份，基于我贴出的脱敏 API 片段生成一份 Day 15 手工验收清单，包含方法、路径、预期状态码和待我确认的结果。不要假设命令已经执行，不要索要真实用户数据、口令或令牌。」按清单自己运行命令，保存脱敏的状态码记录。遇到错误时只分享最小复现和删去本机用户名、私有路径及请求秘密后的错误文本。


# 第 16 天：用 Nest 模块搭起博客 API

原课：<https://xiguadev.com/node-60days/day-16>

## 今日先学

课程主线项目叫「协作任务板」。第 16–30 天先独立完成一份轻量博客 API，练熟 Nest 的请求处理和数据库接入。沿用此前 Task 练习的 `Controller → Service → 数据访问` 分层思路，本阶段使用 `Post`（文章）和 `Author`（作者）。第 46 天起再把这套做法带回协作任务板，按任务板的业务规则重新建模。

`Controller` 管 HTTP 路径和参数，`Service` 管业务动作，`Module` 负责把它们接在一起。Nest 根据构造函数的类型查找已注册的 provider，把同一个服务实例交给调用它的 controller。今天先用服务中的数组作为临时数据源。

## 跟做

统一使用 Node.js **22 / 24 / 26**（任一受支持 LTS，新项目优先 26）、npm、Nest **11.x**。后半段使用 PostgreSQL **16.x** 和 Prisma **6.19.0**。在工作目录运行 `node -v` 和 `npm -v` 核对环境，再建立独立项目。后续命令均在 `mini-blog-api` 根目录执行。`curl` 示例按 Bash 编写，Windows 请使用 Git Bash。

```bash
npx --yes @nestjs/cli@11 new mini-blog-api --package-manager npm --skip-git
cd mini-blog-api
```

创建 `src/posts/post.ts`。示例的 `id` 和 `authorId` 是正整数，时间使用 `Date`，经过 JSON 序列化后是 ISO 8601 字符串。

```ts
export interface Post {
  id: number;
  title: string;
  body: string;
  authorId: number;
  createdAt: Date;
  publishedAt: Date | null;
}
```

```ts
// src/posts/posts.service.ts
import { Injectable } from '@nestjs/common';
import type { Post } from './post';

@Injectable()
export class PostsService {
  private readonly posts: Post[] = [];

  list(): Post[] {
    return [...this.posts];
  }
}
```

```ts
// src/posts/posts.controller.ts
import { Controller, Get } from '@nestjs/common';
import { PostsService } from './posts.service';

@Controller('posts')
export class PostsController {
  constructor(private readonly posts: PostsService) {}

  @Get()
  list() {
    return this.posts.list();
  }
}
```

```ts
// src/posts/posts.module.ts
import { Module } from '@nestjs/common';
import { PostsController } from './posts.controller';
import { PostsService } from './posts.service';

@Module({ controllers: [PostsController], providers: [PostsService] })
export class PostsModule {}
```

```ts
// src/app.module.ts（替换）
import { Module } from '@nestjs/common';
import { PostsModule } from './posts/posts.module';

@Module({ imports: [PostsModule] })
export class AppModule {}
```

在脚手架的 `src/main.ts` 保留 `NestFactory.create(AppModule)`，将监听改为 `await app.listen(3000, '127.0.0.1')`。运行 `npm run start:dev`，另开终端请求 `curl -i http://127.0.0.1:3000/posts`。预期是 `200` 和 `[]`。端口已被占用时先停止旧服务，确保请求命中当前 Nest 项目。

## 练习

暂时从 `PostsModule.providers` 移除 `PostsService`，观察热重启的输出，再恢复配置。

## 参考答案与验收

缺少 provider 时，Nest 启动报错，提示无法解析 `PostsController` 对 `PostsService` 的依赖。恢复 `providers: [PostsService]` 后，再请求 `/posts`，应恢复 `200` 和 `[]`。这个错误发生在应用组装阶段，早于 HTTP 请求。

## AI 搭档

只给 AI 看这四个类的名称和构造函数签名，请它画一张依赖图，标明哪个模块注册服务。使用课程示例，别粘贴密码或业务数据。

# 第 17 天：追踪 Nest 请求生命周期

原课：<https://xiguadev.com/node-60days/day-17>

## 今日先学

一次正常请求按 `Middleware → Guard → Interceptor 入站 → Pipe → Controller → Service → Interceptor 出站` 的顺序走。中间件适合记录请求概况，守卫决定能否进入路由，管道处理参数，拦截器包围处理过程。未处理的异常会交给异常过滤器。守卫提前拒绝时，后续的处理器和参数管道都不会执行。

这里用两个短日志区分请求已经到达与处理已经结束。`res.once('finish')` 在响应写完时读取最终 HTTP 状态，避免在入站时记下默认状态。日志只记录方法和状态，课程中的请求体、查询串和认证头都无需记录。

## 跟做

新增 `src/common/trace.middleware.ts`，再用 `configure` 挂到应用。

```ts
// src/common/trace.middleware.ts
import { Injectable, NestMiddleware } from '@nestjs/common';
import type { NextFunction, Request, Response } from 'express';

@Injectable()
export class TraceMiddleware implements NestMiddleware {
  use(req: Request, res: Response, next: NextFunction) {
    console.log('middleware in', req.method);
    res.once('finish', () => console.log('response finish', res.statusCode));
    next();
  }
}
```

```ts
// src/app.module.ts（替换）
import { MiddlewareConsumer, Module, NestModule } from '@nestjs/common';
import { TraceMiddleware } from './common/trace.middleware';
import { PostsModule } from './posts/posts.module';

@Module({ imports: [PostsModule] })
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer.apply(TraceMiddleware).forRoutes('{*path}');
  }
}
```

在 `src/posts/posts.service.ts` 增加 `NotFoundException` 的导入和 `get` 方法。`find` 得不到结果就抛出 404。这里列表为空，仍可观察路由和参数管道的行为。把 `Get` 保留在 controller 导入列表，另加 `Param`、`ParseIntPipe`，并添加 `get` 路由。

```ts
// PostsService 类中
get(id: number): Post {
  const post = this.posts.find((item) => item.id === id);
  if (!post) throw new NotFoundException('文章不存在');
  return post;
}
```

```ts
// PostsController 类中
@Get(':id')
get(@Param('id', ParseIntPipe) id: number) {
  console.log('controller get', id);
  return this.posts.get(id);
}
```

访问 `/posts/1`，终端预期依次出现 `middleware in GET`、`controller get 1`、`response finish 404`。`ParseIntPipe` 已把路径字符串转换为数字。第 18 天会补上正整数与取值上限，第 19 天再统一响应格式。

## 练习

用 `curl -i http://127.0.0.1:3000/posts/abc` 请求同一路由。根据日志判断请求在哪一层终止。

## 参考答案与验收

预期状态 `400`，响应含 `Validation failed (numeric string is expected)`。此请求有 `middleware in GET` 和 `response finish 400`，没有 `controller get …`。路由匹配后，参数管道先拒绝了 `abc`。再访问 `/posts/1`，确认合法数字能进入控制器。完成后删掉方法里的 `console.log('controller get', id)`，保留中间件。

## AI 搭档

把两组课程日志的顺序告诉 AI，让它各出一道题，判断把功能放进守卫、管道还是拦截器。只分享示例日志，别粘贴密码或真实请求数据。

# 第 18 天：用 DTO 校验 JSON 请求体

原课：<https://xiguadev.com/node-60days/day-18>

## 今日先学

`CreatePostDto` 描述客户端提交的字段。TypeScript 的类型检查发生在编译时，实际收到的 JSON 需要运行时验证。把 DTO 写成类，Nest 才能在运行时读取装饰器。标题要先去首尾空白，再校验长度，因此纯空白标题会失败。正文保留版式，允许 1–5000 个字符。`authorId` 必须是 JSON 数字，且落在 PostgreSQL `integer` 的正值范围。今天用课程固定作者 Ada（ID `1`）。

## 跟做

运行 `npm install class-validator class-transformer`。在 `src/main.ts` 导入 `ValidationPipe`，在 `app.listen` 前注册全局管道。`whitelist` 定义允许进入的字段，`forbidNonWhitelisted` 让多余字段直接失败。`transform` 能构造 DTO 实例，下面没有启用数字的隐式转换。

```ts
app.useGlobalPipes(new ValidationPipe({
  transform: true,
  whitelist: true,
  forbidNonWhitelisted: true,
}));
```

```ts
// src/posts/dto/create-post.dto.ts
import { Transform } from 'class-transformer';
import { IsInt, IsString, Length, Max, Min } from 'class-validator';

export class CreatePostDto {
  @Transform(({ value }) => typeof value === 'string' ? value.trim() : value)
  @IsString()
  @Length(1, 120)
  title!: string;

  @IsString()
  @Length(1, 5000)
  body!: string;

  @IsInt()
  @Min(1)
  @Max(2_147_483_647)
  authorId!: number;
}
```

在 `PostsService` 中导入 `CreatePostDto`（这里可用类型导入），添加下列成员。把原 `get` 方法中调用 `find` 的前一行也补上 `this.assertId(id)`，坏格式由 `ParseIntPipe` 处理，越界值由此检查。

```ts
// PostsService 类中，另从 @nestjs/common 导入 BadRequestException
private nextId = 1;

private assertId(id: number) {
  if (!Number.isInteger(id) || id < 1 || id > 2_147_483_647) {
    throw new BadRequestException('文章 ID 超出范围');
  }
}

create(dto: CreatePostDto): Post {
  if (dto.authorId !== 1) throw new NotFoundException('作者不存在');
  const post: Post = {
    id: this.nextId++, title: dto.title, body: dto.body,
    authorId: dto.authorId, createdAt: new Date(), publishedAt: null,
  };
  this.posts.push(post);
  return post;
}
```

在 `PostsController` 中导入 `Body`，把 `@nestjs/common` 的 `Post` 装饰器按下例引入。控制器的 DTO 必须普通导入，运行时管道要用到这个类。

```ts
// PostsController 中导入 Post 装饰器与 CreatePostDto 后，添加方法
@Post()
create(@Body() dto: CreatePostDto) {
  return this.posts.create(dto);
}
```

```bash
curl -i http://127.0.0.1:3000/posts -H 'Content-Type: application/json' \
  -d '{"title":"  Hello  ","body":"My draft","authorId":1}'
```

空进程首次创建预期为 `201`、`id: 1`、`title: "Hello"`、`publishedAt: null`。随后 `GET /posts/1` 返回刚保存的文章。作者 `2` 当前返回 `404`。

## 练习

把请求中的 `authorId` 从数字 `1` 改成字符串 `"1"`，再尝试添加 `publishedAt` 字段。

## 参考答案与验收

仅改成字符串时预期 `400`，`message` 数组含 `authorId must be an integer number`。恢复数字并只加 `"publishedAt":null` 时也预期 `400`，常见信息为 `property publishedAt should not exist`。两次都未新增文章。`GET /posts/0` 应因范围检查返回 `400`。

## AI 搭档

请 AI 根据三个 DTO 字段设计边界输入表，至少列出空白标题、最长合法标题和数字字符串。只给它字段规则和虚构输入，别粘贴密码或业务数据。

# 第 19 天：区分成功响应与异常响应

原课：<https://xiguadev.com/node-60days/day-19>

## 今日先学

HTTP 状态码供客户端做第一层判断。本项目把成功数据放在 `{data: ...}`，把失败原因放在 `{error: {statusCode, message}}`。校验失败时 `message` 可以是字符串数组，其他已知异常通常是一条字符串。拦截器集中包装成功结果，过滤器集中处理未捕获异常。未知错误保留 `500` 并返回固定文案，调用方不会收到堆栈或数据库细节。

## 跟做

在 `src/common` 新建下面两份文件。拦截器只用 `map` 修改成功值，`next.handle()` 发出的异常依然会交给过滤器。后续控制器继续返回业务对象，交给 Nest 统一写响应。

```ts
// src/common/data.interceptor.ts
import { CallHandler, ExecutionContext, Injectable, NestInterceptor } from '@nestjs/common';
import { map } from 'rxjs';

@Injectable()
export class DataInterceptor implements NestInterceptor {
  intercept(_context: ExecutionContext, next: CallHandler) {
    return next.handle().pipe(map((data: unknown) => ({ data })));
  }
}
```

```ts
// src/common/http-error.filter.ts
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, Logger } from '@nestjs/common';
import type { Response } from 'express';

@Catch()
export class HttpErrorFilter implements ExceptionFilter {
  private readonly logger = new Logger(HttpErrorFilter.name);

  catch(exception: unknown, host: ArgumentsHost) {
    const res = host.switchToHttp().getResponse<Response>();
    if (res.headersSent) {
      res.end();
      return;
    }

    let statusCode = 500;
    let message: string | string[] = '服务暂时不可用';
    if (exception instanceof HttpException) {
      statusCode = exception.getStatus();
      const payload = exception.getResponse();
      message = typeof payload === 'string'
        ? payload
        : (payload as { message?: string | string[] }).message ?? exception.message;
    } else {
      const name = exception instanceof Error ? exception.name : 'UnknownError';
      this.logger.error(`Unhandled exception (${name})`);
    }

    res.status(statusCode).json({ error: { statusCode, message } });
  }
}
```

在 `src/main.ts` 导入这两个类，在 `app.listen` 前保留全局校验，并追加 `app.useGlobalInterceptors(new DataInterceptor())` 和 `app.useGlobalFilters(new HttpErrorFilter())`。重新执行第 18 天的成功创建请求，仍是 `201`，文章现在在 `data` 下。请求不存在的 `/posts/999999` 应得到 `404` 和 `{"error":{"statusCode":404,"message":"文章不存在"}}`。

前三天是增量修改，很容易漏掉其中一步。下面给出合并后的完整 `src/main.ts`，可直接覆盖核对：`ValidationPipe`、拦截器、异常过滤器三者缺一，成功/错误响应格式就对不上。

```ts
// src/main.ts（第 16/18/19 天合并后的完整版本）
import { ValidationPipe } from '@nestjs/common';
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { DataInterceptor } from './common/data.interceptor';
import { HttpErrorFilter } from './common/http-error.filter';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  // 第 18 天：DTO 校验，缺了它 whitelist 与 DTO 装饰器全部失效
  app.useGlobalPipes(new ValidationPipe({
    whitelist: true, forbidNonWhitelisted: true, transform: true,
  }));
  // 第 19 天：成功响应包装与异常响应统一
  app.useGlobalInterceptors(new DataInterceptor());
  app.useGlobalFilters(new HttpErrorFilter());
  await app.listen(3000, '127.0.0.1');
}
bootstrap();
```

## 练习

临时在 `PostsService.list()` 中把 `return` 替换为 `throw new Error('do-not-echo')`，请求列表并检查客户端和终端。完成后恢复原方法。

## 参考答案与验收

`GET /posts` 预期 `500` 和 `{"error":{"statusCode":500,"message":"服务暂时不可用"}}`，响应体搜索不到 `do-not-echo`。终端可见 `Unhandled exception (Error)`，中间件记录最终状态 `500`。恢复后，列表回到 `200` 和 `{ "data": [] }`（空进程）。

## AI 搭档

请 AI 扮演前端开发者，根据示例协议区分表单错误与服务故障，并写出两条提示文案。使用假响应，别粘贴密码、业务数据或线上错误堆栈。

# 第 20 天：完成内存版博客里程碑

原课：<https://xiguadev.com/node-60days/day-20>

## 今日先学

今天补齐文章更新与删除。`PATCH` 只修改请求中出现的字段，`title` 和 `body` 可以分别提交，`null` 会被拒绝。`authorId` 在创建时确定，发布时间后面由发布动作决定。删除返回 `200` 和被删 ID，客户端可据此移除列表上的那条文章。所有写入目前只存在当前 Nest 进程的数组里，重启后即清空。

## 跟做

创建更新 DTO。`ValidateIf` 只在字段缺省时跳过验证。课程约定空对象返回 `400`，在 Service 里检查，避免无意义的更新。

```ts
// src/posts/dto/update-post.dto.ts
import { Transform } from 'class-transformer';
import { IsString, Length, ValidateIf } from 'class-validator';

export class UpdatePostDto {
  @ValidateIf((_object, value) => value !== undefined)
  @Transform(({ value }) => typeof value === 'string' ? value.trim() : value)
  @IsString()
  @Length(1, 120)
  title?: string;

  @ValidateIf((_object, value) => value !== undefined)
  @IsString()
  @Length(1, 5000)
  body?: string;
}
```

在 `src/posts/posts.service.ts` 导入 `UpdatePostDto` 类型并追加两个方法。复用 `get` 做 ID 范围和文章存在性检查。`delete` 找到目标对象后借助 `splice` 删除一项，仍保留自增计数，避免在同一次进程内重用刚删掉的 ID。

```ts
// PostsService 类中
update(id: number, dto: UpdatePostDto): Post {
  if (dto.title === undefined && dto.body === undefined) {
    throw new BadRequestException('请至少提供 title 或 body');
  }
  const post = this.get(id);
  if (dto.title !== undefined) post.title = dto.title;
  if (dto.body !== undefined) post.body = dto.body;
  return post;
}

delete(id: number): { id: number } {
  const post = this.get(id);
  this.posts.splice(this.posts.indexOf(post), 1);
  return { id };
}
```

在 `src/posts/posts.controller.ts` 从 `@nestjs/common` 加入 `Delete`、`Patch` 并普通导入 `UpdatePostDto`。新增方法保持路由层薄，领域决策仍留给 Service。

```ts
// PostsController 类中
@Patch(':id')
update(@Param('id', ParseIntPipe) id: number, @Body() dto: UpdatePostDto) {
  return this.posts.update(id, dto);
}

@Delete(':id')
delete(@Param('id', ParseIntPipe) id: number) {
  return this.posts.delete(id);
}
```

## 练习

先在空进程里发创建请求，再只改标题，然后删除并检查详情。如果创建返回的 ID 与示例不同，请把后续 URL 中的 `1` 换成实际的 `data.id`。

```bash
curl -i http://127.0.0.1:3000/posts -H 'Content-Type: application/json' \
  -d '{"title":"Draft","body":"Original body","authorId":1}'
curl -i -X PATCH http://127.0.0.1:3000/posts/1 -H 'Content-Type: application/json' \
  -d '{"title":"Revised"}'
curl -i -X DELETE http://127.0.0.1:3000/posts/1
curl -i http://127.0.0.1:3000/posts/1
```

## 参考答案与验收

按顺序预期 `201 → 200 → 200 → 404`。更新结果的 `data.title` 是 `Revised`，`data.body` 仍为 `Original body`。删除返回 `{"data":{"id":1}}`。另建一篇文章后提交 `{}` 或 `{"title":null}`，两次都应得到 `400`。重启进程再访问列表，预期 `{"data":[]}`。保存这组 HTTP 用例，第 27 天换数据库后用于回归。第 28 天会把列表扩展为分页对象。

## AI 搭档

把五个路由和预期状态交给 AI，请它补一条能发现部分更新覆盖原字段的手工验收步骤。只用本课生成的样例，别粘贴密码或业务数据。


# 第 21 天：PostgreSQL 的表与基本查询

原课：<https://xiguadev.com/node-60days/day-21>

## 今日先学

PostgreSQL 是关系数据库：表保存同类行，列定义数据类型和约束。`PRIMARY KEY` 唯一标识一行，`NOT NULL` 禁止缺值，`FOREIGN KEY` 限制引用不存在的作者。今日把 Day20 的内存文章迁到数据库概念中，但暂不改 Nest 代码。命名保持 `authors`、`posts`；作者 Ada 的 ID 为 1，内容为测试数据。不要把本机连接密码放进命令历史、讲义或提交仓库。

## 跟做

本课程使用 PostgreSQL 16.x。若已有可访问的数据库，打开 `psql` 连到自己的空白练习库；不要求安装或启动数据库软件。下列 SQL 可在 `psql` 提示符输入。若看到 `relation does not exist`，先检查是否选错数据库；本文未执行数据库操作。

```sql
CREATE TABLE authors (
  id integer GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  name varchar(80) NOT NULL
);
CREATE TABLE posts (
  id integer GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  title varchar(120) NOT NULL CHECK (length(btrim(title)) > 0),
  body text NOT NULL,
  author_id integer NOT NULL REFERENCES authors(id),
  created_at timestamptz NOT NULL DEFAULT now(),
  published_at timestamptz
);
INSERT INTO authors (id, name) VALUES (1, 'Ada');
INSERT INTO posts (title, body, author_id)
VALUES ('Nest notes', 'A small draft', 1);
```

读取和修改：

```sql
SELECT id, title, created_at, published_at FROM posts ORDER BY id;
UPDATE posts SET title = 'Nest and data' WHERE id = 1;
DELETE FROM posts WHERE id = 1;
```

预期第一条查询至少返回 `Nest notes`，更新后标题为 `Nest and data`。删除要谨慎：没有 `WHERE` 的删除会清空整张表。若重复执行插入作者遇到主键冲突，先检查 `SELECT * FROM authors WHERE id = 1;`，不要为了消除错误就删表。连接 Nest 时 URL 形如 `postgresql://USER:PASSWORD@localhost:5432/mini_blog?schema=public`，其中凭据用你自己的环境变量提供。这里的 `mini_blog` 只是第 21–24 天手写 SQL 练习用的库名示例；第 25 天会另建独立的 `mini_blog_prisma` 给 Prisma。两天互不影响，不要把手写表误当成 Prisma 迁移生成的库。

## 练习

分别执行下面三条插入，比较不存在的作者、`NULL` 标题和空字符串标题。每条预期失败，按 `psql` 默认的自动提交模式逐条执行，不要把它们包进同一个事务。

```sql
INSERT INTO posts (title, body, author_id) VALUES ('Bad author', 'Draft', 999);
INSERT INTO posts (title, body, author_id) VALUES (NULL, 'Draft', 1);
INSERT INTO posts (title, body, author_id) VALUES ('', 'Draft', 1);
```

## 参考答案与验收

三条依次应因外键、`NOT NULL`、`CHECK` 约束失败。`NOT NULL` 只拒绝 `NULL`，`varchar(120)` 只限制长度，它们本身都允许 `''`；这里额外的 `CHECK (length(btrim(title)) > 0)` 拒绝空串和全由普通空格组成的标题。Nest 的 DTO 仍负责更完整的输入校验。检查 `SELECT count(*) FROM posts;`，按前面已删除示例文章的步骤应为 `0`；再确认 `SELECT id, name FROM authors;` 有 Ada。验收目标是让数据库保证“每篇文章有作者”，并区分缺值和空字符串。若已按旧版建表，先检查并修正不满足规则的标题，再执行 `ALTER TABLE posts ADD CONSTRAINT posts_title_nonblank CHECK (length(btrim(title)) > 0);`，无需重建表。

## 原版对照阅读

原版 Day21 展开更细，讲"为什么是 PostgreSQL"，本讲义只保留了建表和连接。补三点原理，能解释后面很多设计选择：

- **主键选自增还是 UUID**：自增 `BIGSERIAL` 紧凑、索引局部性好，但会暴露业务量、且分库分表时主键会冲突；UUID 全局唯一、便于合并数据，但 128 位随机值会写坏 B-tree 的局部性、索引更大。单机博客用自增即可，分布式或需要对外暴露不可猜 ID 时选 UUID（可用 `uuidv7` 兼顾时间有序）。
- **把业务规则写进 schema**：`NOT NULL`、`UNIQUE`、外键和 `CHECK` 是最后一道防线——即使所有应用代码都有 bug，数据库也不会接受非法状态。能在 schema 表达的规则就别只写在应用层。
- **ACID 不是抽象词**：原子性让"转账"要么全成要么全不成；一致性保证约束不被破坏；隔离性让并发事务互不干扰；持久性保证提交后断电不丢。事务在 PostgreSQL 里以 `BEGIN` / `COMMIT` 包裹，Prisma 用 `$transaction`。

`TIMESTAMPTZ` 存的是带时区的绝对时间点，写入时转成 UTC、读取时按会话时区显示，比 `TIMESTAMP` 更适合多时区系统。

## AI 搭档

请 AI 对照外键、`NOT NULL` 和 `CHECK` 约束解释各自能拦截什么坏数据，并写出一个检查查询。只给虚构表结构，不要粘贴连接串、密码或真实业务数据。

# 第 22 天：用 JOIN、子查询与聚合查询文章

原课：<https://xiguadev.com/node-60days/day-22>

## 今日先学

规范化后，文章只存 `author_id`，作者姓名留在 `authors`。查询展示文章和作者时用 `JOIN`，不要复制姓名到每行文章。子查询可筛选满足汇总条件的作者。聚合函数 `count`、`avg` 把多行归并成统计；非聚合列需出现在 `GROUP BY` 中。以下使用 Day21 的空练习库，先准备两位作者和三篇文章。

## 跟做

```sql
INSERT INTO authors (id, name) VALUES (2, 'Lin');
INSERT INTO posts (title, body, author_id, published_at) VALUES
  ('First', 'Draft text', 1, NULL),
  ('Second', 'Ready text', 1, now()),
  ('Third', 'Ready text', 2, now());
```

`JOIN` 默认只返回两侧都匹配的行；`LEFT JOIN` 即使没有文章也保留作者。`count(p.id)` 在左连接的空行上为 0，不能误用 `count(*)`。

```sql
SELECT p.id, p.title, a.name AS author
FROM posts AS p
JOIN authors AS a ON a.id = p.author_id
ORDER BY p.id;

SELECT a.id, a.name, count(p.id) AS post_count
FROM authors AS a
LEFT JOIN posts AS p ON p.author_id = a.id
GROUP BY a.id, a.name
ORDER BY a.id;

SELECT name FROM authors
WHERE id IN (SELECT author_id FROM posts WHERE published_at IS NOT NULL);
```

第一条应呈现 `First/Ada`、`Second/Ada`、`Third/Lin`。第二条计数为 Ada `2`、Lin `1`。第三条只返回有已发布文章的作者。若结果重复，先检查联结条件是否遗漏 `a.id = p.author_id`。删除测试数据时注意保留 ID 1 的 Ada。Day25 会切换到独立空库，并用 seed 重新建立 ID 1 的 Ada，不会自动复制此库的数据。

## 练习

写一条查询，列出每位作者的已发布文章数，零篇作者也要显示。

## 参考答案与验收

```sql
SELECT a.name, count(p.id) AS published_count
FROM authors a
LEFT JOIN posts p
  ON p.author_id = a.id AND p.published_at IS NOT NULL
GROUP BY a.id, a.name
ORDER BY a.id;
```

把发布条件写在 `ON` 中，Ada 与 Lin 预期都为 `1`。若写在 `WHERE`，没有发布文章的作者会被过滤，和“零篇也显示”冲突。数据尚未导入时先执行 `SELECT` 查看日期非空行。

## 原版对照阅读

原版 Day22 展开更细，拆解 JOIN，本讲义只演示了三种 JOIN 的写法。三个最容易写错的点：

- **JOIN 的心智模型**：`A JOIN B` 先产生两表的笛卡尔积（行数 = A×B），`ON` 条件再逐行过滤，`INNER` 丢弃不匹配的、`LEFT` 保留左表并给右表补 `NULL`。先按这个顺序在纸上推一遍，结果就不再神秘。
- **`ON` 还是 `WHERE`**：对 `LEFT JOIN`，把条件放 `ON` 里，不匹配的行仍保留（右表补 `NULL`）；放 `WHERE` 里会过滤掉这些 `NULL` 行，等于把 `LEFT` 变成了 `INNER`。"只取某类右表行的左表全量"必须放 `ON`。
- **`WHERE` / `GROUP BY` / `HAVING` 的作用阶段**：`WHERE` 在分组前过滤行，`GROUP BY` 聚合，`HAVING` 在分组后过滤组。因此 `WHERE` 里不能用聚合函数，`HAVING` 可以。`COUNT(*)` 数行，`COUNT(col)` 跳过 `NULL`，`COUNT(DISTINCT col)` 去重计数。

复杂报表可用 CTE（`WITH x AS (...)`）把查询拆成有名字的步骤，可读性和可调试性都远好于层层嵌套的子查询。

## AI 搭档

给 AI 以上三张查询结果的字段说明，让它出一道区分 `ON` 与 `WHERE` 的题并给出反例。不得输入数据库凭据或真实业务数据。

# 第 23 天：为常用查询设计索引

原课：<https://xiguadev.com/node-60days/day-23>

## 今日先学

索引帮助数据库定位行，代价是占磁盘且写入时也要维护。不要给每列盲目加索引；先从真实查询的筛选、排序和联结条件判断。主键与唯一约束通常已自动建立索引。文章列表按作者过滤并按创建时间倒序，单列索引未必能同时有效支持两项，所以可考虑 `(author_id, created_at DESC)` 复合索引。小表上查询计划可能仍选择顺序扫描，这是合理的；不能把“看见 Index Scan”当唯一验收标准。

## 跟做

先查看当前计划，再建索引比较。`EXPLAIN` 只规划不实际执行；`ANALYZE` 会运行查询并统计，因此只在可丢弃的练习数据上使用。

```sql
EXPLAIN
SELECT id, title, created_at
FROM posts
WHERE author_id = 1
ORDER BY created_at DESC
LIMIT 10;

CREATE INDEX posts_author_created_idx
ON posts (author_id, created_at DESC);

EXPLAIN
SELECT id, title, created_at
FROM posts
WHERE author_id = 1
ORDER BY created_at DESC
LIMIT 10;
```

复合索引列次序很重要：前导列 `author_id` 支持按作者查找；只按时间排序时未必能充分利用该索引。查询是否使用索引取决于统计信息、表大小、条件选择性和 PostgreSQL 版本。不要为练习清空表，也不要在生产表上照抄建索引。

## 练习

用 `\d posts` 查看已有索引，再运行上面两次 `EXPLAIN`，记录计划。确认相同索引不会被重复创建。

## 参考答案与验收

检查表定义应看到主键索引和 `posts_author_created_idx`。小表计划仍显示 `Seq Scan` 不代表建索引失败，使用 `\di posts*` 确认索引存在即可。再次创建同名索引会报 `relation already exists`；这是重复执行的提示，不代表原查询出错。若想改列设计，先在个人练习库谨慎执行 `DROP INDEX posts_author_created_idx;` 再重建。

## 原版对照阅读

原版 Day23 展开更细，讲索引，本讲义只要求"建索引、看变快"。补四点，让"为什么这个索引有效"可推理：

- **B+ 树为什么是 O(log N)**：PG 默认索引是平衡多叉（B+）树，不是二叉树。每个内部节点按扇出（通常数百个键）逐层分流，100 万行大约只需 3~4 层、3~4 次磁盘读就能定位到叶子，而不是「每次排除一半、约 20 次比较」。叶子节点存索引列值加指向数据行的指针，并用双向链表串起来，所以范围扫描和 `ORDER BY` 能顺序读叶子，不必回到上层。
- **怎么读 `EXPLAIN`**：看 `Seq Scan`（全表扫描，通常是要优化的信号）、`Index Scan`（走索引回表）、`Index Only Scan`（索引覆盖，不回表，最快）；再比较 `cost`（规划器估算，相对值）和 `rows`（预估返回行数）。加 `ANALYZE` 会真的执行并给出实际耗时与行数，两者差很多说明统计信息过期。
- **联合索引的最左匹配**：`CREATE INDEX ON posts (author_id, created_at)` 能服务 `WHERE author_id=?`、`WHERE author_id=? ORDER BY created_at`，但不能服务只按 `created_at` 过滤的查询——索引列从左到右用，跳过左边列就用不上。
- **索引不是免费的**：每个索引都要在 INSERT/UPDATE/DELETE 时同步维护，读写的是"以写换读"。小表（几百行）全表扫描往往比走索引更快。该不该建，问三句：这个查询常用吗？过滤的选择性够吗（返回行的比例小）？写代价能接受吗？

## AI 搭档

请 AI 根据“按作者过滤、按时间排序”的查询，比较单列索引和复合索引的读写代价。只给假数据规模，不粘贴线上计划、密码或业务数据。

# 第 24 天：从查询需求反推数据模型

原课：<https://xiguadev.com/node-60days/day-24>

## 今日先学

数据库模型从业务事实出发，不从 ORM 装饰器出发。一个作者可写多篇文章，是一对多；文章与标签通常是多对多，需连接表；同名作者、重复标签由唯一约束控制；可空的 `published_at` 表示草稿。`created_at` 是创建时刻，`published_at` 是发布时刻，不要用一个时间字段兼任两种意思。协作任务板属于后续阶段，不能把文章字段改叫任务字段来混用。

## 跟做

当前 `authors`、`posts` 已满足作者与文章的关系。若要让文章拥有多个标签，增加独立标签表和连接表，不要把标签逗号拼进 `posts`。

```sql
CREATE TABLE tags (
  id integer GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  name varchar(40) NOT NULL UNIQUE
);
CREATE TABLE post_tags (
  post_id integer NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
  tag_id integer NOT NULL REFERENCES tags(id) ON DELETE CASCADE,
  PRIMARY KEY (post_id, tag_id)
);
CREATE INDEX post_tags_tag_id_idx ON post_tags(tag_id);
```

联合主键阻止同一文章重复挂同一标签；反向索引让“找某标签下的文章”更容易。`ON DELETE CASCADE` 的影响是删文章会删关联行，不会删共享的标签。标签名是否区分大小写、删作者时是否保留文章，都属于需要明确的业务决定。本教程不执行该 SQL，也不要求改写已有数据库。

## 练习

根据上一天的查询，写一条为每篇文章列出标签名的 SQL；没有标签的文章也要出现。

## 参考答案与验收

```sql
SELECT p.id, p.title, t.name AS tag
FROM posts p
LEFT JOIN post_tags pt ON pt.post_id = p.id
LEFT JOIN tags t ON t.id = pt.tag_id
ORDER BY p.id, t.name;
```

两次 `LEFT JOIN` 保证没有标签的文章仍出现，`tag` 为 `NULL`。通过 `\d post_tags` 验收连接表有双列主键、两个外键，`\d tags` 验收 `name` 唯一。Day25 先把作者文章建模进 Prisma，标签关系留作模型扩展练习。

## 原版对照阅读

原版 Day24 展开更细，讲建模，本讲义只给了一张最终 schema。补三点判断依据：

- **前三范式（1NF/2NF/3NF）**：1NF 要求列不可再分（不要用逗号拼接多个标签）；2NF 要求非主键列依赖整个主键（复合键时常见）；3NF 要求非主键列之间不互相依赖。满足 3NF 的表，同一份事实只存一处，更新不会漏。
- **反范式是明确的交换**：为了少一次 JOIN，允许在 `posts` 冗余一个 `author_name` 或 `like_count`；代价是更新时要同步多处，且可能不一致。只有在读远多于写、且用事务或触发器保证同步时才值得。
- **`JSONB` 该用在哪**：适合结构不稳定、字段稀疏、只整体读写的数据（如文章配置、外部 API 的原始载荷）；不适合需要跨行过滤/排序/约束的核心业务字段——它放弃了类型检查和大部分索引优势。PostgreSQL 的 `JSONB` 是二进制存储、支持 GIN 索引和 `->` 查询，但别把它当成"不用设计 schema"的借口。

时间戳列通常四个就够：`created_at`、`updated_at`、`published_at`、`deleted_at`（软删除）。

## AI 搭档

请 AI 扮演产品经理，问三个问题来确定文章删除、标签大小写、草稿字段的规则。回答只用虚构博客场景，别粘贴密码或业务数据。

# 第 25 天：固定 Prisma 版本并定义模型

原课：<https://xiguadev.com/node-60days/day-25>

## 今日先学

本课程固定 Prisma **6.19.0**，客户端和 CLI 显式安装相同版本，避免使用 Prisma 7 的不同配置方式。此前版本号与 npm registry 元数据核对过：`prisma@6.19.0` 存在且要求 Node `>=18.18`。课程按受支持的 Node LTS（22 / 24 / 26）执行。Prisma Schema 描述模型，迁移文件记录数据库变更，生成客户端提供类型安全查询。今天只配置并生成迁移，不声称迁移已在本机数据库执行。

## 跟做

在 Day16 的 `mini-blog-api` 根目录执行。若 `src/posts` 已存在，直接继续；尚未完成前段时先建立 Nest 11 项目。安装完成后确认 `npm ls prisma @prisma/client` 中两者都显示 `6.19.0`。

```bash
npm install @prisma/client@6.19.0
npm install --save-dev prisma@6.19.0
npx prisma init --datasource-provider postgresql
```

第 21–24 天的库已有手写表和数据，不能当作首次迁移的空库。请在 `psql` 中连接本机已有的管理库（例如 `postgres`），使用有建库权限的练习账号创建独立数据库。下列是 SQL，不是在 Bash 中执行；若 `mini_blog_prisma` 已存在且有表，另取一个未使用的练习库名，不要重置旧库。

```sql
CREATE DATABASE mini_blog_prisma;
```

只在 `mini-blog-api` 根目录私有的 `.env` 中设置 `DATABASE_URL`，数据库名改为刚创建的 `mini_blog_prisma`，格式为 `postgresql://USER:PASSWORD@localhost:5432/mini_blog_prisma?schema=public`。替换成本机账号，密码中的特殊字符需做 URL 编码，不要提交真实值。旧 SQL 库保留不动，里面的作者、文章、标签都不会自动复制。没有建库权限时先取得独立空练习库，再继续迁移。把 `prisma/schema.prisma` 替换为：

```prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model Author {
  id    Int    @id @default(autoincrement())
  name  String @db.VarChar(80)
  posts Post[]

  @@map("authors")
}

model Post {
  id          Int       @id @default(autoincrement())
  title       String    @db.VarChar(120)
  body        String    @db.Text
  authorId    Int       @map("author_id")
  author      Author    @relation(fields: [authorId], references: [id], onDelete: Restrict)
  createdAt   DateTime  @default(now()) @map("created_at") @db.Timestamptz(3)
  publishedAt DateTime? @map("published_at") @db.Timestamptz(3)

  @@index([authorId, createdAt(sort: Desc)], map: "posts_author_created_idx")
  @@map("posts")
}
```

确认 `DATABASE_URL` 的数据库名是新的空练习库，再执行 `npx prisma migrate dev --name init_blog`。预期创建 `authors` 与 `posts`，并生成 `prisma/migrations`。注意第 21 天手写的 `CHECK (length(btrim(title)) > 0)` 约束不在 Prisma schema 的表达能力内，所以这次 `init_blog` 生成的迁移**不含该 CHECK**；要在练习库保留它，得把语句手写进迁移 SQL（见第 25 天「Prisma 映射不了的东西」）。若提示 schema drift 或要求 reset，先停止并核对是否仍连着第 21–24 天的旧库，不要靠重置旧库继续。若提示无法连接，先检查 PostgreSQL 是否正在运行、数据库是否存在、环境变量是否加载；不要把 URL 发给 AI 或粘贴到聊天中。若迁移文件夹已存在，不要覆盖旧迁移；先检查现有状态。

迁移只创建表，不会创建 Ada。新建 `prisma/seed.mjs`，用 `upsert` 保证固定作者 ID `1` 存在，重复执行不会插入第二个 Ada。显式写入 ID 不会推进 PostgreSQL 自增序列，脚本随后把作者序列同步到现有最大 ID，避免将来自动创建作者时撞号。

```js
// prisma/seed.mjs
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();
try {
  await prisma.$transaction(async (tx) => {
    await tx.author.upsert({
      where: { id: 1 },
      update: { name: 'Ada' },
      create: { id: 1, name: 'Ada' },
    });
    await tx.$queryRaw`
      SELECT setval(
        pg_get_serial_sequence('authors', 'id'),
        (SELECT COALESCE(MAX(id), 1) FROM authors),
        true
      )
    `;
  });
  console.log('已准备作者 Ada（ID 1）');
} catch (error) {
  console.error('Seed 失败：', error instanceof Error ? error.name : 'UnknownError');
  process.exitCode = 1;
} finally {
  await prisma.$disconnect();
}
```

在项目根目录保存 seed 命令并执行。这里显式使用 Node 加载 `.env`，不依赖迁移时是否自动触发 seed，也无需额外的 TypeScript 运行器。

```bash
npx prisma generate
npm pkg set 'scripts.seed=node --env-file=.env prisma/seed.mjs'
npm run seed
```

新库完成后应有 Ada、没有文章。每次更换数据库并迁移后都要重新运行 `npm run seed`，第 27 天才可用 `authorId: 1` 创建文章。没有可用数据库时先保存脚本，seed 和后续 CRUD 均标注“未运行”。

## 练习

运行 `npx prisma validate` 和 `npx prisma generate`，再查看 `npm ls prisma @prisma/client`。确认生成的 Prisma 模型名是 `author` 和 `post`（代码中 Prisma Client 属性使用小写）。

## 参考答案与验收

验收命令均应退出码为 `0`，`validate` 输出 schema 有效，`generate` 显示 Prisma Client 已生成，依赖树的 CLI 和客户端都是 `6.19.0`。有数据库时连续运行两次 `npm run seed`，再用 `psql` 连接新的 `mini_blog_prisma` 查询 `SELECT id, name FROM authors ORDER BY id;`，预期仍只有一条 `1 | Ada`。本地数据库未启动时 `migrate dev` 和 seed 连接失败不等同于 schema 错误；仍可完成 `validate` 与 `generate`，但数据库迁移和 seed 验收需等可用的 PostgreSQL 16。不要把连接失败描述成已通过。

## 原版对照阅读

原版 Day25 展开更细，讲 Prisma，本讲义只走了"写 schema → migrate → CRUD"一条路。补两块：

- **三套工作流的决策树**：`prisma migrate dev` 在本地开发、要留下可复现的迁移 SQL 文件（团队共用、生产可执行）；`prisma db push` 直接同步 schema、不生成迁移文件，适合原型或不可迁移的库；`prisma db pull` 从已有数据库反向生成 schema，用于接入遗留库。生产环境用 `prisma migrate deploy`，只执行已有迁移、绝不生成新的。
- **Prisma 映射不了的东西**：CHECK 约束、视图、触发器、部分索引、存储过程等 PG 特性无法在 `schema.prisma` 表达。它们依然存在于数据库里，但 `migrate dev` 生成迁移时可能感知不到——这类对象要手写进迁移 SQL，并接受"`prisma validate` 通过不代表数据库完全一致"。
- **`$queryRaw` 是逃生口**：需要窗口函数、复杂 CTE 或 Prisma 不支持的查询时用 `$queryRaw`；它要求用模板字符串传参（把变量作为标记模板的参数传入）以避免 SQL 注入，绝不能字符串拼接用户输入。

## AI 搭档

请 AI 把 `Author 1:N Post` 和两个 `@@map` 映射解释成数据库表关系，再指出一次迁移前的检查清单。给虚构模型，不粘贴密码、连接串或业务数据。


# 第 26 天：查询作者关系并管理 Prisma 迁移

原课：<https://xiguadev.com/node-60days/day-26>

## 今日先学

Prisma 的 relation 字段让应用能从文章取得作者，不代表数据库里重复存了作者。`include` 返回关联对象，`select` 限定要取的字段，公开 API 时应避免无意返回私密列。迁移是版本化数据库变更；`migrate dev` 用于本地开发，`migrate deploy` 用于部署环境应用已提交的迁移。本课没有在真实数据库上运行命令，不代表迁移已通过。

## 跟做

在 `mini-blog-api` 根目录，确认 Day25 已定义 `Author`、`Post` 并生成客户端。先用 Prisma Studio 查看迁移状态，命令仅在本机连接可用时运行：

```bash
npx prisma migrate status
npx prisma studio
```

关闭 Studio 后，在项目根目录的 `scripts` 目录创建 `check-relations.mjs`。若保存过旧版不完整的 `scripts/check-relations.ts`，先删除它，避免未声明的变量影响 Nest 编译。独立脚本用 `.mjs` 直接交给 Node，初始化 PrismaClient，在 `finally` 中断开连接，不需要修改 Nest 构建配置。

```js
// scripts/check-relations.mjs
import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();
try {
  const posts = await prisma.post.findMany({
    include: { author: { select: { id: true, name: true } } },
    orderBy: { createdAt: 'desc' },
  });
  console.log(posts);
} catch (error) {
  console.error('关系查询失败：', error instanceof Error ? error.name : 'UnknownError');
  process.exitCode = 1;
} finally {
  await prisma.$disconnect();
}
```

先确认 Day25 已在新库完成迁移和 seed，再从 `mini-blog-api` 根目录执行，`--env-file` 显式加载本机连接配置：

```bash
node --env-file=.env scripts/check-relations.mjs
```

刚完成 seed 时只有作者、没有文章，输出 `[]` 是正常结果。Day27 通过 API 创建文章后再运行，才能看到文章中的 `author` 对象；空数组不能证明关系查询的字段已验收。

执行迁移之前检查 `DATABASE_URL` 指向个人练习库，确认备份策略和 `git status` 中迁移文件是预期内容。博客模型已在第 25 天 `init_blog` 建好，今天没有 schema 变更，直接 `npx prisma migrate status` 确认 up to date 即可；此时执行 `migrate dev --name ...` 只会报 `Already in sync`，不会生成新迁移文件。第 40 天要检查的是此前已经产生的迁移文件，不是今天新建的。部署环境只应用已审阅的迁移：`npx prisma migrate deploy`。不要在部署时执行 `migrate dev`，也不要用 `db push` 替代需要留痕的迁移历史。

## 练习

把查询改为只返回文章 `id`、`title` 和作者 `name`，并按文章时间从新到旧排列。

## 参考答案与验收

在 `scripts/check-relations.mjs` 中仅替换 `findMany` 查询，保留初始化、`console.log`、异常处理和 `finally`，再用同一条 Node 命令执行：

```js
const posts = await prisma.post.findMany({
  select: {
    id: true,
    title: true,
    author: { select: { name: true } },
  },
  orderBy: { createdAt: 'desc' },
});
```

验收看每个结果仅有 `id`、`title`、`author` 三个顶层属性，关联作者只有 `name`。`select` 与同层的 `include` 不可同时使用；若报错，选择一种写法。无数据库时可静态检查代码和通过 `npx prisma validate`，不要宣称查到了数据。

## 原版对照阅读

原版 Day26 展开更细，讲事务与 Prisma 陷阱，本讲义只演示了事务和 `include`。补三点：

- **SQL 标准的四种隔离级别与 PG 的实际行为**：标准列出 `READ UNCOMMITTED`、`READ COMMITTED`（PG 默认，每条语句读到已提交的最新值）、`REPEATABLE READ`、`SERIALIZABLE`。**PostgreSQL 不实现真正的 `READ UNCOMMITTED`**：请求它会被静默提升为 `READ COMMITTED`，所以永远读不到未提交的脏数据；PG 的 `REPEATABLE READ` 是快照隔离（事务内始终看到同一快照），`SERIALIZABLE` 基于 SSI，冲突时抛 `40001` 并由应用重试。级别越高越能防止并发异常，代价是更多冲突检测与重试，而不只是「更多锁等待」。Prisma 用 `$transaction(fn, { isolationLevel: Prisma.TransactionIsolationLevel.Serializable })` 指定；遇到序列化失败按有限次退避重试，是应用层责任。
- **N+1 的真相**：先用 1 条查询取 20 篇文章，再为每篇查一次作者，就是 1+20 次往返。Prisma 的 `include` 会用一条 JOIN 或一次 `IN (...)` 批量取回关联，把它压成常数次查询。开启 `DEBUG=*` 观察 SQL 条数，是识别 N+1 最直接的办法。
- **连接池**：每个 Prisma Client 实例维护一个连接池，默认大小约为 `num_cpus*2+1`。无服务器或高并发下连接数不够会排队，过多又会压垮 PostgreSQL（连接是昂贵进程）。生产常用 PgBouncer 池化，此时把 Prisma 的连接串指向池化端口。

## AI 搭档

给 AI 看脱敏后的模型字段，让它设计一条列表查询，检查是否只返回需要的作者字段。不要分享 `.env`、密码或真实文章数据。

# 第 27 天：在 Nest 中注入 Prisma 数据服务

原课：<https://xiguadev.com/node-60days/day-27>

## 今日先学

Nest 的 Service 依赖抽象数据访问方式，PrismaService 封装数据库客户端。`OnModuleInit` 在 Nest 启动时连接，`OnModuleDestroy` 在关闭时断开。此日起文章不再写入内存数组，数据库连接故障会使 API 无法正常提供文章读写。Day20 的内存版只适合单进程演练；重启丢数据，不能称为持久化后端。

## 跟做

Day25 安装的 `@prisma/client` 与 CLI 固定为 `6.19.0`。在 `src/prisma` 新增 Service 和模块，再将它注册到根模块。不要把数据库密码写入源码。

```ts
// src/prisma/prisma.service.ts
import { Injectable, OnModuleDestroy, OnModuleInit } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';

@Injectable()
export class PrismaService extends PrismaClient
  implements OnModuleInit, OnModuleDestroy {
  async onModuleInit() { await this.$connect(); }
  async onModuleDestroy() { await this.$disconnect(); }
}
```

```ts
// src/prisma/prisma.module.ts
import { Global, Module } from '@nestjs/common';
import { PrismaService } from './prisma.service';

@Global()
@Module({ providers: [PrismaService], exports: [PrismaService] })
export class PrismaModule {}
```

在 `AppModule` 中普通导入 `PrismaModule`，加入现有的 `imports: [PostsModule, PrismaModule]`，保留 Day17 的中间件配置。确认 Day25 的 `DATABASE_URL` 指向新练习库，已完成迁移并运行 seed，库中有 Ada（ID `1`）。连接配置仅保存在项目根目录私有的 `.env`。

将 `src/posts/posts.service.ts` 整份替换为下面版本，移除旧数组和 `nextId`。五个 CRUD 方法都改成数据库操作并返回 Promise；控制器原来直接返回 Service 结果的写法可保留，Nest 会等待 Promise，再交给 Day19 的拦截器包装。`Post` 沿用 Day16 的接口，DTO 沿用 Day18 和 Day20，不改字段或校验规则。注意：这里的 `create()` 在第 33 天会被按登录身份确定作者的版本**整体替换**，到时请删除旧方法，不要两个都留着。

```ts
// src/posts/posts.service.ts（替换）
import { BadRequestException, Injectable, NotFoundException } from '@nestjs/common';
import { Prisma } from '@prisma/client';
import { PrismaService } from '../prisma/prisma.service';
import type { CreatePostDto } from './dto/create-post.dto';
import type { UpdatePostDto } from './dto/update-post.dto';
import type { Post } from './post';

@Injectable()
export class PostsService {
  constructor(private readonly prisma: PrismaService) {}

  private assertId(id: number) {
    if (!Number.isInteger(id) || id < 1 || id > 2_147_483_647) {
      throw new BadRequestException('文章 ID 超出范围');
    }
  }

  async list(): Promise<Post[]> {
    return this.prisma.post.findMany({ orderBy: { id: 'asc' } });
  }

  async get(id: number): Promise<Post> {
    this.assertId(id);
    const post = await this.prisma.post.findUnique({ where: { id } });
    if (!post) throw new NotFoundException('文章不存在');
    return post;
  }

  async create(dto: CreatePostDto): Promise<Post> {
    try {
      return await this.prisma.post.create({
        data: { title: dto.title, body: dto.body, authorId: dto.authorId },
      });
    } catch (error) {
      if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === 'P2003') {
        throw new NotFoundException('作者不存在');
      }
      throw error;
    }
  }

  async update(id: number, dto: UpdatePostDto): Promise<Post> {
    if (dto.title === undefined && dto.body === undefined) {
      throw new BadRequestException('请至少提供 title 或 body');
    }
    this.assertId(id);
    const data: { title?: string; body?: string } = {};
    if (dto.title !== undefined) data.title = dto.title;
    if (dto.body !== undefined) data.body = dto.body;
    try {
      return await this.prisma.post.update({ where: { id }, data });
    } catch (error) {
      if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === 'P2025') {
        throw new NotFoundException('文章不存在');
      }
      throw error;
    }
  }

  async delete(id: number): Promise<{ id: number }> {
    this.assertId(id);
    try {
      return await this.prisma.post.delete({ where: { id }, select: { id: true } });
    } catch (error) {
      if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === 'P2025') {
        throw new NotFoundException('文章不存在');
      }
      throw error;
    }
  }
}
```

创建只写入 DTO 允许的三个字段，ID 与创建时间由数据库产生，`publishedAt` 默认是 `null`。作者不再靠 `authorId === 1` 硬编码判断，而由外键保证存在；当前模型的 `P2003` 转成“作者不存在”404。更新只写请求中实际出现的标题和正文，不会覆盖未提交字段，也不会修改作者或发布时间。更新、删除找不到记录的 `P2025` 转成文章 404，其他数据库错误继续交给 Day19 的过滤器返回通用 500。

执行 `npx prisma generate` 后运行 `npm run build`，编译通过再 `npm run start:dev`。这使用脚手架现有构建命令，无需更改构建配置。

## 练习

启动服务后先请求列表，再用旧 DTO 创建文章，复制响应中的 `data.id`，替换后续命令的 `ID`。不要假设数据库自增 ID 总是 `1`。

```bash
curl -i http://127.0.0.1:3000/posts
curl -i http://127.0.0.1:3000/posts -H 'Content-Type: application/json' \
  -d '{"title":"  Draft  ","body":"Original body","authorId":1}'
curl -i http://127.0.0.1:3000/posts/ID
curl -i -X PATCH http://127.0.0.1:3000/posts/ID -H 'Content-Type: application/json' \
  -d '{"title":"Revised"}'
```

更新成功后停止并重新启动 API，再查同一 ID，确认文章仍在。随后删除并查询详情，回归 Day20 的删除约定：

```bash
curl -i http://127.0.0.1:3000/posts/ID
curl -i -X DELETE http://127.0.0.1:3000/posts/ID
curl -i http://127.0.0.1:3000/posts/ID
```

再建一篇用于错误输入验收：空更新 `{}`、`{"title":null}`、创建时的 `"authorId":"1"` 应被拒绝；使用新库不存在的作者 `2` 创建也应失败。最后暂时用无效数据库名重新启动，观察服务及日志，随后恢复正确配置。

## 参考答案与验收

数据库可用且迁移、seed 完成时，空库列表应返回 `200 {"data":[]}`。创建为 `201`，`data.title` 是 `Draft`、`publishedAt` 是 `null`；详情与只改标题均为 `200`，正文仍是 `Original body`。重启后同一 ID 应仍能读到 `Revised`。删除为 `200 {"data":{"id":实际ID}}`，再查为文章不存在的 `404`。空更新、`null` 标题和数字字符串作者 ID 均为 `400`；作者 `2` 在未新增其他作者的新库中返回 `404 作者不存在`。有文章时还可重跑 Day26 的关系查询确认 Ada 关联。

连接失败时 Nest 启动报错或请求返回通用 `500`，不能再假装返回空数组。恢复连接后重启，未删除的行应仍在。没有可用数据库时只检查代码与编译，将以上 HTTP、重启和关系查询验收标注“未运行”。请勿为此练习把数据库凭据贴入报告。

## AI 搭档

请 AI 根据上述注入关系画出模块依赖图，并指出如何在测试中替换 PrismaService。只给伪造服务签名，不分享连接串或业务数据。

# 第 28 天：实现分页、检索与排序

原课：<https://xiguadev.com/node-60days/day-28>

## 今日先学

数据库列表必须限制返回数量。接口约定 `page` 从 1 开始，默认每页 10 条，最多 50 条；`q` 在标题或正文里做大小写不敏感的包含搜索；`sort` 仅允许 `createdAt` 或 `title`，`order` 仅允许 `asc`、`desc`。参数是字符串，要校验再传 Prisma，绝不把任意客户端字符串拼成 SQL。总数与当前页结果组成 `{items,total,page,pageSize}`，第 19 天的拦截器会再加 `data` 外层。

## 跟做

为简明起见，在 Controller 里先读 `@Query()` 字符串并调用 Service 校验。Prisma `skip/take` 参数由校验后的数字计算。Day16 的成功包装器不改变对象内部结构。

```ts
// posts.service.ts 中增加 listPage 方法
async listPage(query: Record<string, string | undefined>) {
  const page = Number(query.page ?? '1');
  const pageSize = Number(query.pageSize ?? '10');
  const sort = query.sort ?? 'createdAt';
  const order = query.order ?? 'desc';
  const q = query.q?.trim();
  if (!Number.isInteger(page) || page < 1 || page > 1_000_000) {
    throw new BadRequestException('page 必须是 1 到 1000000 的整数');
  }
  if (!Number.isInteger(pageSize) || pageSize < 1 || pageSize > 50) {
    throw new BadRequestException('pageSize 必须是 1 到 50 的整数');
  }
  if (!['createdAt', 'title'].includes(sort)) {
    throw new BadRequestException('sort 不受支持');
  }
  if (order !== 'asc' && order !== 'desc') {
    throw new BadRequestException('order 只能是 asc 或 desc');
  }
  const where = q ? { OR: [
    { title: { contains: q, mode: 'insensitive' as const } },
    { body: { contains: q, mode: 'insensitive' as const } },
  ] } : {};
  // sort / order 已过白名单校验。不要写 orderBy: { [sort]: order }：
  // 计算键会让对象退化成 { [x: string]: string }，无法赋给 Prisma 的排序类型。
  const direction: 'asc' | 'desc' = order === 'asc' ? 'asc' : 'desc';
  const orderBy: Prisma.PostOrderByWithRelationInput[] = sort === 'title'
    ? [{ title: direction }, { id: 'asc' }]
    : [{ createdAt: direction }, { id: 'asc' }];
  const [total, items] = await this.prisma.$transaction([
    this.prisma.post.count({ where }),
    this.prisma.post.findMany({
      where, skip: (page - 1) * pageSize, take: pageSize,
      orderBy,
      select: { id: true, title: true, createdAt: true, authorId: true },
    }),
  ]);
  return { items, total, page, pageSize };
}
```

从 `@nestjs/common` 导入 `BadRequestException`，从 `@prisma/client` 导入 `Prisma` 类型。在 controller 把原来的 `list()` 路由改成接收 `@Query() query: Record<string, string | undefined>` 并调用 `this.posts.listPage(query)`。直接按 `title` 排序时相同标题间顺序未定义，真实系统可增加 `id` 作为次排序键。

## 练习

请求 `/posts?page=1&pageSize=5&q=nest&sort=title&order=asc`，再请求非法 `/posts?page=0` 和 `/posts?sort=authorId`。

## 参考答案与验收

合法参数应返回 `200`，字段包含 `items`、`total`、`page:1`、`pageSize:5`；命中项目依标题升序。非法参数各返回 `400`，消息分别说明 page 范围和 sort 不受支持。无匹配时 `items:[]`、`total:0`，不应返回 404。跟做里的 `orderBy` 用白名单分支构造，编译期就不依赖动态键；若自己改成 `{ [sort]: order }`，`npm run build` 会报 TS 类型错误，不要用 `as any` 之类的断言绕过检查。

## AI 搭档

给 AI 看允许的分页和排序规则，让它找出至少三种越界输入，并设计接口验收表。只给假查询参数，不粘贴密码或真实业务数据。

# 第 29 天：用事务保证多步写入并识别并发

原课：<https://xiguadev.com/node-60days/day-29>

## 今日先学

单条 SQL 通常由数据库原子执行；多个写入作为一个业务动作时，需要事务防止只完成一半。发布文章要先确认文章存在，再设置 `publishedAt`；写入失败整体回滚。并发请求也可能同时通过“先查再改”的检查，所以唯一性、外键和条件更新应尽量交给数据库约束。事务不是自动解决所有竞争；更严格的业务还要考虑锁、隔离级别和重试。以下仅为示范代码，不表示已连数据库运行。

## 跟做

给 Service 增加发布方法。按 Day24 的定义，发布状态由 `publishedAt` 是否为空表示。事务内若文章不存在，抛出 Nest 的 `NotFoundException`；ORM 将失败传播出去。该更新本身是单条数据库操作，事务展示可扩展到将来增加审计行等多步动作。

```ts
async publish(id: number) {
  this.assertId(id);
  return this.prisma.$transaction(async (tx) => {
    const post = await tx.post.findUnique({ where: { id } });
    if (!post) throw new NotFoundException('文章不存在');
    if (post.publishedAt) return post;
    return tx.post.update({
      where: { id }, data: { publishedAt: new Date() },
    });
  });
}
```

为路由增加 `@Patch(':id/publish')`，沿用 `ParseIntPipe` 解析 ID，调用 Service 的 `publish`。使用两个终端几乎同时调用它，观察两次响应：两次都会成功且 `publishedAt` 非空，但在 READ COMMITTED 下可能是两个不同的时间（后写覆盖先写），不应把后一次改回草稿。要做到只发布一次，得用条件更新，见下面的答案。对“余额扣减”一类数值业务，不要照搬先查再改；应写成带条件的原子更新并检查受影响行数。

## 练习

把文章 ID 改成不存在的正整数调用发布路由；再对有效文章调用两次。检查错误映射及发布时间是否有值。

## 参考答案与验收

不存在记录应由应用转换成 `404`，对外为 Day19 统一格式。有效记录两次调用都返回成功、`publishedAt` 非空，但值可能是两个不同的时间——这正是 READ COMMITTED 下的后写覆盖：两个事务都读到草稿、再各自写入不同的 `publishedAt`。「先读后判」只能避免把已发布改回草稿，做不到 exactly-once；要保证只发布一次，需要用条件更新 `UPDATE ... WHERE publishedAt IS NULL` 并检查受影响行数，在 Prisma 中是带 `where` 条件的 `updateMany` 后看 `count`，只有 `count === 1` 的那次算发布成功。本演示不要声称提供完整的审计或 exactly-once 保证。数据库不可用时记录为未能运行验证。

## AI 搭档

请 AI 给“发布并写审计记录”设计事务失败场景和回滚检查步骤。只用伪造 ID 与数据，别粘贴密码或业务信息。

# 第 30 天：完成可持久化博客 API

原课：<https://xiguadev.com/node-60days/day-30>

## 今日先学

博客后端里程碑由 HTTP、DTO、统一错误、PostgreSQL、Prisma 迁移和 Nest 依赖注入组成。Day20 是无数据库、进程内数组的可运行学习版本：覆盖创建、列表、详情、部分更新、删除，但重启会丢数据，不能作为持久化后端。今天的目标是把相同接口切换到 PostgreSQL。第 46 天起才迁移到「协作任务板」，届时另增 Task、Board、Member 等业务模型，不要把 `Post` 偷换成 Task。

## 跟做

在项目根目录先核对版本和环境，不安装或启动系统级软件：

```bash
node -v
npm -v
npm ls @nestjs/core prisma @prisma/client
npx prisma validate
npx prisma migrate status
```

本课程约定 Node 22 / 24 / 26（受支持 LTS）、Nest 11.x、Prisma CLI/Client 6.19.0、PostgreSQL 16.x、npm。迁移状态命令需要数据库连接；没有可用 PostgreSQL 时只能完成静态配置检查。确认使用 Day25 独立的新库并完成 `npm run seed`，已替换 Day27 完整数据库版 `PostsService`，在同一类中加入 Day28 的 `listPage` 和 Day29 的 `publish`；不要只替换列表就保留其他内存方法。DTO 和成功、错误包装继续沿用 Day18–20 的约定。建议接口如下：

- `GET /posts?page=1&pageSize=10&q=&sort=createdAt&order=desc`：分页检索。
- `GET /posts/:id`：详情，不存在为 404。
- `POST /posts`：创建，`title`、`body`、`authorId`；成功 201。
- `PATCH /posts/:id`：部分更新，空对象 400；需认证，仅作者本人或管理员。
- `PATCH /posts/:id/publish`：设置发布时间；需认证，仅作者本人或管理员。
- `DELETE /posts/:id`：删除，成功返回被删 ID。

用 `curl` 创建并保存返回 ID，接着按序执行列表、详情、改标题、发布、删除、再查详情。成功外层为 `{ "data": ... }`，错误外层为 `{ "error": { "statusCode": ..., "message": ... } }`。分页对象下含 `items`、`total`、`page` 和 `pageSize`。

## 练习

写一份自己的冒烟验收清单，包含错误输入、分页和服务重启；不需要连生产环境，也不需要装数据库软件。

## 参考答案与验收

最低验收：`prisma validate` 通过；依赖版本匹配；在有 PostgreSQL 16 练习库时迁移状态为 up to date；新建文章的字段经 DTO 校验；错误 ID 返回 404；非法分页返回 400；重启 API 后文章还存在。若数据库不可用，只能确认静态配置与编译检查，标注数据库项“未运行”，不能报告全部通过。Day20 的无库内存版本单独可运行，不依赖这些数据库条件。

## AI 搭档

请 AI 扮演 API 测试者，按清单找一条最可能遗漏的回归路径，并说明预期状态码。只给虚构响应与字段，绝不粘贴数据库密码、个人凭据或真实业务数据。


# 第 31 天：用 Session 和 JWT 表达登录状态

原课：<https://xiguadev.com/node-60days/day-31>

## 今日先学

继续使用第 30 天的 NestJS 11、PostgreSQL 16、Prisma 6.19.x 博客。今天先在博客根目录做一个独立实验，熟悉两个经常被混淆的概念。Session 由服务器保存状态，浏览器带着一个随机会话 ID 去查。签名 JWT 自带声明，API 验签后才信任其中的身份。JWT 的签名保护完整性，正文可以被读取。Cookie 是传递凭据的方式，Session ID 和 JWT 都可以放进 Cookie，浏览器自动发送 Cookie 时就要评估 CSRF。

| 需求 | Session | 短时 JWT |
| --- | --- | --- |
| 立即注销 | 删除服务端记录并清 Cookie | 已签发令牌可用至过期，需撤销表或会话版本才能提前拒绝 |
| 多实例 | 共享会话存储 | 共享验签配置，仍可能查库确认账号和权限 |
| 常见用法 | 同源网页，由后端管理登录 | API 客户端，通过 `Authorization: Bearer` 传递 |

## 跟做

在博客根目录安装 `npm i express-session`。创建 `labs/session.mjs`。它只统计访问次数，无账号功能，使用单进程内存存储，并且只监听本机。

```js
import express from 'express';
import session from 'express-session';
import { randomBytes } from 'node:crypto';

const app = express();
app.use(session({
  name: 'blog.lab.sid', secret: randomBytes(32).toString('base64url'),
  resave: false, saveUninitialized: false,
  cookie: { httpOnly: true, sameSite: 'lax', maxAge: 300_000 },
}));
app.get('/visits', (req, res) => {
  req.session.visits = (req.session.visits ?? 0) + 1;
  res.json({ visits: req.session.visits });
});
app.post('/logout', (req, res, next) => {
  req.session.destroy(error => {
    if (error) return next(error);
    res.clearCookie('blog.lab.sid', { path: '/' });
    res.sendStatus(204);
  });
});
app.listen(3101, '127.0.0.1');
```

运行 `node labs/session.mjs`。在第二个终端用 `curl -c lab.cookies -b lab.cookies http://127.0.0.1:3101/visits` 连续请求两次，应看到 `1`、`2`。Windows PowerShell 使用 `curl.exe`。`-b` 读取会话凭据，`-c` 把响应更新写回文件。实验后删除该文件，勿分享。正式网页应启用 HTTPS、`Secure`、CSRF 防护和共享存储，登录成功时重新生成会话 ID。

## 练习

用同一 Cookie 文件退出，再访问计数。设想博客新增一个需即时注销的同源运营后台，说明你会选哪种登录状态。

## 参考答案与验收

`curl -i -b lab.cookies -c lab.cookies -X POST http://127.0.0.1:3101/logout` 返回 204。再跑 `/visits` 命令应看到 `1`。同源运营后台可选 Session，退出时删除共享存储中的该会话。下一课博客 API 使用短时 Bearer JWT。

## AI 搭档

提示词「用一个虚构后台画出 Session 登录后访问、退出的三步流程，并标注谁保存什么。」人工验收时确认 Cookie 里只有会话凭据，退出会删除服务端记录。只发计数和状态码，去掉 Cookie 与请求头凭据。

# 第 32 天：给博客 API 签发并校验 JWT

原课：<https://xiguadev.com/node-60days/day-32>

## 今日先学

认证回答“你是谁”。前课只有作者 `Author`，还没有账号或登录入口；今天新增 `User`，通过唯一的 `authorId` 与作者一一关联，`Post.authorId` 继续引用 `Author.id`。密码使用 Argon2id 哈希，绝不回传哈希。登录签发十分钟 access token 和七天 refresh token：前者是 JWT，用于 Bearer 请求；后者是随机凭据，数据库只存它的 SHA-256 哈希，用于轮换和退出。JWT 的 `sub` 始终是 `User.id`，不是作者编号。

## 跟做

在博客根目录执行 `npm i @nestjs/jwt@11 @nestjs/config@4 argon2`。先在 `prisma/schema.prisma` 的现有 `Author` 中增加 `user User?`，再追加下面两个模型。已有作者保持不变，新注册账号会原子创建自己的作者；已有作者绑定需单独核验，不能仅凭姓名认领。

```prisma
model User {
  id              Int              @id @default(autoincrement())
  email           String           @unique
  passwordHash    String
  authorId        Int              @unique
  author          Author           @relation(fields: [authorId], references: [id], onDelete: Restrict)
  refreshSessions RefreshSession[]
}

model RefreshSession {
  tokenHash String   @id
  userId    Int
  expiresAt DateTime
  user      User     @relation(fields: [userId], references: [id], onDelete: Cascade)

  @@index([userId])
  @@index([expiresAt])
}
```

执行 `npx prisma migrate dev --name users_refresh_sessions`、`npx prisma generate`。用命令为本地 `.env` 追加随机密钥，执行一次即可。先确认 `.env` 已忽略。使用密钥管理服务注入线上密钥，并记录轮换与紧急撤销步骤。

```bash
node -e "process.stdout.write('\nJWT_SECRET='+require('node:crypto').randomBytes(32).toString('base64url')+'\n')" >> .env
```

在 `src/app.module.ts` 的 `imports` 中载入 `ConfigModule.forRoot({ isGlobal: true })`、第 27 天的 `PrismaModule` 和下面的 `AuthModule`，导入对应类。在 `src/main.ts` 的 `listen()` 前确认已有 `app.useGlobalPipes(new ValidationPipe({ whitelist: true, forbidNonWhitelisted: true, transform: true }))`，从 `@nestjs/common` 导入 `ValidationPipe`；若缺依赖先执行 `npm i class-validator class-transformer`。新建下面模块、服务、控制器和 Guard；若曾做过认证练习，合并到同一套入口，不重复声明路由。

```ts
import { Module } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { JwtModule } from '@nestjs/jwt';
import { JwtAuthGuard } from './jwt-auth.guard';
import { AuthService } from './auth.service';
import { AuthController } from './auth.controller';
import { PrismaModule } from '../prisma/prisma.module';

@Module({
  imports: [PrismaModule, JwtModule.registerAsync({
    inject: [ConfigService],
    useFactory: (config: ConfigService) => {
      const secret = config.getOrThrow<string>('JWT_SECRET');
      if (Buffer.from(secret, 'base64url').length < 32) {
        throw new Error('JWT_SECRET 必须由至少 32 字节随机数据生成');
      }
      const issuer = 'blog-api';
      const audience = 'blog-client';
      return { secret,
        signOptions: { algorithm: 'HS256', expiresIn: 600, issuer, audience },
        verifyOptions: { algorithms: ['HS256'], issuer, audience } };
    },
  })],
  controllers: [AuthController],
  providers: [AuthService, JwtAuthGuard],
  exports: [JwtModule, JwtAuthGuard],
})
export class AuthModule {}
```

新建服务。刷新令牌每次使用后原子删除旧记录并写入新记录，同一个旧令牌并发刷新时只有一次成功。这里的退出撤销指定 refresh token，已有 access token 最多仍可用十分钟；立即撤销所有访问令牌需另加会话版本校验。定期清理已过期的 `RefreshSession`，并在生产为注册、登录、刷新加限流。

```ts
// src/auth/auth.service.ts
import { ConflictException, Injectable, UnauthorizedException } from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';
import { Prisma } from '@prisma/client';
import { createHash, randomBytes } from 'node:crypto';
import * as argon2 from 'argon2';
import { PrismaService } from '../prisma/prisma.service';

const hashToken = (token: string) => createHash('sha256').update(token).digest('hex');
const refreshLifetime = 7 * 24 * 60 * 60 * 1000;

@Injectable()
export class AuthService {
  constructor(private readonly db: PrismaService, private readonly jwt: JwtService) {}

  async register(email: string, password: string, name: string) {
    const passwordHash = await argon2.hash(password, { type: argon2.argon2id });
    try {
      return await this.db.user.create({
        data: { email, passwordHash, author: { create: { name } } },
        select: { id: true, email: true, authorId: true },
      });
    } catch (error) {
      if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === 'P2002') {
        throw new ConflictException('邮箱已注册');
      }
      throw error;
    }
  }

  async login(email: string, password: string) {
    const user = await this.db.user.findUnique({
      where: { email }, select: { id: true, passwordHash: true },
    });
    if (!user || !await argon2.verify(user.passwordHash, password)) {
      throw new UnauthorizedException('邮箱或密码错误');
    }
    return this.db.$transaction(tx => this.issue(tx, user.id));
  }

  private async issue(tx: Prisma.TransactionClient, userId: number) {
    const refreshToken = randomBytes(32).toString('base64url');
    const accessToken = await this.jwt.signAsync({ sub: String(userId) });
    await tx.refreshSession.create({ data: {
      tokenHash: hashToken(refreshToken), userId,
      expiresAt: new Date(Date.now() + refreshLifetime),
    } });
    return { accessToken, refreshToken, expiresIn: 600 };
  }

  async refresh(refreshToken: string) {
    const tokenHash = hashToken(refreshToken);
    return this.db.$transaction(async tx => {
      const session = await tx.refreshSession.findUnique({ where: { tokenHash } });
      if (!session) throw new UnauthorizedException('请重新登录');
      const consumed = await tx.refreshSession.deleteMany({
        where: { tokenHash, expiresAt: { gt: new Date() } },
      });
      if (consumed.count !== 1) throw new UnauthorizedException('请重新登录');
      return this.issue(tx, session.userId);
    });
  }

  async logout(refreshToken: string) {
    await this.db.refreshSession.deleteMany({ where: { tokenHash: hashToken(refreshToken) } });
  }
}
```

控制器和输入 DTO 放在同一文件。下面用 JSON 传 refresh token，适合本地 API 客户端实验；客户端只暂存在内存，刷新时替换两个令牌，401 时重新登录。网页若改为自动携带的 HttpOnly Cookie，必须同时设计 CSRF 防护、HTTPS 和 Cookie 属性。服务端日志禁止记录这些请求体。

```ts
// src/auth/auth.controller.ts
import { Body, Controller, Header, HttpCode, Post } from '@nestjs/common';
import { Transform } from 'class-transformer';
import { IsEmail, IsString, Length, Matches, MaxLength } from 'class-validator';
import { AuthService } from './auth.service';

class CredentialsDto {
  @Transform(({ value }) => typeof value === 'string' ? value.trim().toLowerCase() : value)
  @IsEmail() @MaxLength(254)
  email!: string;

  @IsString() @Length(12, 128)
  password!: string;
}

class RegisterDto extends CredentialsDto {
  @Transform(({ value }) => typeof value === 'string' ? value.trim() : value)
  @IsString() @Length(1, 80) @Matches(/\S/)
  name!: string;
}

class RefreshDto {
  @IsString() @Matches(/^[A-Za-z0-9_-]{43}$/)
  refreshToken!: string;
}

@Controller('auth')
export class AuthController {
  constructor(private readonly auth: AuthService) {}

  @Post('register') @Header('Cache-Control', 'no-store')
  register(@Body() dto: RegisterDto) {
    return this.auth.register(dto.email, dto.password, dto.name);
  }

  @Post('login') @HttpCode(200) @Header('Cache-Control', 'no-store')
  login(@Body() dto: CredentialsDto) { return this.auth.login(dto.email, dto.password); }

  @Post('refresh') @HttpCode(200) @Header('Cache-Control', 'no-store')
  refresh(@Body() dto: RefreshDto) { return this.auth.refresh(dto.refreshToken); }

  @Post('logout') @HttpCode(204) @Header('Cache-Control', 'no-store')
  async logout(@Body() dto: RefreshDto) { await this.auth.logout(dto.refreshToken); }
}
```

```ts
// src/auth/jwt-auth.guard.ts
import { CanActivate, ExecutionContext, Injectable, UnauthorizedException } from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';
import type { Request } from 'express';

export type AuthRequest = Request & { user?: { sub: string } };

@Injectable()
export class JwtAuthGuard implements CanActivate {
  constructor(private readonly jwt: JwtService) {}
  async canActivate(context: ExecutionContext) {
    const req = context.switchToHttp().getRequest<AuthRequest>();
    const token = /^Bearer ([^\s]+)$/i.exec(req.headers.authorization ?? '')?.[1];
    if (!token) throw new UnauthorizedException();
    try {
      const claims = await this.jwt.verifyAsync<{ sub?: unknown; exp?: unknown }>(token);
      if (typeof claims.sub !== 'string' || !claims.sub || typeof claims.exp !== 'number') {
        throw new UnauthorizedException();
      }
      req.user = { sub: claims.sub };
      return true;
    } catch {
      throw new UnauthorizedException();
    }
  }
}
```

## 练习

在认证控制器新增 `GET /auth/me`，只回显通过验证的用户编号。先做无凭据请求，再用本地 API 客户端登录，临时在客户端保存令牌变量，配置 Bearer 认证后重试。

## 参考答案与验收

在认证控制器类内加入下方方法，前缀为 `@Controller('auth')`。控制器从 Nest 导入 `Get`、`UseGuards`、`Req`、`Header`，并从 Guard 文件导入 `JwtAuthGuard` 和 `type AuthRequest`。

```ts
@Get('me')
@UseGuards(JwtAuthGuard)
@Header('Cache-Control', 'no-store')
me(@Req() req: AuthRequest) {
  return { id: req.user!.sub };
}
```

运行 `npm run build`、`npm run start:dev`。用本地 API 客户端按下面顺序操作，JSON 请求带 `Content-Type: application/json`；令牌变量仅留在该客户端，勿提交或截图。

| 步骤 | 请求与预期 |
| --- | --- |
| 注册 A | `POST /auth/register`，`{"email":"a@example.test","password":"local-demo-12345","name":"作者A"}`，201，保存 `id` 和 `authorId` |
| 登录 A | `POST /auth/login`，只发送同一 `email`、`password`，200，暂存 access token `A1`、refresh token `R1` |
| 查身份 | 无 Bearer 请求 `/auth/me` 为 401，带 `A1` 为 200，返回账号 `id` |
| 轮换 | `POST /auth/refresh`，`{"refreshToken":"<R1>"}`，200，替换为新 `A2`、`R2`；再用 `R1` 刷新为 401 |
| 退出 | `POST /auth/logout`，`{"refreshToken":"<R2>"}`，204；再用 `R2` 刷新为 401，清除客户端两个令牌 |

把本地签发时效临时改成 3 秒，重新登录并等待至少 4 秒，旧 access token 请求 `/auth/me` 应得 401；refresh token 仍可换出新 access token。完成后恢复 600 秒。过期 refresh token（在本地 Studio 把该记录 `expiresAt` 改到过去）刷新也为 401。重复注册为 409，错密码为 401，数据库只保存密码哈希与 refresh token 哈希。退出不会提前撤销已经签发的 access token。

## AI 搭档

提示词「检查这段已脱敏的 Guard 是否检查签名、算法、发行方、受众和过期时间，把检查项对应到代码。」人工核对 `verifyOptions` 与 Guard，跑过期验收。只分享字段名、状态码和代码，省略密钥、令牌、邮箱与密码。

# 第 33 天：用 RBAC 和归属判断约束文章操作

原课：<https://xiguadev.com/node-60days/day-33>

## 今日先学

授权回答“这个人可以做什么”。RBAC 按角色赋权，资源归属则需要再判断文章的作者。今天的规则是普通用户只能删除自己的 `Post`，管理员可以删除任意文章。角色来自数据库，忽略客户端提供的角色。部署后修改角色，下一次请求就会依据最新记录授权。身份缺失或无法对应账号为 401，资源可见但无操作权限为 403，文章不存在为 404。下面针对公开博客，若资源为私有，应考虑统一返回 404。

## 跟做

在 `prisma/schema.prisma` 添加枚举 `Role`，成员为 `USER`、`ADMIN`，在现有 `User` 加入 `role Role @default(USER)`。沿用 `Post.authorId`，若前课命名不同就替换字段名。本段代码按整数 ID 示范。若博客使用字符串 ID，DTO/路由和 Prisma 查询沿用原 ID 类型，JWT 的 `sub` 已是字符串。

```bash
npm i @casl/ability
npx prisma migrate dev --name add_user_roles
npx prisma generate
```

使用成熟授权库集中写规则。在 `src/posts/post-policy.ts` 创建授权函数。

```ts
import { AbilityBuilder, createMongoAbility, subject } from '@casl/ability';
import type { User } from '@prisma/client';

export function canDeletePost(actor: Pick<User, 'authorId' | 'role'>, post: { authorId: number }) {
  const { can, build } = new AbilityBuilder(createMongoAbility);
  if (actor.role === 'ADMIN') can('delete', 'Post');
  if (actor.role === 'USER') can('delete', 'Post', { authorId: actor.authorId });
  return build().can('delete', subject('Post', post));
}
```

将此方法加入 `src/posts/posts.service.ts`，保留既有 `this.prisma` 注入。从 Nest 导入三个异常，从同目录导入 `canDeletePost`。在 `src/posts/posts.module.ts` 导入 `AuthModule`。在原 `DELETE /posts/:id` 上添加 `@UseGuards(JwtAuthGuard)`、`@HttpCode(204)`，保留 `@Param('id', ParseIntPipe) id: number`，增加 `@Req() req: AuthRequest`，控制器执行 `await this.posts.remove(id, req.user!.sub)`。

```ts
async remove(id: number, sub: string) {
  if (!/^[1-9]\d*$/.test(sub) || !Number.isSafeInteger(Number(sub))) {
    throw new UnauthorizedException();
  }
  const actor = await this.prisma.user.findUnique({
    where: { id: Number(sub) }, select: { authorId: true, role: true },
  });
  if (!actor) throw new UnauthorizedException();
  const post = await this.prisma.post.findUnique({
    where: { id }, select: { authorId: true },
  });
  if (!post) throw new NotFoundException();
  if (!canDeletePost(actor, post)) throw new ForbiddenException();
  const result = await this.prisma.post.deleteMany({
    where: actor.role === 'ADMIN' ? { id } : { id, authorId: actor.authorId },
  });
  if (result.count === 0) throw new NotFoundException();
}
```

删除条件也带作者编号，可避免检查和删除之间作者变化时误删。创建也必须查映射：从 `CreatePostDto` 删除 `authorId` 字段及装饰器，只保留 `title`、`body`；在原 `POST /posts` 加 `@UseGuards(JwtAuthGuard)`，接收 `@Req() req: AuthRequest`，改为调用 `this.posts.createForActor(dto, req.user!.sub)`。**把第 27 天 `PostsService` 里的旧 `create()` 整个删除**，再用下面的方法**替换**它（不是追加），并导入 `CreatePostDto`。如果只追加不删除，旧方法仍引用已被删除的 `dto.authorId`，`npm run build` 会报 TS 错误。其他编辑、发布路由同样必须按 `User.authorId → Author.id` 的映射判断归属，不能直接比较 `sub` 与文章的 `authorId`；下面给出两条路由的完整实现。普通注册 DTO 不接收角色，管理员账号由受控运维流程设置。

```ts
async createForActor(dto: CreatePostDto, sub: string) {
  if (!/^[1-9]\d*$/.test(sub) || !Number.isSafeInteger(Number(sub))) {
    throw new UnauthorizedException();
  }
  const actor = await this.prisma.user.findUnique({
    where: { id: Number(sub) }, select: { authorId: true },
  });
  if (!actor) throw new UnauthorizedException();
  return this.prisma.post.create({
    data: { title: dto.title, body: dto.body, authorId: actor.authorId },
  });
}
```

## 编辑与发布也要做归属判断

只给 `createForActor` 和 `removeForActor` 是不够的：若 `PATCH /posts/:id`、`PATCH /posts/:id/publish` 还保持第 27 天的裸实现，未登录也能改标题、发布任意文章，Day33/Day35 的权限模型会被整体绕过。两条路由都要加 `JwtAuthGuard`，从 `req.user!.sub` 查 `User.authorId` 映射，再用 `actor.authorId` 与 `Post.authorId` 比较；管理员由 `canDeletePost` 放行。Service 的更新条件同样要带 `authorId`，避免检查与写入之间作者变化。

```ts
// src/posts/posts.controller.ts：补两条受保护路由（其余路由保持原有实现）
@Patch(':id')
@UseGuards(JwtAuthGuard)
async updateForActor(@Param('id', ParseIntPipe) id: number,
  @Body() dto: UpdatePostDto, @Req() req: AuthRequest) {
  return this.posts.updateForActor(id, dto, req.user!.sub);
}

@Patch(':id/publish')
@UseGuards(JwtAuthGuard)
async publishForActor(@Param('id', ParseIntPipe) id: number,
  @Req() req: AuthRequest) {
  return this.posts.publishForActor(id, req.user!.sub);
}
```

```ts
// src/posts/posts.service.ts：复用 Day33 的 actor 映射与 canDeletePost 规则
private async actorFor(sub: string) {
  if (!/^[1-9]\d*$/.test(sub) || !Number.isSafeInteger(Number(sub))) {
    throw new UnauthorizedException();
  }
  const actor = await this.prisma.user.findUnique({
    where: { id: Number(sub) }, select: { authorId: true, role: true },
  });
  if (!actor) throw new UnauthorizedException();
  return actor;
}

async updateForActor(id: number, dto: UpdatePostDto, sub: string) {
  const actor = await this.actorFor(sub);
  const post = await this.prisma.post.findUnique({ where: { id }, select: { authorId: true } });
  if (!post) throw new NotFoundException();
  if (!canDeletePost(actor, post)) throw new ForbiddenException();
  const result = await this.prisma.post.updateMany({
    where: actor.role === 'ADMIN' ? { id } : { id, authorId: actor.authorId },
    data: { ...dto },
  });
  if (result.count === 0) throw new NotFoundException();
  return this.prisma.post.findUniqueOrThrow({ where: { id } });
}

async publishForActor(id: number, sub: string) {
  const actor = await this.actorFor(sub);
  const post = await this.prisma.post.findUnique({ where: { id }, select: { authorId: true } });
  if (!post) throw new NotFoundException();
  if (!canDeletePost(actor, post)) throw new ForbiddenException();
  const result = await this.prisma.post.updateMany({
    where: actor.role === 'ADMIN' ? { id } : { id, authorId: actor.authorId },
    data: { publishedAt: new Date() },
  });
  if (result.count === 0) throw new NotFoundException();
  return this.prisma.post.findUniqueOrThrow({ where: { id } });
}
```

把 `UpdatePostDto`、`Patch`、`Body`、`Param`、`ParseIntPipe`、`Req`、`UseGuards` 与三个异常补进对应文件的导入；`canDeletePost` 判断的是同一组「管理员放行 / 普通用户必须是作者」规则，也可以把它重命名为 `canManagePost` 后复用。第 30 天接口清单里的两条 `PATCH` 也应标注「需认证」。

## 练习

用两个普通账号 A、B 和一个管理员，在本地测试库准备两篇由 A 发布、可删除的文章。运行 `npx prisma studio`，只在本地测试库把指定测试管理员的 `role` 改为 `ADMIN`。依次执行下表，保留状态码。

## 参考答案与验收

| 操作 | 预期 |
| --- | --- |
| 未登录删除 A 的第一篇 | 401，文章还在 |
| B 删除 A 的第一篇 | 403，文章还在 |
| A 删除自己的第一篇 | 204，再删是 404 |
| 管理员删除 A 的第二篇 | 204 |

运行 `npm run build`，然后 `npm run start:dev` 走 HTTP 验收。把管理员恢复为 `USER` 后，用旧令牌尝试删除 A 新建的第三篇，应为 403。

## AI 搭档

提示词「这四条博客授权用例中，哪条能单独验证归属约束？请补一条旧令牌在降权后的测试。」分享角色与虚构编号。人工验收用同一令牌在数据库降权前后各检查一次。

# 第 34 天：用 OAuth 2.0 与 OIDC 接入外部登录

原课：<https://xiguadev.com/node-60days/day-34>

## 今日先学

OAuth 2.0 允许应用获得外部服务授予的访问权限。OpenID Connect（OIDC）增加身份层，博客用它确认登录用户。今日使用授权码流程，由服务器交换授权码。`state` 绑定这一次浏览器登录流程，PKCE 绑定授权请求和换码，`nonce` 绑定收到的 ID Token。使用维护中的 `openid-client` v6 处理发现、换码及校验。博客根据验证后的 `(iss, sub)` 找 `User`，再签发第 32 天的应用令牌。

## 跟做

使用受支持的 Node LTS（22 / 24 / 26，新项目优先 26）的较新补丁版。在演示身份提供方注册 confidential Web 客户端，仅允许 `http://127.0.0.1:3000/auth/oidc/callback`。选支持本机 HTTP 回调的提供方。将准确的发行方 URL、客户端 ID、秘密分别存入本地 `.env` 的 `OIDC_ISSUER`、`OIDC_CLIENT_ID`、`OIDC_CLIENT_SECRET`，密钥来自配置后台。执行 `npm i openid-client@^6 express-session`、`npm i -D @types/express-session`。

在 `prisma/schema.prisma` 为 `User` 增加 `externalIdentities ExternalIdentity[]`，沿用用户主键类型。下列模型以整数 ID 为例。执行 `npx prisma migrate dev --name external_identity` 和 `npx prisma generate`。

```prisma
model ExternalIdentity {
  issuer  String
  subject String
  userId  Int
  user    User   @relation(fields: [userId], references: [id], onDelete: Cascade)

  @@id([issuer, subject])
}
```

在 `src/auth/oidc.controller.ts` 放入下列代码。`PrismaService` 的导入按项目目录调整。用同一份已发现的配置处理登录与回调。回调基址取预登记常量，请求参数取自实际请求。

```ts
import { Controller, Get, Header, Req, Res, UnauthorizedException } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { JwtService } from '@nestjs/jwt';
import type { Request, Response } from 'express';
import 'express-session';
import * as oidc from 'openid-client';
import { PrismaService } from '../prisma/prisma.service';

const origin = 'http://127.0.0.1:3000';
const redirectUri = `${origin}/auth/oidc/callback`;
type Attempt = { verifier: string; state: string; nonce: string };
declare module 'express-session' {
  interface SessionData { oidcAttempt?: Attempt }
}

@Controller('auth/oidc')
export class OidcController {
  private readonly provider: Promise<oidc.Configuration>;
  constructor(config: ConfigService, private readonly jwt: JwtService,
    private readonly prisma: PrismaService) {
    this.provider = oidc.discovery(new URL(config.getOrThrow('OIDC_ISSUER')),
      config.getOrThrow('OIDC_CLIENT_ID'), config.getOrThrow('OIDC_CLIENT_SECRET'));
    // 暂存发现失败，首次访问时由 Nest 处理。
    void this.provider.catch(() => undefined);
  }

  @Get('start')
  async start(@Req() req: Request, @Res() res: Response) {
    const config = await this.provider;
    const attempt = { verifier: oidc.randomPKCECodeVerifier(),
      state: oidc.randomState(), nonce: oidc.randomNonce() };
    const url = oidc.buildAuthorizationUrl(config, {
      redirect_uri: redirectUri, scope: 'openid', state: attempt.state,
      nonce: attempt.nonce, code_challenge_method: 'S256',
      code_challenge: await oidc.calculatePKCECodeChallenge(attempt.verifier),
    });
    req.session.oidcAttempt = attempt;
    await new Promise<void>((resolve, reject) => req.session.save(err => err ? reject(err) : resolve()));
    res.redirect(url.href);
  }

  @Get('callback')
  @Header('Cache-Control', 'no-store')
  async callback(@Req() req: Request) {
    const attempt = req.session.oidcAttempt;
    if (!attempt) throw new UnauthorizedException();
    delete req.session.oidcAttempt;
    await new Promise<void>((resolve, reject) => req.session.save(err => err ? reject(err) : resolve()));
    const currentUrl = new URL(redirectUri);
    currentUrl.search = new URL(req.originalUrl, origin).search;
    const config = await this.provider;
    const claims = await oidc.authorizationCodeGrant(config, currentUrl, {
      pkceCodeVerifier: attempt.verifier, expectedState: attempt.state,
      expectedNonce: attempt.nonce, idTokenExpected: true,
    }).then(result => result.claims()).catch(() => { throw new UnauthorizedException(); });
    if (!claims) throw new UnauthorizedException();
    const link = await this.prisma.externalIdentity.findUnique({
      where: { issuer_subject: { issuer: claims.iss, subject: claims.sub } },
    });
    if (!link) throw new UnauthorizedException();
    // 本机演示只签 access token，刻意不调用第 32 天的 issue() 双令牌流程：
    // 这里不产生 refresh token，令牌过期后需重新走一遍 OIDC 登录。
    // 生产接入应在绑定/首次登录时调用 AuthService.issue() 或等价流程，保持与密码登录一致的双令牌与撤销语义。
    return { accessToken: await this.jwt.signAsync({ sub: String(link.userId) }), expiresIn: 600 };
  }
}
```

在 `src/auth/auth.module.ts` 中仅当设置了 `OIDC_ISSUER` 且 `NODE_ENV !== 'production'` 时把 `OidcController` 加进现有 `controllers`，把导出 Prisma 服务的模块加入 `imports`。控制器仅用于本机演示，且回调只签 access token、不签发 refresh token：OIDC 演示复用 `JwtService.signAsync`，与第 32 天 `AuthService.issue()` 的双令牌体系不同，令牌过期必须重新授权。这是为缩小本机演示范围做的取舍，生产接入应在绑定/首次登录时调用 `issue()` 或等价流程，保持撤销和刷新语义一致。`src/main.ts` 在 `listen()` 前按同一条件挂 `app.use('/auth/oidc', session({ name: 'blog.oidc.sid', secret: process.env.OIDC_SESSION_SECRET!, resave: false, saveUninitialized: false, cookie: { httpOnly: true, sameSite: 'lax', maxAge: 300_000 } }))`，导入 `express-session` 的默认导出。用第 32 天命令生成独立的 `OIDC_SESSION_SECRET`，设置时先检查该值存在。生产接入需要 HTTPS、`Secure` Cookie、共享会话存储、明确的绑定流程，以及避免记录认证回调查询串的日志配置。

## 练习

用身份提供方演示账号完成一次 `/auth/oidc/start`。先不绑定，再用 `npx prisma studio` 按管理员核验的发行方和提供方后台所显示的协议 `sub` 建一条本地关联，指向测试 `User`。某些提供方给每个应用不同的 `sub`，值必须属于此客户端。邮箱只能用作联系信息。

## 参考答案与验收

`npm run start:dev` 后，本机 `/auth/oidc/start` 预期 302。浏览器同意授权后，未绑定账号回调为 401，已绑定账号用新的登录流程回调为 200；其应用访问令牌访问 `/auth/me` 应得到对应博客编号。直接打开没有登录上下文的 `/auth/oidc/callback` 应为 401。没有演示 IdP 时，只核对本地数据库迁移与错误分支，将完整回调列为待验证。

## AI 搭档

提示词「为博客外部登录说明授权码、ID Token 和应用访问令牌分别由谁签发、用在哪里。」人工检查 `(iss, sub)` 双键和四条预期状态。删去 Cookie、授权码、真实标识和全部令牌再分享。

# 第 35 天：给博客建立 Web 防护基线

原课：<https://xiguadev.com/node-60days/day-35>

## 今日先学

把防护落到每个入口。DTO ValidationPipe 拦住不符合约定的输入。Helmet 添加安全响应头。同源页面按文本渲染用户内容，富文本需使用成熟净化库并配置 CSP。跨域 CORS 只授权指定浏览器来源，无论来源如何，服务端都照常校验身份。若网页用 Cookie 自动携带凭据，写操作需要 CSRF 保护。使用 Prisma 参数化查询，动态排序字段从固定列表选择。登录限流之外，还需要通用错误、可靠的密码哈希及最少字段回显。

## 跟做

在博客根目录执行 `npm i helmet @nestjs/throttler class-validator class-transformer`。在 `src/main.ts` 的 `listen()` 之前合并配置，若已有 ValidationPipe 就修改原实例。这里针对本地开发前端，默认不需要跨域时省略 `enableCors`。

```ts
import helmet from 'helmet';
import { ValidationPipe } from '@nestjs/common';

// bootstrap 内，已有 app
app.use(helmet());
app.useGlobalPipes(new ValidationPipe({
  whitelist: true, forbidNonWhitelisted: true, transform: true,
}));
if (process.env.WEB_ORIGIN) {
  const origin = new URL(process.env.WEB_ORIGIN).origin;
  app.enableCors({ origin });
}
```

在 `src/app.module.ts` 或 `src/auth/auth.module.ts` 的 `imports` 中加入 `ThrottlerModule.forRoot([{ ttl: 60_000, limit: 5 }])`。从 `@nestjs/throttler` 导入该模块和 Guard，在现有 `POST /auth/login` 方法加 `@UseGuards(ThrottlerGuard)`。本地按来源 IP 计数，生产多实例用共享限流存储，反向代理仅信任部署明确配置的代理链。建议在入口设置体积上限和超时。浏览器使用不同域且确需 Cookie 时，显式配置允许来源和 `credentials`，并落地 CSRF 防护。

## 练习

在 `src/posts/dto/create-post.dto.ts` 检查标题规则，使用测试账号验证正常标题和空白标题。再在刚重启的本地服务验证登录频率限制。同一个本机测试客户端内，先完成一次合法登录，再在一分钟内逐次提交五次相同合法登录请求。

## 参考答案与验收

在原 DTO 的 `title` 上应用这些规则，保留原文内容字段的校验。确保控制器的 `@Body()` 类型用该 DTO 类。示例用 `@Matches` 保证至少有一个非空白字符。

```ts
import { IsString, Length, Matches } from 'class-validator';

export class CreatePostDto {
  @IsString()
  @Length(1, 120)
  @Matches(/\S/)
  title!: string;
  // 原有正文等字段沿用既有校验规则。
}
```

执行 `npm run build`、`npm run start:dev`。带有效认证的新建文章，普通标题应为 201，纯空白标题应为 400。一分钟内前五次登录应为 200，第六次为 429，窗口结束后再试应恢复。用 `curl -i http://127.0.0.1:3000/auth/me` 检查 401 响应也有 `X-Content-Type-Options: nosniff`。检查正常响应和错误日志均无密码、Cookie 与令牌。

## AI 搭档

提示词「根据这份脱敏的入口配置，列出 DTO、浏览器安全头和 IP 限流分别通过哪个本地测试验收。」人工核对上面的 201、400、401、429 和响应头。只提供配置结构及状态码，无须提交原始请求体或真实凭据。


# 第 36 天：给博客 Post 列表加 Redis 缓存

原课：<https://xiguadev.com/node-60days/day-36>

## 今日先学

缓存是可丢弃的副本，不是 `Post` 的事实来源。今天让 PostgreSQL 仍保存博客数据，用 Redis 缓存公开文章列表，设置过期时间，文章新增、修改、删除后主动删除相关键。缓存命中可以减少重复查询，但必须接受短暂的旧数据风险，并设计数据库不可用、Redis 不可用时的降级路径。Redis 只放可重建数据，不放密码、JWT 秘密或未经保护的个人资料。

第 41 天才开始 Docker。本阶段优先选择 WSL2/Linux 的原生 Redis、公司提供的托管 Redis，或本机已有的 Redis 服务。Windows 暂时没有 Redis 时，不要为了赶进度安装来路不明的服务；可设置 `CACHE_ENABLED=false`，走数据库路径完成代码学习。以下命令只是示例，不表示本机已安装或已执行。

## 跟做

在博客项目目录安装成熟客户端：

```bash
npm i ioredis
```

在 `.env` 中只保存连接地址，真实密码由本地环境变量或部署平台密钥注入。没有 Redis 时保持关闭：

```text
REDIS_URL=redis://127.0.0.1:6379
CACHE_ENABLED=false
```

在 `src/cache/redis.service.ts` 创建 Redis 边界。`ioredis` 的客户端只在开关开启时创建；连接错误打印脱敏事件，不把 URL 中的密码写入日志。

```ts
import { Injectable, Logger, OnModuleDestroy } from '@nestjs/common';
import Redis from 'ioredis';

@Injectable()
export class RedisService implements OnModuleDestroy {
  private readonly log = new Logger(RedisService.name);
  private readonly client?: Redis;

  constructor() {
    if (process.env.CACHE_ENABLED !== 'true') return;
    const url = process.env.REDIS_URL;
    if (!url) throw new Error('CACHE_ENABLED=true 时必须设置 REDIS_URL');
    this.client = new Redis(url, { maxRetriesPerRequest: 1, enableOfflineQueue: false });
    this.client.on('error', () => this.log.warn('Redis 连接不可用，缓存将降级'));
  }

  async get(key: string) {
    return this.client?.get(key) ?? null;
  }
  async setJson(key: string, value: unknown, ttlSeconds: number) {
    await this.client?.set(key, JSON.stringify(value), 'EX', ttlSeconds);
  }
  async del(...keys: string[]) {
    if (keys.length) await this.client?.del(...keys);
  }
  async onModuleDestroy() { await this.client?.quit(); }
}
```

在 `src/cache/cache.module.ts` 放入下面模块，让 `PostsModule` 导入 `CacheModule`，并在 `PostsService` 构造器注入 `private readonly redis: RedisService`，从对应文件导入类。

```ts
import { Module } from '@nestjs/common';
import { RedisService } from './redis.service';

@Module({ providers: [RedisService], exports: [RedisService] })
export class CacheModule {}
```

`PostsService.listPublic()` 先读取 `blog:posts:public:v1`。`RedisService.get()` 未命中返回 `null`，而 `JSON.parse(null)` 会返回 `null` 却不抛异常，所以必须先判空再解析；有合法缓存才返回，解析失败或形状不对先删除坏键再查库；无缓存查 Prisma，成功后写入 30 秒。沿用前课 `publishedAt` 非空表示发布、`body` 表示正文的模型。要让两条路径返回同样的形状：缓存里的 `createdAt` 经 `JSON.parse` 后是字符串，Prisma 查出来是 `Date`，这里统一在返回前转成 ISO 字符串。Redis 读写异常被捕获，不能因为缓存故障让公开博客整体 500。缓存只保存公开字段。

```ts
async listPublic() {
  const key = 'blog:posts:public:v1';
  try {
    const cached = await this.redis.get(key);
    // 关键：JSON.parse(null) 返回 null 而不抛异常，必须先判空；
    // 否则缓存未命中时不会进 catch，会直接 return null，下面的查库永远不执行。
    if (cached !== null) {
      const parsed = JSON.parse(cached) as { id: number; title: string; body: string; authorId: number; createdAt: string }[];
      if (Array.isArray(parsed)) return parsed;
      // 形状不对也按坏键处理
      await this.redis.del(key).catch(() => undefined);
    }
  } catch {
    // JSON 解析失败或 Redis 异常：删除坏键，继续走数据库
    await this.redis.del(key).catch(() => undefined);
  }

  const posts = await this.prisma.post.findMany({
    where: { publishedAt: { not: null } },
    select: { id: true, title: true, body: true, authorId: true, createdAt: true },
    orderBy: { createdAt: 'desc' }, take: 20,
  });
  // 统一形状：DB 的 Date 与缓存里的字符串都对外暴露为 ISO 字符串
  const shaped = posts.map((p) => ({ ...p, createdAt: p.createdAt.toISOString() }));
  await this.redis.setJson(key, shaped, 30).catch(() => undefined);
  return shaped;
}
```

在真实存在的四个写操作成功提交数据库后调用 `await this.redis.del('blog:posts:public:v1').catch(() => undefined)`，避免数据库已写成功却因 Redis 故障向客户端报失败：**第 33 天的 `createForActor`**（不是第 27 天那个已被整体替换掉的旧 `create()`）、`update`、`remove` 和 `publish`。只删公开列表键即可，因为只有这些操作会改变公开可见性；写进被替换掉的死代码不会触发失效。先写数据库再删缓存，仍可能有并发读回填旧值，30 秒 TTL 限制本实验的陈旧时间。多页列表把分页参数纳入键，或先只缓存固定首页。

## 练习

在 `GET /posts/public` 接入 `listPublic()` 时，先确认控制器里静态路由 `@Get('public')` 声明在 `@Get(':id')` **之前**；否则 `public` 会先命中 `ParseIntPipe` 变成 400，缓存代码根本不会被调用。分别打开和关闭 `CACHE_ENABLED` 请求两次。打开时可以用 Redis CLI 的 `GET blog:posts:public:v1` 观察键；没有 Redis 时确认 API 仍从 PostgreSQL 返回同样结果。新增一篇已发布 `Post` 后立刻再次请求列表。

## 参考答案与验收

缓存打开且 Redis 正常时，第一次请求是未命中并查库，第二次在 30 秒内读同一键；新增文章后缓存键被删除，下一次列表能看到新文章。`CACHE_ENABLED=false` 或 Redis 连接失败时，接口仍返回 200 和数据库结果；没有文章时返回空数组。`GET /posts/public` 不应返回 `User.passwordHash` 等内部字段。`curl -i` 检查 Redis 不可用时不是 500，新增失败时也不应删除旧的有效缓存。

建议加一个 `node:test` 或现有测试：把 Redis 服务替换为记录调用的假对象，断言列表第一次调用 `get` 后查询数据库并 `setJson`，第二次命中后不调用 Prisma，创建成功后调用 `del`。这是逻辑验收，不宣称已在本机执行。

## AI 搭档

提示词「阅读这段脱敏的博客缓存服务，列出事实来源、缓存键、TTL、失效时机和 Redis 故障降级路径；不要猜测未提供的配置。」人工逐项对照代码。分享前删除 Redis URL、数据库连接串、用户邮箱、令牌和文章私密内容。

# 第 37 天：掌握 Redis 的键、TTL 与原子操作

原课：<https://xiguadev.com/node-60days/day-37>

## 今日先学

Redis 常见数据结构有 String、Hash、List、Set 和 Sorted Set。博客先使用 String 存 JSON 缓存，使用 Set 做失效索引，使用 `INCR` 加计数。每个键都应有命名空间、版本和明确 TTL。`GET` 与 `SET EX` 是基本读写；多个命令分开执行不一定是原子的，需要 Redis 事务或 Lua 脚本。Redis 的计数可以辅助限流，但多实例部署要统一连接与过期策略，不能把它误认为业务数据库事务。

## 跟做

Windows 没有 Redis 时可继续使用 `CACHE_ENABLED=false`，把下面脚本作为阅读和单元测试材料；不要把“能写代码”说成“已经连通 Redis”。在 WSL2/Linux 或托管 Redis 中，确认服务地址来自环境变量后，创建 `labs/redis-smoke.mjs`：

```js
import Redis from 'ioredis';

const url = process.env.REDIS_URL;
if (!url) throw new Error('请通过环境变量提供 REDIS_URL');
const redis = new Redis(url, { maxRetriesPerRequest: 1 });
try {
  const key = `blog:lab:${Date.now()}`;
  await redis.set(key, JSON.stringify({ postId: 7 }), 'EX', 30);
  console.log('read:', await redis.get(key));
  console.log('ttl:', await redis.ttl(key));
  await redis.del(key);
  console.log('after delete:', await redis.get(key));
} finally {
  await redis.quit();
}
```

运行 `node labs/redis-smoke.mjs`。预期依次看到包含 `postId` 的 JSON、0 到 30 之间的 TTL、最后的 `null`。不要用 `KEYS *` 作为线上清理方式，它会在大键空间阻塞服务。需要查询本应用键时使用受控的 `SCAN`，并限制批量数量。

在 `src/cache/post-cache.ts` 实现版本化键函数，禁止调用方随意传入整段 URL 作为键。文章列表和文章详情使用不同键；文章更新后删除详情键以及列表索引。若维护文章到缓存键的映射，可使用 Set：`SADD blog:post:keys:<id> blog:post:v1:<id>`，清理时 `SMEMBERS` 后 `DEL`，最后删 Set。缓存键本身仍须设置过期时间。

对于“每个用户每分钟最多 5 次预览”的学习实验，使用 `INCR` 加 `EXPIRE`，但先说明两个命令之间存在并发窗口。需要严格窗口时使用成熟限流包或 Lua 原子脚本；业务扣款、库存等关键状态必须由 PostgreSQL 事务负责。不要把客户端传入的用户 ID 当作身份，使用第 32 天 Guard 得到的 `req.user.sub`。

## 练习

写一个 `countPreview(userId: string)` 函数，放进第 36 天的 `RedisService` 类，直接使用其私有 `client`，不能向只有 `get/setJson/del` 的包装器调用不存在的 `incr/expire`。键格式为 `blog:preview:v1:<userId>:<当前分钟>`，首次计数设置 60 秒 TTL。返回当前次数；超过 5 次让控制器返回 429。测试同一虚构用户连续调用 6 次，另一个用户调用一次，确认两个计数互不影响。没有 Redis 时此计数实验标为未验证。

## 参考答案与验收

学习版的核心逻辑如下，真实项目还要处理 Redis 故障、并发原子性和键长度限制：

```ts
async countPreview(userId: string) {
  if (!/^[a-zA-Z0-9_-]{1,80}$/.test(userId)) throw new Error('invalid id');
  const minute = Math.floor(Date.now() / 60_000);
  const key = `blog:preview:v1:${userId}:${minute}`;
  if (!this.client) throw new Error('计数实验需要 Redis');
  const count = await this.client.incr(key);
  if (count === 1) await this.client.expire(key, 60);
  return count;
}
```

验收时同一用户的返回值应为 1、2、3、4、5、6；控制器对第 6 次返回 429，另一个用户仍从 1 开始。等待窗口或使用测试时钟后计数自然过期。检查键上有 TTL，代码没有 `KEYS *`，也没有硬编码 Redis 密码。若要宣布严格通过并发测试，应改用成熟限流实现或原子脚本，而不是把这段学习代码直接当生产方案。

## AI 搭档

提示词「比较 `INCR` 后 `EXPIRE` 与原子 Lua 限流的并发差异，只根据这段脱敏代码给出测试矩阵。」人工验收要求包含首次计数、超限、不同用户、过期和 Redis 失败五种情况。AI 输入不能包含连接地址中的密码、真实 IP、Cookie 或用户 ID。

# 第 38 天：用 BullMQ 把耗时任务放到队列

原课：<https://xiguadev.com/node-60days/day-38>

## 今日先学

HTTP 请求适合快速确认“任务已接收”，不适合一直等待图片处理、邮件发送或文章索引。BullMQ 使用 Redis 保存队列状态：生产者把任务放入队列，Worker 取出处理，失败后按策略重试。任务必须可重试和幂等，不能把密码、原始令牌或整份敏感对象放进 job data。API 返回 202 表示已接受，不等于任务已完成；完成状态应通过查询接口或通知获得。

## 跟做

在博客项目安装成熟库：

```bash
npm i @nestjs/bullmq bullmq
```

BullMQ 不能脱离 Redis。第 46 天以前的博客继续使用当前项目。先在 `Post` 模型追加 `updatedAt DateTime @default(now()) @updatedAt @map("updated_at") @db.Timestamptz(3)`，执行 `npx prisma migrate dev --name post_updated_at`、`npx prisma generate`，后面的任务版本来自这个字段。

本地接入队列前必须提供可用的 `REDIS_URL`，`CACHE_ENABLED=false` 只关闭缓存。没有 Redis 时暂不把下面的 `QueueModule` 加入 `PostsModule` 或 `AppModule`，通过可选队列依赖完成数据库路径与假队列测试，真实消费标为未验证。配置放在 `src/queue/queue.module.ts`。将 URL 拆成 ioredis 的连接参数，不把未经处理的 `{ url }` 当作连接选项。

```ts
import { Module } from '@nestjs/common';
import { ConfigModule, ConfigService } from '@nestjs/config';
import { BullModule } from '@nestjs/bullmq';
import { PrismaModule } from '../prisma/prisma.module';
import { PostIndexProcessor } from './post-index.processor';

@Module({
  imports: [PrismaModule, BullModule.forRootAsync({
    imports: [ConfigModule], inject: [ConfigService],
    useFactory: (config: ConfigService) => {
      const url = new URL(config.getOrThrow<string>('REDIS_URL'));
      if (!['redis:', 'rediss:'].includes(url.protocol)) throw new Error('Redis 协议无效');
      const db = Number(url.pathname.slice(1) || '0');
      if (!Number.isInteger(db) || db < 0) throw new Error('Redis DB 无效');
      return { connection: {
        host: url.hostname, port: Number(url.port || 6379), db,
        username: url.username ? decodeURIComponent(url.username) : undefined,
        password: url.password ? decodeURIComponent(url.password) : undefined,
        ...(url.protocol === 'rediss:' ? { tls: {} } : {}),
        maxRetriesPerRequest: null, enableOfflineQueue: false,
      } };
    },
  }), BullModule.registerQueue({ name: 'post-index' })],
  providers: [PostIndexProcessor],
  exports: [BullModule],
})
export class QueueModule {}
```

有 Redis 时在 `PostsModule` 导入 `QueueModule`。在 `PostsService` 的 Nest 导入中增加 `Optional`、`ServiceUnavailableException`，从 `@nestjs/bullmq` 导入 `InjectQueue`，从 `bullmq` 导入 `Queue`。在已有构造器参数后追加 `@Optional() @InjectQueue('post-index') private readonly indexQueue?: Queue`。将下面方法加入服务，重新索引端点调用它。没有队列或入队失败时返回 503；不能假装任务已接收。任务只传文章编号、动作和版本，消费者从数据库重读。

```ts
async enqueueIndex(postId: number) {
  const post = await this.prisma.post.findUnique({ where: { id: postId } });
  if (!post) throw new NotFoundException();
  if (!this.indexQueue) throw new ServiceUnavailableException('队列未启用');
  try {
    const job = await this.indexQueue.add('refresh',
      { postId: post.id, operation: 'upsert', version: post.updatedAt.toISOString() },
      { jobId: `post-${post.id}-${post.updatedAt.getTime()}`,
        attempts: 3, backoff: { type: 'exponential', delay: 1000 },
        removeOnComplete: { age: 3600, count: 1000 },
        removeOnFail: { age: 86_400 } });
    return { jobId: job.id };
  } catch {
    throw new ServiceUnavailableException('队列暂不可用');
  }
}
```

本课先由管理员显式调用重建端点，不在创建文章后直接追加可能失败的 `await add()`；这样不会出现文章已提交却向客户端报创建失败的情况。若以后要自动入队，先补 Outbox 与补偿处理。新建 `src/queue/post-index.processor.ts`。下面是实际可接入的本地日志消费者，不连接搜索服务，也不声称已经建立搜索索引；重复消费只会重复输出同一个结构化事件。生产需要单独的搜索适配器和消费进程。

```ts
import { Logger } from '@nestjs/common';
import { Processor, WorkerHost } from '@nestjs/bullmq';
import { Job } from 'bullmq';
import { PrismaService } from '../prisma/prisma.service';

@Processor('post-index')
export class PostIndexProcessor extends WorkerHost {
  private readonly log = new Logger(PostIndexProcessor.name);
  constructor(private readonly prisma: PrismaService) { super(); }

  async process(job: Job<{ postId: number; operation: 'upsert'; version: string }>) {
    if (!Number.isSafeInteger(job.data.postId) || job.data.postId <= 0 ||
      job.data.operation !== 'upsert') throw new Error('invalid job data');
    const post = await this.prisma.post.findUnique({
      where: { id: job.data.postId }, select: { id: true, updatedAt: true },
    });
    if (!post) return { skipped: 'deleted' };
    this.log.log(JSON.stringify({ event: 'post.index.demo', jobId: job.id,
      postId: post.id, version: post.updatedAt.toISOString() }));
    return { processed: post.id, demoOnly: true };
  }
}
```

## 练习

在 `PostsService` 加入下面管理员入口，从 Nest 导入 `ForbiddenException`。在已有 `PostsController` 新增方法 `@Post(':id/reindex') @UseGuards(JwtAuthGuard) @HttpCode(202)`，参数为 `@Param('id', ParseIntPipe) id: number, @Req() req: AuthRequest`，返回 `this.posts.reindex(id, req.user!.sub)`，补齐装饰器及 Guard 的导入。

```ts
async reindex(id: number, sub: string) {
  if (!/^[1-9]\d*$/.test(sub) || !Number.isSafeInteger(Number(sub))) {
    throw new UnauthorizedException();
  }
  const actor = await this.prisma.user.findUnique({ where: { id: Number(sub) } });
  if (!actor) throw new UnauthorizedException();
  if (actor.role !== 'ADMIN') throw new ForbiddenException();
  return this.enqueueIndex(id);
}
```

用 mock Queue 断言 payload 只有 `postId`、`operation`、`version`，没有 `passwordHash`、JWT 或正文全文。为模拟失败的处理器设置前两次抛错、第三次成功，对应 `attempts: 3`（总共三次，包含首次）。

## 参考答案与验收

管理员提交有效文章编号时应返回 202 和任务标识；普通用户返回 403，未登录返回 401，不存在文章返回 404。队列选项应有 `attempts: 3` 或经过明确评估的更小值，退避时间大于 0，并设置完成/失败清理策略。集成环境可观察：前两次抛错、第三次成功时任务最终 completed；只有三次都失败才进入 failed；学习版不连接 Redis 时，用 mock Queue 断言 `add('refresh', ...)` 被调用一次，并检查 data 仅含允许字段。队列 Redis 断开时，API 应返回明确的 503 或统一错误，而不是假装任务已完成。

## AI 搭档

提示词「把这个文章重建索引任务改造成可重试幂等设计：指出 jobId、最少字段、删除文章时的结果和临时失败的处理方式。」人工检查 API 的 202 语义和管理员授权。只发送字段名和虚构文章编号，删掉队列地址、日志、令牌和真实内容。

# 第 39 天：安全接收并隔离文章图片

原课：<https://xiguadev.com/node-60days/day-39>

## 今日先学

上传安全不等于只检查文件名。请求大小、字段数量、扩展名、声明 MIME、文件内容、随机存储名、保存目录权限和后续处理都要有边界。允许列表比黑名单可靠；文件不直接放进静态公开目录，先进入隔离区，必要时经过病毒扫描、图片解码和重编码，再上传对象存储。服务端生成名字，不能信任客户端的 `originalname`。今天只实现防御和预期状态码，不进行攻击复现、payload 或网站扫描。

## 跟做

安装 Nest 官方上传适配所需的成熟包。若项目已有 `@nestjs/platform-express`，只需补充 `multer` 类型（按项目 TypeScript 配置决定）。

```bash
npm i multer
npm i -D @types/multer
```

在 `.env` 配置上传根目录和上限，路径应位于应用工作目录外或专门挂载卷。示例不包含真实秘密：

```text
UPLOAD_ROOT=./var/quarantine
UPLOAD_MAX_BYTES=5242880
```

在 `src/uploads/upload.validation.ts` 建立允许列表和随机名。只允许 JPEG、PNG、WebP 的声明类型和扩展名组合；真实生产流程仍应读取文件头或交给图片处理服务验证，不能仅信任 `mimetype`。磁盘存储使用随机 UUID，保留原始扩展名只为后续处理提示，不用于路径拼接。

```ts
import { BadRequestException } from '@nestjs/common';
import { randomUUID } from 'node:crypto';
import { extname } from 'node:path';

const allowed = new Map([
  ['image/jpeg', '.jpg'], ['image/png', '.png'], ['image/webp', '.webp'],
]);

export function safeUploadName(mimetype: string, originalname: string) {
  const expected = allowed.get(mimetype);
  const extension = extname(originalname).toLowerCase();
  if (!expected || extension !== expected) throw new BadRequestException('不支持的文件类型');
  return `${randomUUID()}${expected}`;
}
```

先在博客项目根目录的 `prisma/schema.prisma` 追加封面元数据模型，并在项目根执行 `npx prisma migrate dev --name post_cover_meta`（`api/prisma/` 是第 47 天起协作任务板的路径，博客项目用 `prisma/`，照抄会建在错误目录）。这个迁移是第 40 天里程碑要检查的对象；生产版本还应补上到 `Post` / `Author` 的外键，这里用整数 ID 保持练习库可独立迁移。`PostCover.ownerId` 存的是 `Author.id`，不是 JWT 里的 `User.id`。

```prisma
model PostCover {
  id         String   @id @default(uuid())
  postId     Int
  ownerId    Int
  storedName String   @unique
  mimeType   String
  byteSize   Int
  createdAt  DateTime @default(now())

  @@index([postId])
}
```

在 `src/uploads/uploads.controller.ts` 用 `FileInterceptor`。`limits.fileSize` 是 Multer 层限制，仍需在业务层检查 `file.size`；设置字段名、数量和请求大小上限。上传路由必须有 JWT Guard，`User` 身份从 `req.user.sub` 得到，不从表单接收 ownerId；`sub` 是 `User.id`，要与文章 `authorId`（`Author.id`）比较必须先查 `User.authorId` 映射。隔离目录要由后端提前创建并限制权限，文件保存成功后写 `Post` 的图片元数据。数据库写入失败时删除临时文件。

```ts
// src/uploads/uploads.controller.ts（完整文件）
import {
  BadRequestException, Controller, Param, ParseIntPipe, PayloadTooLargeException,
  Post, Req, UploadedFile, UseGuards, UseInterceptors,
} from '@nestjs/common';
import { FileInterceptor } from '@nestjs/platform-express';
import { JwtAuthGuard, type AuthRequest } from '../auth/jwt-auth.guard';
import { safeUploadName } from './upload.validation';
import { UploadsService } from './uploads.service';

@Controller('posts')
export class UploadsController {
  constructor(private readonly uploads: UploadsService) {}

  @Post(':id/cover')
  @UseGuards(JwtAuthGuard)
  @UseInterceptors(FileInterceptor('cover', {
    dest: process.env.UPLOAD_ROOT ?? './var/quarantine',
    limits: { fileSize: 5 * 1024 * 1024, files: 1, fields: 10 },
    fileFilter: (_req, file, cb) => {
      try { safeUploadName(file.mimetype, file.originalname); cb(null, true); }
      catch { cb(new BadRequestException('不支持的文件类型'), false); }
    },
  }))
  async cover(@Param('id', ParseIntPipe) id: number,
    @UploadedFile() file: Express.Multer.File, @Req() req: AuthRequest) {
    if (!file) throw new BadRequestException('必须上传 cover');
    if (file.size > 5 * 1024 * 1024) throw new PayloadTooLargeException();
    return this.uploads.attachCover(id, file, req.user!.sub);
  }
}
```

`UploadsService` 负责归属检查、用 `safeUploadName` 的返回值改名、写数据库，并在失败时删除临时文件。把下面两个文件放进 `src/uploads/`，再把 `UploadsModule` 加入 `AppModule` 的 `imports`。没有这一步，上面的控制器会因为找不到 `uploads` provider 而无法启动。

```ts
// src/uploads/uploads.service.ts
import { BadRequestException, ForbiddenException, Injectable, NotFoundException } from '@nestjs/common';
import { promises as fs } from 'node:fs';
import { join, resolve } from 'node:path';
import { PrismaService } from '../prisma/prisma.service';
import { safeUploadName } from './upload.validation';

@Injectable()
export class UploadsService {
  private readonly root = resolve(process.env.UPLOAD_ROOT ?? './var/quarantine');

  constructor(private readonly prisma: PrismaService) {}

  async attachCover(postId: number, file: Express.Multer.File, sub: string) {
    const userId = Number(sub);
    if (!Number.isSafeInteger(userId) || userId < 1) throw new BadRequestException();
    // sub 是 User.id，Post.authorId 是 Author.id；必须先按 Day32 的映射查出 authorId。
    const actor = await this.prisma.user.findUnique({
      where: { id: userId }, select: { authorId: true },
    });
    if (!actor?.authorId) throw new ForbiddenException();
    const ownerId = actor.authorId;
    const post = await this.prisma.post.findUnique({ where: { id: postId } });
    if (!post) throw new NotFoundException();
    if (post.authorId !== ownerId) throw new ForbiddenException();

    const storedName = safeUploadName(file.mimetype, file.originalname);
    await fs.mkdir(this.root, { recursive: true, mode: 0o700 });
    const source = join(this.root, file.filename);
    const target = join(this.root, storedName);
    try {
      await fs.rename(source, target);
      return await this.prisma.postCover.create({
        data: { postId, ownerId, storedName, mimeType: file.mimetype, byteSize: file.size },
        select: { id: true, postId: true, mimeType: true, byteSize: true, createdAt: true },
      });
    } catch (error) {
      await fs.unlink(source).catch(() => undefined);
      await fs.unlink(target).catch(() => undefined);
      throw error;
    }
  }
}
```

```ts
// src/uploads/uploads.module.ts
import { Module } from '@nestjs/common';
import { UploadsController } from './uploads.controller';
import { UploadsService } from './uploads.service';

@Module({ controllers: [UploadsController], providers: [UploadsService] })
export class UploadsModule {}
```

上面的 `dest` 版本会先由 Multer 生成临时文件名；更严格的实现应使用 `diskStorage` 的随机 `filename`，在业务层读取文件头，验证成功后移动到不可执行的隔离目录。响应不要回传服务器绝对路径，只返回数据库生成的资源 ID。下载接口用认证和归属判断，或由对象存储发短时签名 URL；不要直接把整个 `UPLOAD_ROOT` 暴露为静态目录。

## 练习

用本地测试客户端准备一个允许的 PNG 和一个不在允许列表的文本文件，分别提交 `multipart/form-data` 字段 `cover`。再提交一个超过 5 MiB 的测试文件。检查服务响应和隔离目录；不要上传真实身份证件、客户图片或任何含敏感信息的文件。

## 参考答案与验收

允许的图片在请求身份、文章归属都满足时返回 201 或项目约定的 200，并返回资源 ID；不支持的类型返回 400，过大返回 413，未登录返回 401，非文章作者按规则返回 403，不存在的文章返回 404。失败上传不应在可访问目录留下文件，数据库中不应出现未完成的附件记录。成功文件名应为随机值，不能包含原始文件名中的路径片段；响应中不能出现服务器绝对路径、Cookie 或令牌。

补一个服务测试：把 `safeUploadName('image/png', 'cover.png')` 断言为随机 `.png` 名；把 `safeUploadName('text/plain', 'cover.txt')` 断言抛出 `BadRequestException`。测试文件大小、归属和清理逻辑时使用临时目录与虚构内容。真实生产验收还要增加文件头验证、病毒扫描、重编码和对象存储权限检查。

## AI 搭档

提示词「根据这段脱敏上传控制器，列出允许列表、大小限制、隔离保存、归属检查和异常清理的人工验收项，并给出期望状态码。」人工逐项检查 401、403、404、400、413 与成功路径。不要将真实文件、原始文件名、绝对路径、令牌或图片内容发送给 AI。

# 第 40 天：博客安全与异步能力里程碑

原课：<https://xiguadev.com/node-60days/day-40>

## 今日先学

今天不引入新平台，而是把第 31–39 天串成一个可验收的博客里程碑。完成后，博客使用 JWT 认证，`User` 的角色和 `Post.authorId` 控制文章操作；公开 `Post` 列表可用 Redis 缓存但 Redis 故障能降级；重新索引使用 BullMQ 任务；封面上传经过允许列表、大小上限和隔离保存；所有秘密来自环境或平台密钥。这个博客仍是练习项目，协作任务板到第 46 天再迁移，不能把当前代码直接宣称为生产系统。

## 跟做

先执行 `npm i zod`，再在 `src/config/env.validation.ts` 集中校验配置。这里把 `DATABASE_URL`、`UPLOAD_MAX_BYTES`、`WEB_ORIGIN`、`OIDC_*`、`PORT`、`HOST` 一并纳入；`UPLOAD_MAX_BYTES` 定义后**必须在第 39 天的上传拦截器里读取**，否则校验通过却仍硬编码 5 MiB，等于没有生效。缓存开关必须有明确语义；启用 Redis 缓存时缺少 URL 直接启动失败，关闭时列表只走 PostgreSQL。队列是否可用取决于是否接入第 38 天模块，与缓存开关独立。不要在校验失败时打印整份 `process.env`。

```ts
import { z } from 'zod';

export const envSchema = z.object({
  NODE_ENV: z.enum(['development', 'test', 'production']).default('development'),
  PORT: z.coerce.number().int().min(1).max(65535).default(3000),
  HOST: z.string().min(1).default('127.0.0.1'),
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),
  CACHE_ENABLED: z.enum(['true', 'false']).default('false'),
  REDIS_URL: z.string().url().optional(),
  UPLOAD_ROOT: z.string().min(1).default('./var/quarantine'),
  UPLOAD_MAX_BYTES: z.coerce.number().int().min(1).max(10 * 1024 * 1024).default(5 * 1024 * 1024),
  WEB_ORIGIN: z.string().url().optional(),
  OIDC_ISSUER: z.string().url().optional(),
  OIDC_CLIENT_ID: z.string().optional(),
  OIDC_CLIENT_SECRET: z.string().optional(),
});

export function validateEnv(input: Record<string, unknown>) {
  const result = envSchema.superRefine((env, ctx) => {
    if (env.CACHE_ENABLED === 'true' && !env.REDIS_URL) {
      ctx.addIssue({ code: 'custom', path: ['REDIS_URL'], message: '缓存开启时必须设置' });
    }
  }).safeParse(input);
  if (!result.success) throw new Error('环境配置无效');
  return result.data;
}
```

在 `AppModule` 用 `ConfigModule.forRoot({ isGlobal: true, validate: validateEnv })`，保留 `PrismaModule`、`AuthModule`、`PostsModule` 和已完成的 `UploadsModule`；只有具备 Redis 时才按第 38 天让 `PostsModule` 导入 `QueueModule`，不要为里程碑无条件在根模块重复导入。无队列时重建端点明确返回 503。为 `GET /health` 增加基础进程状态；不要为了健康检查把 Redis 故障伪装成正常。可分成 liveness（进程活着）和 readiness（数据库、必须依赖可用），并写清这两个端点的用途。日志只记录事件名、请求 ID、状态码和耗时，禁止记录 `Authorization`、Cookie、密码、刷新令牌、完整上传路径和连接字符串。

把里程碑验收写入 `test/milestone.checklist.md` 之外的自动化测试文件（不要把秘密放进测试）。至少覆盖：Guard 的 401、角色/归属的 403、未知 Post 的 404；缓存命中与失效；队列任务的 202 与最少 payload；上传的 400/413；健康检查的 200。集成测试使用独立测试数据库和临时上传目录，结束时清理；若没有 Redis，标记队列和缓存集成为“环境未提供”，同时运行不依赖 Redis 的降级测试。

## 练习

执行一次人工里程碑走查。创建两个虚构 `User` 和两篇 `Post`，按作者、管理员、未登录三种身份验收文章操作；关闭 Redis 验收公开列表；用假队列验收管理员重建索引；用允许和拒绝文件验收上传。将每条结果写到自己的检查表中，只保存状态码、测试编号和“通过/未验证”，不保存令牌、密码或个人信息。

## 参考答案与验收

最低通过线如下：

| 检查 | 预期 |
| --- | --- |
| 未登录访问需认证的接口 | 401 |
| 普通用户操作他人 `Post` | 403，数据不改变 |
| 请求不存在的 `Post` | 404 |
| Redis 关闭时公开列表 | 仍由 PostgreSQL 返回 200 |
| 管理员提交重建任务 | 202，任务数据不含秘密 |
| 队列不可用 | 明确 503 或统一依赖错误，不返回假成功 |
| 不允许的上传类型 | 400 |
| 超过 5 MiB | 413 |
| 正常健康检查 | 200，响应不含秘密 |

运行 `npm run build` 和已有测试命令时，若环境具备依赖再记录实际结果；本讲义没有替你执行，也不把未提供的 PostgreSQL、Redis、身份提供方或队列服务说成已验证。检查 Prisma 迁移文件、`User.role`、`Post.authorId`、外部身份联合键，以及 `post_cover_meta`（`PostCover` 模型）迁移是否已提交。确认 `.env`、上传目录和临时测试文件均在忽略规则中。

完成后应能解释一条完整链路：JWT Guard 得到 `User`，服务根据角色与 `Post.authorId` 授权，Post 查询可从 Redis 读取，写入后失效缓存，管理员任务进入 BullMQ，Worker 按 `postId` 读取最新数据，上传文件留在隔离区。不能解释或没有对应测试的部分标为未验证，留到后续补齐。

## AI 搭档

提示词「这是一个脱敏的博客里程碑检查表，请按认证、授权、缓存、队列、上传、配置和日志分类，指出缺失的人工验收项；不要补造服务已运行的结论。」人工以状态码和数据是否改变为准，逐条复核。提交给 AI 前只保留虚构编号、字段名、测试结果和错误类别。


# 第 41 天：用 Docker 打包博客 API

原课：<https://xiguadev.com/node-60days/day-41>

## 今日先学

从今天开始学 Docker。镜像是可重复运行的应用包，容器是镜像的运行实例。PostgreSQL 16 是博客数据库，本课只打包 NestJS 11 API，不把数据库密码或 JWT 密钥写入镜像。`.dockerignore` 排除依赖、版本库、`.env`、构建缓存和上传数据。生产进程使用非 root 用户，容器内监听 `0.0.0.0`，主机端口只映射到本机。以下命令是教学步骤，不代表已在此环境执行。

## 跟做

在博客项目根目录创建 `.dockerignore`：

```text
node_modules
.git
.env
.env.*
!.env.example
dist
coverage
var
```

创建 `Dockerfile`。构建阶段生成 Prisma Client 并编译 Nest；独立的 `migrate` 阶段保留锁文件安装的 `prisma@6.19.0` CLI，只负责迁移；`production-deps` 才裁剪开发依赖，最后的 `runtime` 不含 CLI。不要在运行镜像里用 `npx prisma` 临时下载版本。若 schema 路径或启动入口不同，沿用实际位置修改，不把 `.env` 复制进镜像。

```dockerfile
FROM node:22-bookworm-slim AS base
RUN apt-get update && apt-get install -y --no-install-recommends openssl \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app

FROM base AS build
COPY package*.json ./
RUN npm ci
COPY . .
RUN ./node_modules/.bin/prisma generate && npm run build

FROM build AS migrate
ENV NODE_ENV=production
USER node
CMD ["./node_modules/.bin/prisma", "migrate", "deploy"]

FROM build AS production-deps
RUN npm prune --omit=dev

FROM base AS runtime
ENV NODE_ENV=production
COPY --from=production-deps --chown=node:node /app/package*.json ./
COPY --from=production-deps --chown=node:node /app/node_modules ./node_modules
COPY --from=build --chown=node:node /app/dist ./dist
COPY --from=build --chown=node:node /app/prisma ./prisma
USER node
EXPOSE 3000
CMD ["node", "dist/main.js"]
```

先确认 Nest 的 `main.ts` 监听 `0.0.0.0`。在项目根目录运行 `docker build --target runtime -t blog-api:local .`；若机器未装 Docker Desktop 或 Linux Docker Engine，先完成安装，不要伪称运行成功。运行时由环境传入 `DATABASE_URL`、`JWT_SECRET`。容器里的 `127.0.0.1` 是容器自身：若沿用宿主机数据库，Docker Desktop 可将本地专用环境文件的数据库主机改为 `host.docker.internal`，并检查数据库监听/访问规则；Linux Engine 运行命令需额外加 `--add-host=host.docker.internal:host-gateway`。不要为了连通而把数据库暴露到公网。更直接的完整实验使用第 42 天 Compose。第 41 天暂不导入依赖 Redis 的 `QueueModule`，除非已提供容器可访问的 Redis。`--env-file` 只读取已忽略的文件，不要把值贴入命令历史或截图。

```bash
docker run --rm --name blog-api -p 127.0.0.1:3000:3000 --env-file .env blog-api:local
```

## 练习

检查构建上下文是否排除了 `.env`、`node_modules` 和上传目录。启动容器后访问 `/health/live`（第 45 天创建的健康端点；`/health` 的由来见第 07 天原生示例），再用 `docker stop blog-api` 停止（若使用 `--rm`，停止后容器自动移除）。

## 参考答案与验收

预期镜像构建成功，`docker image ls blog-api` 可见 `local` 标签，`GET http://127.0.0.1:3000/health/live` 返回 200。检查镜像（`docker image inspect blog-api:local`）的 Config.Env，不应包含实际密钥；运行容器的 Config.Env 会包含通过环境注入的值，不要输出或分享它。确认进程用户不是 root。数据库连接无效时应启动失败或 readiness 不健康，而不是报告已连接。没有 Docker 环境时将构建和运行标为“未验证”，完成 Dockerfile 与忽略规则检查即可。

## 原版对照阅读

原版 Day41 展开更细，把 Dockerfile 逐行讲透，本讲义给的是一份可用镜像。补四点原理：

- **镜像 ≠ 容器**：镜像是只读的分层文件系统模板，容器是镜像的运行实例（可写层）。`docker build` 产出镜像，`docker run` 才产生容器。每一条 Dockerfile 指令生成一层，层数影响体积与缓存。
- **多阶段构建**：原版镜像是 `deps` 装全部依赖、`build` 编译 TypeScript、`runner` 只拷产物三段；本文 Dockerfile 是 `base/build/migrate/production-deps/runtime` 五阶段（`migrate` 段供第 42 天的一次性迁移服务复用，`production-deps` 单独装生产依赖）。共同点是最终镜像不含 devDependencies、源码和构建工具，体积和攻击面都大幅缩小；阶段名按本文 Dockerfile 对照，不要照抄原版。
- **缓存友好的指令顺序**：把 `COPY package*.json` + `npm ci` 放在 `COPY .` 之前。源码频繁变动时，依赖层因内容没变而命中缓存，不必每次重装几百个包。
- **原版 alpine 镜像的坑（本文已规避）**：原版用 alpine（musl libc），Prisma 查询引擎默认按 glibc 编译，会出现 `libssl` / `openssl` 加载失败，其解法是 schema 里设 `binaryTargets = ["native", "linux-musl-openssl-3.0.x"]`。但本文用 `node:22-bookworm-slim`（glibc），不要照着给 Debian 镜像加 musl 引擎目标，也不要凭空装 `tini`。无论哪种镜像，运行阶段都应用非 root 用户，并让 Node 进程作为 PID 1 正确接收 `SIGTERM`（或用 `dumb-init` 之类转发信号）才能优雅关闭。

## AI 搭档

提示词「审阅这份脱敏 Dockerfile：检查运行用户、构建阶段、秘密是否进入镜像、端口绑定与启动命令，并列出本地验收命令。」人工检查镜像环境和健康端点。不要发送 `.env`、镜像仓库凭据、数据库 URL 或令牌。

# 第 42 天：用 Compose 启动 API 与 PostgreSQL

原课：<https://xiguadev.com/node-60days/day-42>

## 今日先学

Compose 用一个 YAML 描述多个本地服务。本课编排 Nest API 与 PostgreSQL 16，数据库只对 Compose 网络可见，数据放具名卷。健康检查表示数据库可接受连接，不代表迁移已完成。Compose 的依赖顺序不能代替应用重试，也不等于生产备份。若还没有 Docker，先阅读配置，在已具备 Docker 的 Linux、WSL2 或 Docker Desktop 环境完成练习。

## 跟做

在项目根目录创建 `compose.yaml`。数据库密码通过 `.env` 提供，`.env` 已在 `.gitignore` 和 `.dockerignore` 中排除。下例为本地学习密码，不能用于公网服务或生产。确认 API 镜像使用昨天的 Dockerfile，应用读取同名 `DATABASE_URL`。

```yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_USER: blog
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:?set in .env}
      POSTGRES_DB: blog
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U blog -d blog"]
      interval: 5s
      timeout: 3s
      retries: 10
  migrate:
    build:
      context: .
      target: migrate
    environment:
      DATABASE_URL: postgresql://blog:${POSTGRES_PASSWORD}@db:5432/blog?schema=public
    depends_on:
      db:
        condition: service_healthy
  api:
    build:
      context: .
      target: runtime
    environment:
      NODE_ENV: production
      DATABASE_URL: postgresql://blog:${POSTGRES_PASSWORD}@db:5432/blog?schema=public
      JWT_SECRET: ${JWT_SECRET:?set in .env}
      CACHE_ENABLED: "false"
    ports:
      - "127.0.0.1:3000:3000"
    depends_on:
      db:
        condition: service_healthy
volumes:
  pgdata:
```

本地 `.env` 至少包含 `POSTGRES_PASSWORD` 和第 32 天生成的 `JWT_SECRET`。Docker Compose 的变量插值并不保证所有特殊字符在 URL 中自动转义；本练习使用随机字母数字密码，真实部署用秘密管理和正确 URL 编码。此两服务实验不导入 `QueueModule`，缓存关闭，重建端点预期 503。按顺序执行，迁移失败就先排错，不启动 API：

```bash
docker compose config --quiet
docker compose build migrate api
docker compose up -d db
docker compose run --rm migrate
docker compose up -d api
```

`migrate` 的默认命令直接执行锁文件安装的 `./node_modules/.bin/prisma migrate deploy`，不会下载 CLI。`run` 会等待健康的数据库依赖；它只迁移，不启动 Nest，也不需要 JWT 密钥。之后 schema 有新迁移时先重复迁移步骤再更新 API。不要分享展开了密码的 `docker compose config` 输出。

## 练习

查看 `docker compose ps` 和 `docker compose logs api`，请求 `/health/live`（第 45 天还会提供 `/health/ready`），创建一篇测试 `Post`，执行 `docker compose down` 后再启动并检查记录仍在。最后执行 `docker compose down -v` 清理练习卷；该命令会删除数据库数据，只在确认数据可丢弃时运行。

## 参考答案与验收

`db` 应显示 healthy，API 映射仅绑定 `127.0.0.1`；`/health/live` 返回 200，创建文章返回 201。`down` 后 `pgdata` 卷保留，重启后记录仍在。`down -v` 后数据清空是预期行为。验收结束确认无真实数据，且 `.env` 未进入版本库。Compose 仅用于本机练习，不作为公网生产部署方案。

## 原版对照阅读

原版 Day42 展开更细，讲 Compose，本讲义给了一份能起来的配置。补四点：

- **`depends_on` 只管启动顺序，不管"准备好"**：单纯 `depends_on: [db]` 只保证 db 容器先创建，不代表 PostgreSQL 已能接受连接。要用 `condition: service_healthy` 配合 healthcheck，或让应用自己重试连接。
- **迁移单独作为一个 job**：不要让每个 API 实例启动时都跑 `migrate deploy`——多实例并发迁移会互相冲突。本文把 `migrate` 写成一次性服务，但 `api.depends_on` 只有 `db: service_healthy`，**没有** `migrate: service_completed_successfully`；顺序靠下面「`up -d db` → `run --rm migrate` → `up -d api`」的手动分步保证，迁移失败就停下排错、不启动 API。若改成 Compose 自动保证顺序，需补该依赖条件并给 `migrate` 设 `restart: "no"`，同时删掉手动 `run` 那一步，避免迁移跑两次。
- **存活 vs 就绪**：liveness（存活）回答"要不要重启我"，进程死锁时失败；readiness（就绪）回答"能不能给我导流"，依赖未就绪时失败。编排器据此分别决定重启和流量切换。健康检查要探真实依赖（DB 必查），但别让 Redis 抖动连带拖垮整个 API。
- **容器里的 `localhost` 是容器自己**：连同 compose 的其他服务要用服务名（如 `db:5432`），不是 `localhost`。数据要放具名卷，否则 `docker compose down` 后容器被删、数据一起丢失。

## AI 搭档

提示词「解释这份脱敏 Compose 中端口绑定、具名卷、数据库健康检查和迁移命令的作用，并指出不可提交的字段。」人工确认数据持久化与销毁命令影响。不要把 `docker compose config` 中展开的密码或 JWT 值传给 AI。

# 第 43 天：为博客建立 CI/CD 检查流水线

原课：<https://xiguadev.com/node-60days/day-43>

## 今日先学

CI 在每次代码变更时自动安装依赖、生成 Prisma Client、运行测试并构建；CD 才负责交付或部署。先让 CI 只检查，不授予云端部署权限。锁文件保证依赖可重复安装。数据库测试使用短期测试服务和隔离数据库；CI 不能依赖开发者电脑上的 `.env`。秘密只在受保护环境配置，普通拉取请求不应读取部署密钥。

## 跟做

以 GitHub Actions 为例，在 `.github/workflows/ci.yml` 建立工作流。若博客使用不同脚本名称，按 `package.json` 修改。测试库用专属非生产凭据，并且不含真实用户内容。此工作流不上传镜像、不部署、不提交远程仓库。

```yaml
name: ci
on:
  pull_request:
  push:
    branches: [main]
permissions:
  contents: read
jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_USER: test
          POSTGRES_PASSWORD: test-only
          POSTGRES_DB: blog_test
        ports: ["5432:5432"]
        options: >-
          --health-cmd "pg_isready -U test -d blog_test"
          --health-interval 5s --health-timeout 3s --health-retries 10
    env:
      DATABASE_URL: postgresql://test:test-only@localhost:5432/blog_test?schema=public
      NODE_ENV: test
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
      - name: Generate ephemeral test JWT secret
        run: node -e "const fs=require('node:fs'); const secret=require('node:crypto').randomBytes(32).toString('base64url'); fs.appendFileSync(process.env.GITHUB_ENV, 'JWT_SECRET='+secret+'\n')"
      - run: npm ci
      - run: ./node_modules/.bin/prisma generate
      - run: ./node_modules/.bin/prisma migrate deploy
      - run: npm test -- --runInBand
      - run: npm run build
```

确认测试脚本接受参数；若不是 Jest，删掉不适用的参数并使用项目真实测试命令。CI 每次生成独立的 32 字节随机密钥并写入 `GITHUB_ENV`，后续步骤自动读取，不输出密钥；同时满足第 32 天的 base64url 解码长度和第 40 天的字符串长度校验，不用于部署。没有 Redis 的 CI 不接入 `QueueModule`，队列单测使用 mock。把工作流提交到本地分支后，在 Git 平台创建 PR 时观察状态；本任务不执行远程提交。

## 练习

添加一项授权测试：普通用户请求删除另一用户文章应为 403，数据库记录仍存在。打开 CI 日志确认对应测试被运行；再检查工作流权限仅有 `contents: read`，没有云部署密钥。

## 参考答案与验收

流水线的可观察证据：五个步骤（依赖安装 / `prisma generate` / 迁移 / 测试 / 构建）在 Actions 页各有绿色勾号，Tests 步骤输出 `1 passed` 或实际用例数；把该授权测试改成必然失败的断言后重新推送，对应步骤变红、PR 显示 "Some checks were not successful" 且无法合并，恢复断言后转绿。工作流顶部可见 `permissions: contents: read`，没有云部署密钥相关环境变量。测试流程不得执行生产数据库迁移。若仓库尚未接入 CI，静态检查 YAML 与本地运行同样脚本只能标为“本地验证”，不能声称流水线已通过。

## 原版对照阅读

原版 Day43 展开更细，讲 CI/CD，本讲义只给了一份 workflow。补四点：

- **CI 与 CD 是两件事**：CI（持续集成）是每次 push 都跑的"闸门"——类型检查、单测、构建；CD（持续交付/部署）是通过闸门后把产物推到仓库或上线。把两者放一个 job 会让"测试失败"仍可能发布。
- **service container**：CI 里的 PostgreSQL/Redis 用 `services:` 声明，与本机 compose 同构，runner 通过服务名访问。没有它，集成测试会因为连不上数据库而失败。
- **迁移必须在测试之前**：测试库也是空库，先 `prisma migrate deploy` 建好表，再跑测试，呼应第 42 天的顺序原则。
- **类型检查由构建命令承担**：本文 workflow 的五步里没有单独的 `lint`/`typecheck` 步骤，是 `npm run build`（`tsc --noEmit && vite build`，Nest 侧为 `nest build`）在做全量静态类型检查——类型不过就构建失败。`tsc --noEmit` 只检查不产出文件；若另配 ESLint，它管的是代码风格与可疑写法，与类型检查不是一回事。第三方 action 在生产流水线里建议锁定到具体 commit SHA（本文为可读性用 `@v4` 这类大版本 tag），避免上游被篡改后影响构建。

## AI 搭档

提示词「审阅这段脱敏 CI 配置，找出权限过宽、测试/生产环境混用和未锁定步骤，并提出检查方法。」人工核对权限、服务地址和脚本输出，不接受 AI 凭空报告的通过结果。不要发送真实 Actions Secret、私有仓库令牌或 CI 日志中的凭据。

# 第 44 天：规划一次手动云端发布与回滚

原课：<https://xiguadev.com/node-60days/day-44>

## 今日先学

今天学习发布流程，不登录真实云账号、不填账单、不连生产资源、不推送镜像或远程提交；**本机的镜像构建、Compose 配置校验与生产发布演练照常做**。发布前选符合地域、合规和预算要求的托管平台，明确 API 运行环境、托管 PostgreSQL、密钥管理、对象存储和日志保留策略。云资源可能按实例时长、数据库容量、出站流量、磁盘快照和日志计费；免费额度会变化，资源忘记关闭也可能产生费用。开始前阅读当前价格与限额，设置预算告警，避免承诺“免费”。

## 跟做

1. 选 Node 22 运行环境和托管 PostgreSQL 16；确认 Prisma 6.19.x 与生产数据库兼容。生产数据库禁止使用 Compose 的本地卷。
2. 在平台秘密管理处设置 `DATABASE_URL`、JWT 签名密钥、可选 `REDIS_URL` 和对象存储凭据。每个环境独立生成秘密，限制读取权限；绝不写入 Git、镜像、日志或讲义。
3. 由 CI 构建不可变镜像并以提交 SHA 标记。部署前备份数据库，检查迁移是否向前兼容；新增列先可空或有安全默认值，应用切换后再做后续清理。
4. 用手动审批将镜像部署到 staging，运行迁移、健康检查和小范围验收，再安排生产窗口。没有自动化验证和回滚演练就不要扩大流量。

每次发布留存版本号、迁移编号、操作者和时间，不记录密钥。手动回滚步骤应事先写好：停止扩大流量，将应用切回上一个兼容镜像；检查 `/health/ready` 和关键 API；通知相关人员。数据库迁移不一定可逆，不能假定切回旧镜像即可恢复数据。破坏性 schema 变更需备份、兼容窗口和独立恢复方案。完成后确认预算、告警和资源所有者。

## 练习

为虚构服务填写发布卡：版本 SHA、变更摘要、数据库备份时间、迁移编号、健康检查 URL、回滚镜像、负责人、成本上限和回滚触发条件。模拟“新镜像 readiness 连续失败”，写出停止流量、切回兼容镜像、复查数据和通知流程，不实际操作云环境。**本机可演练的部分照做**：用第 41/42 天的 Dockerfile 与 Compose 重新构建一次镜像，用 `docker compose config` 校验配置、`docker image ls` 确认镜像存在，再用第 55 天的生产 Compose 在本机完整起一次栈、观察迁移 job 先于 API 完成，最后 `docker compose down` 清理。这些都在本机完成，不产生云端费用。

## 参考答案与验收

发布卡字段齐全；回滚条件可观察，例如 readiness 连续失败或关键 API 错误率超过团队阈值；回退版本与当前迁移兼容。本机演练要有可观察证据：镜像构建成功、`docker compose config` 无报错、迁移 job 先于 API 就绪、`docker compose down` 后容器清除。确认没有云端访问、远程发布或远程提交：本任务只在 localhost 执行。费用说明应指出实例、数据库、存储、网络和日志均可能收费，并要求发布前查平台最新价格、设预算告警和删除闲置资源。

## 原版对照阅读

原版 Day44 是"云部署实战"，逐行讲 `fly.toml` / `railway.json`，本讲义出于费用与账号安全只做纸面清单。补四点，让清单背后的判断可迁移到任何平台：

- **为什么这套镜像不上 Vercel**：Vercel 面向 Serverless 函数，有执行时长上限、无常驻进程，跑不了 WebSocket 网关和 BullMQ worker。需要常驻服务 + 后台 worker 的项目更适合容器平台（Fly.io / Railway / Cloud Run）。
- **托管 PostgreSQL 与 PgBouncer**：Supabase / Neon 等托管库常内置 PgBouncer 做连接复用。注意 Prisma 在事务模式下需要 `?pgbouncer=true`，且准备好的语句可能不兼容——按平台文档设置连接串参数。
- **迁移在生产谁跑**：不能在 Web 启动时跑迁移（多实例并发冲突），应在发布流水线里作为独立、一次性步骤执行，且遵循"先兼容后清理"——先加可空列、部署新代码、再删旧列，保证新旧版本能共存，才谈得上回滚。
- **健康检查映射**：`/health/live` 给平台的重启探针，只查进程本身；`/health/ready` 给负载均衡的导流探针，但**只查必要依赖（PostgreSQL）**——第 45 天明确 Redis 是可选缓存，它抖动不应让 readiness 失败、把实例摘出导流。平台自动停机时别把 BullMQ worker 一起饿死——它要处理完在途作业再退出。

## AI 搭档

提示词「用虚构服务信息审阅这张手动发布卡：指出遗漏的审批、备份、兼容迁移、健康验收、成本提醒和回滚步骤，不要访问云端。」人工验证每一步有责任人和停止条件。只提供虚构 SHA 与成本，不提供账户 ID、秘密、真实域名或客户数据。

# 第 45 天：为博客添加结构化日志、观测与健康检查

原课：<https://xiguadev.com/node-60days/day-45>

## 今日先学

日志回答发生了什么，指标呈现一段时间的数量和延迟，追踪把一次请求关联到多项服务。结构化 JSON 日志更便于检索，但不得记录密码、Cookie、JWT、授权码、数据库 URL、上传内容或完整个人资料。健康检查至少区分 liveness（进程是否应重启）与 readiness（是否可接流量）。健康响应只公开依赖状态，不暴露连接串或异常堆栈。监控告警须有阈值、负责人和处理流程。

## 跟做

Nest 内置 Logger 可先用于结构化字段，生产可接成熟日志库与 OpenTelemetry SDK，并统一导出到受控平台。创建 `src/health/health.controller.ts`，由服务探测 PostgreSQL；`/health/live` 不检查外部依赖，`/health/ready` 才检查数据库，Redis 是可选缓存时不可用不应使 readiness 失败。健康端点不返回秘密或原始错误。

```ts
import { Controller, Get, ServiceUnavailableException } from '@nestjs/common';
import { PrismaService } from '../prisma/prisma.service';

@Controller('health')
export class HealthController {
  constructor(private readonly prisma: PrismaService) {}

  @Get('live')
  live() { return { status: 'ok' }; }

  @Get('ready')
  async ready() {
    try {
      await this.prisma.$queryRaw`SELECT 1`;
      return { status: 'ok', dependencies: { database: 'ok' } };
    } catch {
      throw new ServiceUnavailableException({
        status: 'not_ready', dependencies: { database: 'unavailable' },
      });
    }
  }
}
```

将控制器加入 `HealthModule`，让 `AppModule` 导入。添加全局拦截器或既有 HTTP 日志中间件，为请求生成随机 request ID，并只记录 method、路由模板、statusCode、durationMs、requestId。错误日志记录错误类别和 requestId；不要把 `req.headers`、完整 URL 查询参数、请求体或异常中的配置对象整体输出。采集 p50/p95 延迟、5xx 比率、进程内存、队列积压和数据库连接池使用率，设置合理保留期限与访问权限。

下面是一份可直接放进 `src/common/logging.interceptor.ts` 的最小实现：用 `requestId` 贯穿一次请求，只输出白名单字段。路由模板取 `req.route?.path`（如 `/posts/:id`），而不是完整 URL，避免把查询串里的令牌写进日志。

```ts
// src/common/logging.interceptor.ts
import {
  CallHandler, ExecutionContext, Injectable, NestInterceptor,
} from '@nestjs/common';
import { randomUUID } from 'node:crypto';
import { Observable, tap } from 'rxjs';

@Injectable()
export class LoggingInterceptor implements NestInterceptor {
  intercept(ctx: ExecutionContext, next: CallHandler): Observable<unknown> {
    const req = ctx.switchToHttp().getRequest();
    const requestId = randomUUID();
    const started = Date.now();
    req.requestId = requestId; // 供异常过滤器复用同一个 ID
    return next.handle().pipe(
      tap({
        next: () => this.write(req, requestId, Date.now() - started),
        error: (error) => {
          // 只记录错误类别与 requestId，不输出 error 对象（可能含配置/凭据）
          this.write(req, requestId, Date.now() - started, error?.constructor?.name ?? 'Error');
        },
      }),
    );
  }

  private write(req: any, requestId: string, durationMs: number, error?: string) {
    // eslint-disable-next-line no-console -- 教学最小实现；生产换成 Pino 等结构化日志
    console.log(JSON.stringify({
      requestId,
      method: req.method,
      route: req.route?.path ?? req.url.split('?')[0],
      statusCode: req.res?.statusCode ?? (error ? 500 : 200),
      durationMs,
      ...(error ? { error } : {}),
    }));
  }
}
```

在 `src/main.ts` 用 `app.useGlobalInterceptors(new LoggingInterceptor())` 注册。核对日志行：`requestId` 每次请求都不同，同一请求内所有日志（含错误）带同一个值；`route` 是模板而非真实 ID；整行不含 `authorization`、`cookie`、`password` 或查询串。生产环境把 `console.log` 换成 Pino 的 `logger.info()`，并让它读取 `req.requestId`（配合 AsyncLocalStorage 可免手动传参）。

## 练习

本机数据库正常时访问 `/health/live` 和 `/health/ready`；在测试环境用 mock 让 Prisma 探测抛错，再请求 readiness。检查一次普通请求产生的日志字段，并用虚构 Cookie 和 Bearer 值确认日志中没有凭据。不要通过破坏共享数据库来模拟故障。

## 参考答案与验收

两项健康检查正常时均为 200；数据库 mock 失败时 `/health/ready` 返回 503 且只显示 `database: unavailable`，`/health/live` 仍为 200。日志包含 requestId、路由模板、状态码和耗时，不含原始请求头、查询串中的授权参数、用户密码或上传路径。测试应断言日志脱敏和 ready 失败分支。未连接真实指标或追踪后端时，记为“代码已准备，外部观测未验证”，不得声称已建立生产告警。

## 原版对照阅读

原版 Day45 展开更细，讲可观测性，本讲义只给了 HealthController。补四点：

- **日志是给机器和给人两类读者读的**：结构化日志（每行一个 JSON 对象，含 `time`/`level`/`msg`/`requestId` 等字段）便于聚合检索；散文式日志只有人读得懂、难以过滤。Pino 是 Node 的事实标准，因为序列化开销低。
- **`requestId` 串联一次请求的所有日志**：在入口中间件生成（或从入站 `X-Request-Id` 继承），用 AsyncLocalStorage 贯穿整个异步调用链，每条日志自动带上它。出问题时按 requestId 一搜，就能还原完整链路。
- **脱敏是红线**：`authorization`、`cookie`、密码、令牌、身份证等字段永远不进日志，打印时用字段白名单而不是黑名单，避免新增字段悄悄泄露。
- **可观测性三件套**：logs（发生了什么）、metrics（多久、多少、成功率）、traces（跨服务调用了什么）。健康检查之外，配合 p95 延迟和错误率才能判断"系统是否健康"。

## AI 搭档

提示词「审阅以下删除所有真实值的结构化日志样例，标出可能的秘密字段，并为健康检查给出 liveness、readiness 的状态码验收表。」人工逐字段确认脱敏和依赖边界。只分享虚构请求 ID、路由模板、状态码和延迟，不分享真实日志、令牌、IP 或用户标识。


# 第 46 天：把协作任务板写成需求和接口契约

原课：<https://xiguadev.com/node-60days/day-46>

## 今日先学

「协作任务板」是一个多租户 SaaS。租户就是团队，同一个账号可以属于多个团队。最小故事是这样的：小林注册后创建甲队和「上线准备」项目，邀请已注册的小周加入甲队。两人可以新建任务、移动状态，乙队成员只能操作自己的团队。第一版只做注册登录、团队成员、项目和任务、三列看板、站内通知与状态统计。把计费、拖拽排序、附件和邮件邀请留在范围之外，先把一条操作链路跑通。

## 跟做

在练习项目 `task-board/README.md` 写下数据关系。`User` 是账号；`Membership` 用 `(teamId,userId)` 记录成员身份和角色；`Team` 有多个 `Project`；`Project` 有多个 `Task`。对外的任务形状固定为 `{id:string,title:string,status:'todo'|'doing'|'done',teamId:string,projectId:string}`。服务层根据 URL 确定目标团队和项目，从已验证的令牌得到用户 ID，然后查成员关系。请求体只收本次可改的字段。

把下表抄进 README，作为后续接口实验的预期。`/api` 是统一前缀，`T`、`P`、`K` 代表实际的团队、项目和任务 ID。

| 请求 | 预期 |
| --- | --- |
| `POST /api/auth/login`，输入邮箱与密码 | `200 {accessToken}` |
| `POST /api/teams/T/projects/P/tasks`，输入 `{"title":"写发布说明"}` | `201`，任务状态为 `todo` |
| `PATCH /api/teams/T/projects/P/tasks/K`，输入 `{"status":"doing"}` | `200`，返回更新后的任务 |
| `GET /api/teams/T/projects/P/tasks?status=doing` | `200 {items,nextOffset}` |

用箭头画出数据流。浏览器页面经 HTTP 找 NestJS 11，控制器解析输入，服务核对权限和业务规则，Prisma 6.19.x 读写 PostgreSQL 16。PG 保存正式数据，Redis 和 BullMQ 后续处理通知作业。选受支持的 Node LTS（22 / 24 / 26，新项目优先 26）。前端采用 React + Vite + TypeScript。HTML 定义页面结构，CSS 控制样式，JSX 是在组件里描述结构的语法，放进 `.tsx` 文件后由 Vite 编译。明天会打开本机页面并验证三者如何连起来。

## 练习

在 README 写五条验收句，分别覆盖同队读取、没有登录、其他团队成员来读、当前项目找不到记录、普通成员管理成员。给每条写清调用人和结果。

## 参考答案与验收

小周属于甲队，读甲队项目得 `200`。未带有效令牌得 `401`；乙队成员访问甲队得 `403`；甲队成员访问本队范围内不存在的项目或任务得 `404`；甲队普通成员添加成员得 `403`。普通成员与所有者均可读写本团队项目和任务。检查每条都写了触发条件和可观察结果，后面直接用它们做测试。

## AI 搭档

先自己写五条，再发脱敏契约。「请逐条问我是谁在何处做什么，并指出哪个预期状态码缺了前置条件。先等我解释，再点评，别替我重写。输入只含虚构团队和邮箱，绝不提供秘密或真实客户数据。」

# 第 47 天：启动 Nest、数据库和 React 页面

原课：<https://xiguadev.com/node-60days/day-47>

## 今日先学

今天打通两条独立链路。后端先确认 Nest 可以接请求，再用 Prisma 查询 PG；浏览器先渲染一个组件，再让 Vite 转发 `/api` 请求。Compose 只使用已有的容器运行环境，或者沿用前面阶段提供的 PG16 实验容器并替换连接串。以下都是本机命令，从自己的 `task-board` 目录开始。

## 跟做

在容器方案下，将下面内容写入项目根目录的 `compose.yaml`。示例密码只用于这台电脑，当已有实验容器时复用该容器即可。端口已占用时改左侧端口和连接串，容器里的端口保持不变。

```yaml
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_USER: board
      POSTGRES_PASSWORD: board_dev_only
      POSTGRES_DB: board
    ports:
      - '127.0.0.1:5432:5432'
    volumes:
      - board-data:/var/lib/postgresql/data
volumes:
  board-data:
```

```bash
node -v
npx --yes --package @nestjs/cli@11 nest new api --package-manager npm --skip-git
npm create vite@6 -- web --template react-ts
# 如选了上面的 Compose 方案，在根目录运行
 docker compose up -d postgres
cd api
npm install @prisma/client@6.19.0 @nestjs/config@4 class-validator class-transformer
npm install --save-dev prisma@6.19.0
```

在 `api/.env` 写 `DATABASE_URL=postgresql://board:board_dev_only@127.0.0.1:5432/board?schema=public`，确认 `api/.gitignore` 忽略 `.env`。提交契约时可保留仅含变量名的 `.env.example`。先创建 `api/prisma/schema.prisma`，今天只生成客户端，明天加入表并运行迁移。CLI 和客户端使用同一 6.19 补丁号，后面保持锁文件一致；若脚手架询问是否直接安装前端依赖，可先跳过。前端脚手架固定用 Vite 6（`npm create vite@6`），与配套包 `day54-web/package.json` 锁定的 `vite ^6.4.0`、`@vitejs/plugin-react ^4.7`、单份 `tsconfig.json` 与 `tsc --noEmit && vite build` 一致；直接用更新版本的 `create vite` 会得到 `tsc -b` 与不同的 tsconfig 拆分，覆盖源码前请先对齐构建脚本。

```prisma
// api/prisma/schema.prisma，后续 model 都追加到这个文件
 generator client {
   provider = "prisma-client-js"
 }
 datasource db {
   provider = "postgresql"
   url      = env("DATABASE_URL")
 }
```

```ts
// api/src/prisma.service.ts
import { Injectable, OnModuleDestroy, OnModuleInit } from '@nestjs/common';
import { PrismaClient } from '@prisma/client';

@Injectable()
export class PrismaService extends PrismaClient implements OnModuleInit, OnModuleDestroy {
  async onModuleInit() { await this.$connect(); }
  async onModuleDestroy() { await this.$disconnect(); }
}
```

在 `api/src/app.module.ts` 的 `imports` 加 `ConfigModule.forRoot({isGlobal:true})`，`providers` 加 `PrismaService`，导入对应类。在生成的 `AppController` 构造器中注入 `private readonly db: PrismaService`，保留原有 `AppService` 依赖，加入这个方法。鉴于脚手架的控制器单测还没有配置数据库，本课以 HTTP 验收，第 56 天会改造单测。

```ts
// api/src/app.controller.ts 的 AppController 类内，沿用已有 Get 导入
@Get('health')
async health() {
  await this.db.$queryRaw`SELECT 1`;
  return { ok: true };
}
```

在 `api/src/main.ts`，`listen` 前加入 `app.setGlobalPrefix('api')`、`app.enableShutdownHooks()` 和 `app.useGlobalPipes(new ValidationPipe({whitelist:true,forbidNonWhitelisted:true,transform:true}))`，从 `@nestjs/common` 导入 `ValidationPipe`。本机用 `await app.listen(Number(process.env.PORT ?? 3000), process.env.HOST ?? '127.0.0.1')`。在 `api` 执行 `npx prisma generate`、`npm run start:dev`，另开终端请求 `curl -i http://127.0.0.1:3000/api/health`，应见 `200` 与 `{"ok":true}`。

将下面组件放进 `web/src/App.tsx`，保留生成的 `main.tsx`。浏览器从 `index.html` 的根节点启动，`main.tsx` 把 `App` 挂上去，`{title}` 把变量显示在 HTML 标题里。在 `web/vite.config.ts` 的 `defineConfig` 对象内保留 `plugins`，添加 `server: { host:'127.0.0.1', proxy: { '/api':'http://127.0.0.1:3000', '/socket.io': { target:'http://127.0.0.1:3000', ws:true } } }`。关键在第 51/54 天的实时链路：网关的 `namespace:'/board'` 是命名空间，Socket.IO 的 HTTP 握手端点固定是 `/socket.io/`，因此代理必须覆盖 `/socket.io`；只代理 `/api` 或只代理 `/board`，握手请求都到不了 Nest。客户端 `io('/board', { path:'/socket.io', ... })` 的第一个参数是 namespace，第二个参数里的 `path` 才是握手路径，两者不要混为一谈。

```tsx
// web/src/App.tsx
import './App.css';

export default function App() {
  const title = '协作任务板';
  return <main className="board"><h1>{title}</h1><p>项目启动成功</p></main>;
}
```

### 原课技术栈补齐：Next.js App Router 与 tRPC

原课第 47 天采用 Next.js + tRPC。本讲义的团队项目先沿用前面熟悉的 Nest REST + Vite，减少同时更换后端和前端的负担；但 Next.js 与 tRPC 是本日的必做对照实验，不把它们当作已经学会或直接略过。

Next.js 在 React 上增加按文件夹组织页面、服务器渲染与服务端路由。`app/page.tsx` 对应首页，`app/api/.../route.ts` 处理 HTTP；默认组件可在服务器执行，使用 React 状态的组件要加 `'use client'`。tRPC 用同一个 TypeScript Router 类型连接客户端与服务器；它提供编译期调用提示，外部 JSON 仍需运行时校验。不要把已有 Prisma Client 放到 `'use client'` 组件中；数据库只在服务端访问。

在与 `task-board` 平级的**新目录**做实验，不要覆盖 Nest 工程。React 先用第 47 天主线完成第一个页面，下面只加一种接口方式：

```bash
npx create-next-app@16 trpc-lab --ts --eslint --app --no-src-dir --no-tailwind --use-npm
cd trpc-lab
npm install @trpc/server@11 @trpc/client@11 zod@3
```

交互中不启用额外的 React Compiler，并保留默认路径别名。若端口 3000 正被 Nest 占用，这个实验用 3001。新建以下文件。tRPC 的 `procedure` 是有类型的操作；`query` 只读，`mutation` 修改数据；Zod 校验客户端输入。

```ts
// server/router.ts
import { initTRPC } from '@trpc/server';
import { z } from 'zod';

const t = initTRPC.create();
export const appRouter = t.router({
  hello: t.procedure.input(z.object({ name: z.string().trim().min(1).max(40) }))
    .query(({ input }) => ({ message: `你好，${input.name}` })),
});
export type AppRouter = typeof appRouter;
```

```ts
// app/api/trpc/[trpc]/route.ts
import { fetchRequestHandler } from '@trpc/server/adapters/fetch';
import { appRouter } from '../../../../server/router';

function handler(req: Request) {
  return fetchRequestHandler({ endpoint: '/api/trpc', req, router: appRouter, createContext: () => ({}) });
}
export { handler as GET, handler as POST };
```

```tsx
// app/page.tsx，完整替换
'use client';
import { useState } from 'react';
import { createTRPCClient, httpBatchLink } from '@trpc/client';
import type { AppRouter } from '../server/router';

const client = createTRPCClient<AppRouter>({
  links: [httpBatchLink({ url: '/api/trpc' })],
});
export default function Page() {
  const [message, setMessage] = useState('尚未请求');
  async function load() {
    try { setMessage((await client.hello.query({ name: '学习者' })).message); }
    catch { setMessage('请求失败，请检查本机终端'); }
  }
  return <main><h1>tRPC 对照实验</h1><button onClick={load}>发送请求</button><p>{message}</p></main>;
}
```

运行 `npm run dev -- --port 3001`，打开终端给出的本机地址，点击后看到「你好，学习者」。运行 `npm run build` 做生产编译。把调用中的 `name` 改成数字，TypeScript 应报错；恢复后，将空白字符串交给服务器，Zod 应拒绝。由此区分编译期契约与运行时校验。

这里没有数据库、真实用户和权限。接入数据库时，`createContext()` 应从请求验证会话并提供服务端 Prisma 实例，受保护的 procedure 中再检查团队成员关系；不要信任客户端传来的 `userId`。tRPC 跨进程调用并不替代认证或授权。第 54 天会给这个实验接 React Query；主线任务 API 继续使用 Nest REST，两个实验的数据库、端口和认证保持分离。


## 练习

清掉 `web/src/index.css` 的模板样式，为 `web/src/App.css` 写一条 `.board` 规则，启动页面，并通过 Vite 的地址请求后端健康端点。

## 参考答案与验收

CSS 可以写 `.board { max-width: 60rem; margin: 2rem auto; padding: 1rem; }`。在 `web` 执行 `npm install`、`npm run dev`，打开终端实际打印的地址，默认 `http://127.0.0.1:5173`。改 JSX 的标题后页面会刷新显示。对该地址追加 `/api/health`，应得到同样的 JSON。PG 连不上时先核对容器状态与连接串。页面可打开但代理报错时，检查 API 是否仍在监听 3000。

## AI 搭档

自己定位一遍再问。「我的页面能显示，Vite 转发健康检查时失败。请根据我贴的终端摘要，分别问我如何确认浏览器、代理、API 和数据库，再核对我的推断。只给下一条本机检查建议。我会删掉连接串、密码、令牌和真实客户数据。」

# 第 48 天：登录、建团队和验证成员身份

原课：<https://xiguadev.com/node-60days/day-48>

## 今日先学

认证回答「你是谁」，授权回答「你在这个团队能做什么」。短期 JWT 只保存 `sub`，也就是账号 ID。每次进入团队路径时再查成员表，因此权限按当前数据库记录判定。成员角色有 `owner` 和 `member` 两种，只有所有者能添加成员。创建团队与创建首位所有者应在同一次数据库写入中完成，避免留下没人能管理的团队。

## 跟做

把下列模型追加到 `api/prisma/schema.prisma`。在 `api` 运行 `npx prisma migrate dev --name auth_teams`，再执行 `npx prisma generate`。安装 `npm install @nestjs/jwt@11`。若用 `npm view` 或锁文件确认该包的当前兼容版本，可保持 Nest 11 和实际解析出的兼容版本。

```prisma
enum TeamRole {
  owner
  member
}

model User {
  id           String       @id @default(uuid())
  email        String       @unique
  passwordHash String
  memberships  Membership[]
}

model Team {
  id          String       @id @default(uuid())
  name        String
  memberships Membership[]
}

model Membership {
  teamId String
  userId String
  role   TeamRole @default(member)
  team   Team     @relation(fields: [teamId], references: [id])
  user   User     @relation(fields: [userId], references: [id])

  @@id([teamId, userId])
  @@index([userId])
}
```

在 `api/src/auth.ts` 新建认证代码，以下为需接入 Nest 模块的片段。用本机命令 `node -p "require('node:crypto').randomBytes(32).toString('hex')"` 生成自己的 `JWT_SECRET` 放到 `api/.env`。在 `AppModule.imports` 加入 `JwtModule.registerAsync({inject:[ConfigService],useFactory:(c:ConfigService)=>({secret:c.getOrThrow<string>('JWT_SECRET'),signOptions:{algorithm:'HS256',expiresIn:'30m'},verifyOptions:{algorithms:['HS256']}})})`。`ConfigService` 从 `@nestjs/config` 导入，`JwtModule` 从 `@nestjs/jwt` 导入。密码经带盐 scrypt 派生后存储，验证时以恒定时间比对等长缓冲区。

```ts
// api/src/auth.ts，后文 AuthController 与此片段放在一起
import { randomBytes, scrypt, timingSafeEqual } from 'node:crypto';
import { promisify } from 'node:util';
import { Transform } from 'class-transformer';
import { IsEmail, IsString, MaxLength, MinLength } from 'class-validator';
import {
  Body, CanActivate, ConflictException, Controller, ExecutionContext,
  HttpCode, Injectable, Post, UnauthorizedException,
} from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';
import { Prisma } from '@prisma/client';
import { PrismaService } from './prisma.service';

const derive = promisify(scrypt);

class Credentials {
  @Transform(({ value }) => typeof value === 'string' ? value.trim().toLowerCase() : value)
  @IsEmail() @MaxLength(254)
  email!: string;

  @IsString() @MinLength(12) @MaxLength(128)
  password!: string;
}

async function hashPassword(password: string) {
  const salt = randomBytes(16).toString('hex');
  return `${salt}:${(await derive(password, salt, 64)).toString('hex')}`;
}

async function matches(password: string, stored: string) {
  const [salt, hex] = stored.split(':');
  if (!salt || !hex) return false;
  const expected = Buffer.from(hex, 'hex');
  const actual = await derive(password, salt, 64);
  return expected.length === actual.length && timingSafeEqual(expected, actual);
}

@Controller('auth')
export class AuthController {
  constructor(private db: PrismaService, private jwt: JwtService) {}

  @Post('register')
  async register(@Body() body: Credentials) {
    try {
      return await this.db.user.create({
        data: { email: body.email, passwordHash: await hashPassword(body.password) },
        select: { id: true, email: true },
      });
    } catch (error) {
      if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === 'P2002') {
        throw new ConflictException('此邮箱已注册');
      }
      throw error;
    }
  }

  @Post('login') @HttpCode(200)
  async login(@Body() body: Credentials) {
    const user = await this.db.user.findUnique({ where: { email: body.email } });
    if (!user || !await matches(body.password, user.passwordHash)) {
      throw new UnauthorizedException('邮箱或密码有误');
    }
    return { accessToken: await this.jwt.signAsync({ sub: user.id }) };
  }
}

@Injectable()
export class BearerGuard implements CanActivate {
  constructor(private jwt: JwtService) {}

  async verify(token: string): Promise<{ sub: string }> {
    try {
      const claims = await this.jwt.verifyAsync<{ sub?: string }>(token);
      if (typeof claims.sub !== 'string' || !claims.sub) throw new Error('missing sub');
      return { sub: claims.sub };
    } catch {
      throw new UnauthorizedException('请重新登录');
    }
  }

  async canActivate(ctx: ExecutionContext) {
    const req = ctx.switchToHttp().getRequest();
    const token = /^Bearer (\S+)$/i.exec(req.headers.authorization ?? '')?.[1];
    if (!token) throw new UnauthorizedException('请登录');
    req.user = await this.verify(token);
    return true;
  }
}
```

下面的团队控制器和服务放进 `api/src/teams.ts`。Nest 按装饰器里的顺序调用 guard。先写入用户上下文，再解析 `:teamId`。第 49 天复用两个 guard，第 51 天复用 `TeamAccess.requireMember`。在 `AppModule.controllers` 注册 `AuthController`、`TeamsController`，在 `providers` 注册 `BearerGuard`、`TeamGuard`、`TeamAccess`。

```ts
// api/src/teams.ts
import {
  Body, CanActivate, ConflictException, Controller, ExecutionContext,
  ForbiddenException, Get, Injectable, NotFoundException, Param, Post, Req, UseGuards,
} from '@nestjs/common';
import { Prisma, TeamRole } from '@prisma/client';
import { Transform } from 'class-transformer';
import { IsEmail, IsString, Matches, MaxLength } from 'class-validator';
import { BearerGuard } from './auth';
import { PrismaService } from './prisma.service';

export type ActorRequest = { user: { sub: string }; teamRole: TeamRole };

class TeamName {
  @IsString() @Matches(/\S/) @MaxLength(80)
  name!: string;
}

class MemberEmail {
  @Transform(({ value }) => typeof value === 'string' ? value.trim().toLowerCase() : value)
  @IsEmail() @MaxLength(254)
  email!: string;
}

@Injectable()
export class TeamAccess {
  constructor(private db: PrismaService) {}

  async requireMember(teamId: string, userId: string) {
    const row = await this.db.membership.findUnique({
      where: { teamId_userId: { teamId, userId } },
    });
    if (!row) throw new ForbiddenException('你不属于该团队');
    return row;
  }
}

@Injectable()
export class TeamGuard implements CanActivate {
  constructor(private access: TeamAccess) {}

  async canActivate(ctx: ExecutionContext) {
    const req = ctx.switchToHttp().getRequest<ActorRequest & { params: { teamId: string } }>();
    req.teamRole = (await this.access.requireMember(req.params.teamId, req.user.sub)).role;
    return true;
  }
}

@Controller('teams')
@UseGuards(BearerGuard)
export class TeamsController {
  constructor(private db: PrismaService) {}

  @Get()
  async list(@Req() req: ActorRequest) {
    const rows = await this.db.membership.findMany({
      where: { userId: req.user.sub }, include: { team: true }, orderBy: { teamId: 'asc' },
    });
    return rows.map(({ team, role }) => ({ ...team, role }));
  }

  @Post()
  create(@Req() req: ActorRequest, @Body() body: TeamName) {
    return this.db.team.create({ data: {
      name: body.name.trim(), memberships: { create: { userId: req.user.sub, role: 'owner' } },
    } });
  }

  @Post(':teamId/members') @UseGuards(TeamGuard)
  async add(@Req() req: ActorRequest, @Param('teamId') teamId: string, @Body() body: MemberEmail) {
    if (req.teamRole !== 'owner') throw new ForbiddenException('只有所有者可以添加成员');
    const user = await this.db.user.findUnique({ where: { email: body.email } });
    if (!user) throw new NotFoundException('请先注册');
    try {
      return await this.db.membership.create({ data: { teamId, userId: user.id } });
    } catch (error) {
      if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === 'P2002') {
        throw new ConflictException('该账号已是成员');
      }
      throw error;
    }
  }
}
```

用本机 HTTP 客户端分别注册 `lin@example.test`、`zhou@example.test`、`yi@example.test`。请求为 `POST /api/auth/register`，JSON 使用相同字段 `email`、`password`，可用本机演练密码 `board-demo-12345`，预期 `201 {id,email}`。再把同一输入送到 `POST /api/auth/login`，记录各自的 `accessToken`。后续请求头填写 `Authorization: Bearer <自己的令牌>`。小林与小易各用 `POST /api/teams` 送 `{"name":"甲队"}` 或 `{"name":"乙队"}`，保存返回的团队 ID。小林调用 `POST /api/teams/<甲队ID>/members`，输入 `{"email":"zhou@example.test"}`，预期 `201` 且 `role` 为 `member`。

## 练习

分别用小周和小易调用 `GET /api/teams`，再用小周向甲队添加成员。补测重复注册和用错密码，记下状态。可用浏览器之外的本机 HTTP 客户端，发送 JSON 时设置 `Content-Type: application/json`。

## 参考答案与验收

小周列表只有甲队，角色为 `member`；小易列表只有乙队，角色为 `owner`。小周添加成员返回 `403`，重复注册返回 `409`，错误密码返回 `401`。确认注册响应里没有 `passwordHash`。退出客户端时清掉令牌。下一课保留这三位虚构用户和两个团队的数据。

## AI 搭档

画完请求顺序再问。「请用三张卡片检查我的调用顺序，分别问所用令牌、URL 中的团队和数据库中的成员关系。先给我机会判断结果，再对照 401/403。输入只保留假账号和状态码，删掉 JWT、密码、连接串及真实客户数据。」

# 第 49 天：把项目和任务 CRUD 都限定在团队内

原课：<https://xiguadev.com/node-60days/day-49>

## 今日先学

项目和任务都是团队资源。先通过第 48 天的成员守卫，再让数据库查询一直带着 URL 中的团队和项目。`PATCH` 只修改实际提交的字段，任务创建时的默认状态是 `todo`。数据库还要阻止任务的团队与项目的团队不一致。我们用 `(teamId,projectId)` 外键表达这个规则，之后即使有后台作业写库，也得遵守同一约束。

## 跟做

在 `Team` 上新增 `projects Project[]`，在 `api/prisma/schema.prisma` 追加下列模型。在 `api` 运行 `npx prisma migrate dev --name projects_tasks` 和 `npx prisma generate`。若开发进程没重新载入客户端，重启 `npm run start:dev`。

```prisma
enum TaskStatus {
  todo
  doing
  done
}

model Project {
  id     String @id @default(uuid())
  teamId String
  name   String
  team   Team   @relation(fields: [teamId], references: [id])
  tasks  Task[]

  @@unique([teamId, id])
}

model Task {
  id        String     @id @default(uuid())
  teamId    String
  projectId String
  title     String
  status    TaskStatus @default(todo)
  createdAt DateTime   @default(now())
  project   Project    @relation(fields: [teamId, projectId], references: [teamId, id], onDelete: Restrict)

  @@index([teamId, projectId])
}
```

把下列项目服务放到 `api/src/projects.ts`。唯一 `id` 出现在 `where` 的顶层，Prisma 6 允许同时传 `teamId`，所以修改和删除都在同一条受限查询中执行。下列片段与后面的控制器合用。`P2025` 对应本次操作找不到记录，`P2003` 对应外键限制触发。

```ts
// api/src/projects.ts，包含服务、DTO 与控制器
import {
  BadRequestException, Body, ConflictException, Controller, Delete, Get,
  HttpCode, Injectable, NotFoundException, Param, Patch, Post, UseGuards,
} from '@nestjs/common';
import { IsEnum, IsString, Matches, MaxLength, ValidateIf } from 'class-validator';
import { Prisma, TaskStatus } from '@prisma/client';
import { BearerGuard } from './auth';
import { TeamGuard } from './teams';
import { PrismaService } from './prisma.service';

function mapWriteError(error: unknown): never {
  if (error instanceof Prisma.PrismaClientKnownRequestError) {
    if (error.code === 'P2025') throw new NotFoundException('当前范围内找不到记录');
    if (error.code === 'P2003') throw new ConflictException('关联记录阻止了本次写入');
  }
  throw error;
}

const taskFields = { id: true, title: true, status: true, teamId: true, projectId: true } as const;

@Injectable()
export class BoardService {
  constructor(private db: PrismaService) {}

  async requireProject(teamId: string, projectId: string) {
    const project = await this.db.project.findUnique({ where: { id: projectId, teamId } });
    if (!project) throw new NotFoundException('项目不存在');
    return project;
  }

  listProjects(teamId: string) {
    return this.db.project.findMany({ where: { teamId }, orderBy: { id: 'asc' } });
  }

  createProject(teamId: string, name: string) {
    return this.db.project.create({ data: { teamId, name } });
  }

  renameProject(teamId: string, id: string, name: string) {
    return this.db.project.update({ where: { id, teamId }, data: { name } }).catch(mapWriteError);
  }

  async deleteProject(teamId: string, id: string) {
    await this.db.project.delete({ where: { id, teamId } }).catch(mapWriteError);
  }

  async createTask(teamId: string, projectId: string, title: string) {
    await this.requireProject(teamId, projectId);
    return this.db.task.create({
      data: { teamId, projectId, title }, select: taskFields,
    }).catch(mapWriteError);
  }

  async getTask(teamId: string, projectId: string, id: string) {
    const task = await this.db.task.findUnique({
      where: { id, teamId, projectId }, select: taskFields,
    });
    if (!task) throw new NotFoundException('任务不存在');
    return task;
  }

  updateTask(teamId: string, projectId: string, id: string, body: ChangeTask) {
    const data = { title: body.title?.trim(), status: body.status };
    if (data.title === undefined && data.status === undefined) {
      throw new BadRequestException('请提供 title 或 status');
    }
    return this.db.task.update({
      where: { id, teamId, projectId }, data, select: taskFields,
    }).catch(mapWriteError);
  }

  async deleteTask(teamId: string, projectId: string, id: string) {
    await this.db.task.delete({ where: { id, teamId, projectId } }).catch(mapWriteError);
  }
}

class ProjectName {
  @IsString() @Matches(/\S/) @MaxLength(80)
  name!: string;
}

class NewTask {
  @IsString() @Matches(/\S/) @MaxLength(120)
  title!: string;
}

class ChangeTask {
  @ValidateIf((_object, value) => value !== undefined)
  @IsString() @Matches(/\S/) @MaxLength(120)
  title?: string;

  @ValidateIf((_object, value) => value !== undefined)
  @IsEnum(TaskStatus)
  status?: TaskStatus;
}

@Controller('teams/:teamId/projects')
@UseGuards(BearerGuard, TeamGuard)
export class ProjectsController {
  constructor(private board: BoardService) {}

  @Get()
  list(@Param('teamId') t: string) { return this.board.listProjects(t); }

  @Post()
  create(@Param('teamId') t: string, @Body() body: ProjectName) {
    return this.board.createProject(t, body.name.trim());
  }

  @Get(':projectId')
  get(@Param('teamId') t: string, @Param('projectId') p: string) {
    return this.board.requireProject(t, p);
  }

  @Patch(':projectId')
  rename(@Param('teamId') t: string, @Param('projectId') p: string, @Body() body: ProjectName) {
    return this.board.renameProject(t, p, body.name.trim());
  }

  @Delete(':projectId') @HttpCode(204)
  remove(@Param('teamId') t: string, @Param('projectId') p: string) {
    return this.board.deleteProject(t, p);
  }
}

@Controller('teams/:teamId/projects/:projectId/tasks')
@UseGuards(BearerGuard, TeamGuard)
export class TasksController {
  constructor(private board: BoardService) {}

  @Post()
  create(@Param('teamId') t: string, @Param('projectId') p: string, @Body() body: NewTask) {
    return this.board.createTask(t, p, body.title.trim());
  }

  @Get(':taskId')
  get(@Param('teamId') t: string, @Param('projectId') p: string, @Param('taskId') k: string) {
    return this.board.getTask(t, p, k);
  }

  @Patch(':taskId')
  change(@Param('teamId') t: string, @Param('projectId') p: string,
         @Param('taskId') k: string, @Body() body: ChangeTask) {
    return this.board.updateTask(t, p, k, body);
  }

  @Delete(':taskId') @HttpCode(204)
  remove(@Param('teamId') t: string, @Param('projectId') p: string, @Param('taskId') k: string) {
    return this.board.deleteTask(t, p, k);
  }
}
```

在 `AppModule.controllers` 注册 `ProjectsController`、`TasksController`，`providers` 注册 `BoardService`。使用小林令牌向 `/api/teams/<甲队ID>/projects` POST `{"name":"上线准备"}`，记下 `201` 返回的项目 ID。沿该 URL 加 `/<项目ID>/tasks`，POST `{"title":"写发布说明"}`。应看到 `201` 返回任务 ID 和 `todo`。再加 `/<任务ID>` 读取，返回值只含约定的五个字段。

## 练习

让小周把该任务改成 `doing`，小易尝试读取同一合法团队路径。然后用小林测试 `{"status":null}` 和删除仍有任务的项目。保留上线项目，另建一个空项目练习改名和删除，记录输出。

## 参考答案与验收

小周提交 `{"status":"doing"}` 得 `200`；小易得 `403`；小林请求项目中不存在的任务得 `404`；`null` 得 `400`。空对象也得 `400`，而只提交 `title` 时保留旧状态。删除含任务项目得 `409`，空项目可先改名得 `200` 再删除得 `204`，响应无正文。重读上线项目中的任务确认状态仍为 `doing`，下一课会按状态查询它。

## AI 搭档

自己先读一遍查询条件。「请只检查我贴出的 `where` 和请求契约。逐个问我哪一层校验团队成员、哪一层约束项目与任务，再指出一条值得补的正常权限测试。不要直接给实现。片段使用虚构 ID，删掉密码、令牌和真实客户数据。」

# 第 50 天：给看板三列加过滤、排序和翻页

原课：<https://xiguadev.com/node-60days/day-50>

## 今日先学

看板的每一列都是同一个任务集合按状态过滤的结果。今天增加项目内列表接口，三列依次查 `todo`、`doing`、`done`，每一列分别保存自己的页码位置。空列返回 `200` 与空数组。页内按创建时间倒序排列，时间相同的记录再按 ID 倒序，数据库因此能给出明确的次序。活跃看板在翻页过程中仍可能有新增或移动，导致偏移量分页重复或漏项；第 51 天收到更新通知后从第一页重读。

## 跟做

在 `api/src/projects.ts` 的 `@nestjs/common` 导入中增加 `Query`，把 DTO 放在 `TasksController` 前，类方法分别加入指定类。`skip` 是跳过几条，`take` 是最多取几条；多查一条用于判断是否还可继续。最多允许 `limit=50` 和 `offset=10000`，到上限时结束这次浏览。前端只展示页面拥有的任务，项目总数会由第 53 天统计接口独立提供。

```ts
// api/src/projects.ts 的新增导入，已有的导入继续保留
import { Type } from 'class-transformer';
import { IsInt, Min, Max } from 'class-validator';

// 放在 TasksController 之前，复用已有 ValidateIf、IsEnum、TaskStatus
class TaskListQuery {
  @ValidateIf((_object, value) => value !== undefined)
  @IsEnum(TaskStatus)
  status?: TaskStatus;

  @Type(() => Number) @IsInt() @Min(1) @Max(50)
  limit = 20;

  @Type(() => Number) @IsInt() @Min(0) @Max(10000)
  offset = 0;
}
```

```ts
// 加入 BoardService 类，复用 db、requireProject 和 taskFields
async listTasks(teamId: string, projectId: string, query: TaskListQuery) {
  await this.requireProject(teamId, projectId);
  const rows = await this.db.task.findMany({
    where: { teamId, projectId, status: query.status },
    orderBy: [{ createdAt: 'desc' }, { id: 'desc' }],
    skip: query.offset, take: query.limit + 1, select: taskFields,
  });
  const next = query.offset + query.limit;
  return {
    items: rows.slice(0, query.limit),
    nextOffset: rows.length > query.limit && next <= 10000 ? next : null,
  };
}
```

```ts
// 加入已有的 TasksController 类，复用类上的两个守卫
@Get()
list(@Param('teamId') t: string, @Param('projectId') p: string, @Query() q: TaskListQuery) {
  return this.board.listTasks(t, p, q);
}
```

先用小林在昨天的项目新增两条 `todo`。再拿小周的令牌请求本机端点，路径替换为自己保存的两个 ID。命令使用 Bash，`TOKEN` 表示只保留在当前终端的练习令牌；也可在本机 HTTP 客户端设置认证头。

```bash
BASE='http://127.0.0.1:3000/api/teams/<甲队ID>/projects/<项目ID>/tasks'
curl -i -H "Authorization: Bearer $TOKEN" "$BASE?status=todo&limit=1&offset=0"
```

预期响应中 `items` 有一条，`nextOffset` 为 `1`。用返回值请求第二页，若正好只有两条，则第二页的 `nextOffset` 是 `null`。请求 `?status=doing` 时找到第 49 天移动过的任务；省略 `status` 时按同一规则浏览所有状态。把项目状态列顺序写进 README，后面 React 直接复用。

## 练习

在同一个项目用 `limit=1` 验证两页 ID 不同，再查没有任务的 `done` 列。小周把一条 `todo` 改为 `done`，从两列的第一页重新读取。最后用小易令牌和非法状态分别请求一次。

## 参考答案与验收

初始 `done` 列返回 `{ "items": [], "nextOffset": null }`。移动后，`done` 能读到新任务，`todo` 减少一条；其他列的分页位置无法代表这两列的进度。小易读取甲队列表返回 `403`；小周传 `status=archived`、`limit=0` 或 `offset=-1` 得 `400`。保留一组实际响应，下一课用它确认另一个客户端收到事件后刷新的是同一份数据库数据。

## AI 搭档

自己先记下两页 ID 再问。「根据我贴的三列虚构 JSON，请出一道中途移动任务的推演题，等我回答哪些列要重读，再解释 offset 为什么会漂移。不要代写列表接口。材料里只留合成任务 ID、状态与页号，删掉令牌和真实客户数据。」


# 第 51 天：让同团队看板收到实时更新

原课：<https://xiguadev.com/node-60days/day-51>

## 今日先学

实现「别人改了数据，我这页要更新」有三种方案：轮询最简单，每 N 秒请求一次列表，实现成本最低但延迟高、请求量随在线人数放大；SSE 用一条 HTTP 长连接由服务端单向推送，浏览器原生 `EventSource` 自动重连，但只能服务端到客户端；WebSocket 双向通信，适合多端协作提示。原版第 51 天选 SSE，本改写版改用 Socket.IO（WebSocket 优先、自动降级到 HTTP 长轮询），好处是浏览器兼容和断线重连开箱即用，代价是多一个实时服务和房间状态。Socket.IO 默认 25 秒心跳检测断线，漏掉的事件靠重连后重读 HTTP 列表补齐。要注意单实例边界：房间与连接存在单个进程内存里，多实例部署必须接 Redis adapter 才能跨进程广播，这会引入新的故障点。HTTP 列表负责给页面一份当前快照；WebSocket 负责通知「数据可能变了」，不是把数据库搬到浏览器。收到事件后仍用第 50 天的列表接口重读，因此断线、漏事件或浏览器重连不会让页面把旧数据当成真相。房间按团队划分，客户端不能自行声明有权加入哪个团队；服务端必须从已验证的令牌取用户 ID，再查 Membership。

## 跟做

在 `api` 安装 `npm install @nestjs/websockets@11 @nestjs/platform-socket.io@11 socket.io@4`，保持 Socket.IO 与 Nest 11 兼容。将网关放在 `api/src/board.gateway.ts`，并在 `AppModule.providers` 注册。这里只发送任务 ID 与动作，不广播标题、令牌或整份任务；前端收到后请求列表刷新。`namespace:'/board'` 只是命名空间，握手端点仍是默认的 `/socket.io/`，本机 Vite 代理必须包含 `/socket.io`（见第 47 天）；下面显式写出 `path` 是为了让两端对照更清楚，值与默认值相同。

```ts
// api/src/board.gateway.ts
import {
  ConnectedSocket, MessageBody, OnGatewayConnection, SubscribeMessage,
  WebSocketGateway, WebSocketServer,
} from '@nestjs/websockets';
import { ForbiddenException, Injectable } from '@nestjs/common';
import { JwtService } from '@nestjs/jwt';
import { Server, Socket } from 'socket.io';
import { PrismaService } from './prisma.service';

@WebSocketGateway({ namespace: '/board', path: '/socket.io', cors: { origin: ['http://127.0.0.1:5173'] } })
export class BoardGateway implements OnGatewayConnection {
  @WebSocketServer() server!: Server;
  constructor(private jwt: JwtService, private db: PrismaService) {}

  async handleConnection(socket: Socket) {
    try {
      const token = socket.handshake.auth?.token;
      if (typeof token !== 'string') throw new Error('missing token');
      const claims = await this.jwt.verifyAsync<{ sub: string }>(token);
      if (!claims.sub) throw new Error('missing user');
      socket.data.userId = claims.sub;
    } catch {
      socket.disconnect(true);
    }
  }

  @SubscribeMessage('team:join')
  async join(@ConnectedSocket() socket: Socket, @MessageBody() body: { teamId?: string }) {
    if (typeof body?.teamId !== 'string') throw new ForbiddenException();
    const membership = await this.db.membership.findUnique({
      where: { teamId_userId: { teamId: body.teamId, userId: socket.data.userId } },
      select: { teamId: true },
    });
    if (!membership) throw new ForbiddenException();
    await socket.join(`team:${membership.teamId}`);
    return { joined: true };
  }

  taskChanged(teamId: string, taskId: string, action: 'created' | 'updated' | 'deleted') {
    this.server.to(`team:${teamId}`).emit('task:changed', { taskId, action });
  }
}
```

在 `BoardService` 建构子注入 `BoardGateway`。任务建立成功后，在回传前呼叫 `this.gateway.taskChanged(teamId, task.id, 'created')`；更新呼叫 `updated`，删除成功后呼叫 `deleted`。若你暂时把 Gateway 与 Service 放同一档，避免循环汇入；较清晰的做法是独立档案并以 Nest provider 注入。前端后续会以 `socket.io-client` 连线，团队 ID 来自已载入的团队清单。

## 练习

小林和小周各自在本机客户端登入。让两人加入甲队房间，小易尝试加入甲队。小林建立任务，观察甲队成员只收到 `task:changed` 和任务 ID；小易不得加入也不得收到事件。拔掉网路再恢复，确认页面以 HTTP 重取列表，而不是假设每个事件都收到。

## 参考答案与验收

已登入的甲队成员加入成功；无令牌的连线会断开；乙队成员加入甲队失败，且不进入房间。事件不含任务标题、密码或令牌。断线期间更新的任务仍可由重连后重新取得的 HTTP 列表读到。这是即时提示，不是讯息持久化；可靠通知工作由下一天的伫列处理。

## AI 搭档

先自己描述房间授权再问。「请扮演测试同事，只问我三个问题：房间名由谁决定、服务端用什么资料确认成员、事件漏掉后从哪里恢复。等我回答后才指出缺的正常权限测试。只提供合成 ID，不贴 JWT、密码或真实客户资料。」

# 第 52 天：把通知放进 Redis 与 BullMQ

原课：<https://xiguadev.com/node-60days/day-52>

## 今日先学

即时事件适合提示正在看页面的使用者；通知中心要在离线后仍看得到，就需存入 PostgreSQL。把通知写入与任务变更放进同一个 Prisma transaction，提交后再排 BullMQ 作业。Redis / BullMQ 负责延后处理邮件或摘要，Redis 暂时不可用时不能回滚已提交的任务，也不能把通知工作悄悄丢掉。今日先做可靠的资料通知；寄信留作后续适配器，不在本机或云端发真实邮件。

## 跟做

沿用前面阶段已练习的 Redis 和 BullMQ。将模型追加到 `api/prisma/schema.prisma`，在 `api` 执行 `npx prisma migrate dev --name notifications`。`dedupeKey` 让同一任务事件重试时不重复新增收件通知。

```prisma
model Notification {
  id        String   @id @default(uuid())
  userId    String
  teamId    String
  taskId    String
  kind      String
  dedupeKey String   @unique
  createdAt DateTime @default(now())
  readAt    DateTime?
  @@index([userId, createdAt])
}
```

沿用第 38 天的 `@nestjs/bullmq`：`BullModule.forRoot` 的 `connection` 是 ioredis 的 `RedisOptions`，**没有 `url` 字段**，写 `{ url: process.env.REDIS_URL }` 会报 TS 多余属性，运行时还会被忽略、连到默认 `127.0.0.1:6379`，到第 55 天的 `rediss://` 远端就完全失效。把 `REDIS_URL` 用 `new URL()` 拆成 host/port/账号/密码/TLS（与第 38 天 `src/queue/queue.module.ts` 同一套逻辑），在 `AppModule` 注册全局连接，再在 `NotificationsModule` 注册伫列。下面的三个档案是可编译的最小实作；不要把裸 `new Worker()` 片段贴进 Nest 专案，那会和第 38 天的写法冲突。

```ts
// api/src/redis/redis-options.ts：把 REDIS_URL 拆成 ioredis 的 RedisOptions
import type { RedisOptions } from 'ioredis';

export function redisOptions(raw: string): RedisOptions {
  const url = new URL(raw);
  if (!['redis:', 'rediss:'].includes(url.protocol)) throw new Error('Redis 协议无效');
  const db = Number(url.pathname.slice(1) || '0');
  if (!Number.isInteger(db) || db < 0) throw new Error('Redis DB 无效');
  return {
    host: url.hostname,
    port: Number(url.port || 6379),
    db,
    username: url.username ? decodeURIComponent(url.username) : undefined,
    password: url.password ? decodeURIComponent(url.password) : undefined,
    ...(url.protocol === 'rediss:' ? { tls: {} } : {}),
    maxRetriesPerRequest: null,
    enableOfflineQueue: false,
  };
}

// api/src/app.module.ts 的 imports 里：
// BullModule.forRootAsync({
//   imports: [ConfigModule], inject: [ConfigService],
//   useFactory: (config: ConfigService) => ({
//     connection: redisOptions(config.getOrThrow<string>('REDIS_URL')),
//   }),
// }),
```

```ts
// api/src/notifications/notifications.module.ts
import { BullModule } from '@nestjs/bullmq';
import { Module } from '@nestjs/common';
import { NotificationsProcessor } from './notifications.processor';
import { NotificationsService } from './notifications.service';

@Module({
  imports: [BullModule.registerQueue({ name: 'notifications' })],
  providers: [NotificationsService, NotificationsProcessor],
  exports: [NotificationsService],
})
export class NotificationsModule {}
```

```ts
// api/src/notifications/notifications.service.ts
import { InjectQueue } from '@nestjs/bullmq';
import { Injectable } from '@nestjs/common';
import { Queue } from 'bullmq';
import { PrismaService } from '../prisma.service';

@Injectable()
export class NotificationsService {
  constructor(
    private readonly prisma: PrismaService,
    @InjectQueue('notifications') private readonly queue: Queue,
  ) {}

  async enqueueMany(notificationIds: string[]) {
    await this.queue.addBulk(notificationIds.map((notificationId) => ({
      name: 'task-changed',
      data: { notificationId },
      opts: {
        jobId: notificationId,
        attempts: 5,
        backoff: { type: 'exponential', delay: 1000 },
        removeOnComplete: 1000,
        removeOnFail: 5000,
      },
    })));
  }

  // 补偿扫描器：把已落库但尚未成功入队的通知重新排入
  async requeuePending(limit = 100) {
    const pending = await this.prisma.notification.findMany({
      where: { readAt: null },
      orderBy: { createdAt: 'asc' },
      take: limit,
      select: { id: true },
    });
    await this.enqueueMany(pending.map((n) => n.id));
    return pending.length;
  }
}
```

```ts
// api/src/notifications/notifications.processor.ts
import { Processor, WorkerHost } from '@nestjs/bullmq';
import { Logger } from '@nestjs/common';
import { Job } from 'bullmq';
import { PrismaService } from '../prisma.service';

@Processor('notifications')
export class NotificationsProcessor extends WorkerHost {
  private readonly logger = new Logger(NotificationsProcessor.name);
  constructor(private readonly prisma: PrismaService) { super(); }

  async process(job: Job<{ notificationId: string }>) {
    const notice = await this.prisma.notification.findUnique({
      where: { id: job.data.notificationId },
    });
    if (!notice) return;
    // 本地演练只记录事件；真实邮件/adapter 留在后续单元
    this.logger.log(`notification ${notice.id} ready to deliver`);
  }
}
```

在任务变更 transaction 中写入任务和通知列；通知以团队内其他成员为收件人，排除操作者，并用 `createMany({ skipDuplicates: true })` 或唯一键处理重试。提交 transaction 后呼叫 `enqueueMany(notificationIds)`。若 Redis 暂时不可用，捕获排程错误、记录失败指标，通知列仍留在资料库；回传操作成功，不要让使用者重试再次修改任务。恢复后由 `requeuePending()` 补排，可手动呼叫或交给定时任务；BullMQ 的 `jobId` 与 `dedupeKey` 共同保证幂等。

## 练习

用小周更新一个任务，确认同团队小林能看到一列未读通知，小周不会收到自己的通知。手动重跑同一通知排程两次，验证通知表不重复。停止本机 Redis 后再改任务，确认任务与通知仍已提交，日志记录排程失败；恢复 Redis 后呼叫 `NotificationsService.requeuePending()`，再确认作业被消费者处理完成。

## 参考答案与验收

通知查询以登入者 `userId` 作条件，返回自己的通知；未读以 `readAt IS NULL` 判定。重复 job ID 和 `dedupeKey` 都不会新增第二列。Redis 故障时任务和通知列都已提交，`requeuePending()` 的返回值等于本次补排的数量，且消费者日志出现对应通知 ID；作业最多重试五次，仍失败时需可观测并能人工重放。本练习不实际连邮件服务。

## AI 搭档

先画出提交顺序再问。「请用『任务 transaction、通知列、Redis job、消费者』四个节点让我解释故障时资料在哪。每次只问一个问题，不代画答案；最后指出哪个步骤需幂等。内容用虚构 ID，不贴 Redis URL、凭证或真实客户资料。」

# 第 53 天：用资料库统计支援团队看板

原课：<https://xiguadev.com/node-60days/day-53>

## 今日先学

看板统计回答的是「这个专案目前每种状态有几项」，不是把前端载入的单页项目数出来。若页面只载入 20 条，前端数量就不是总量。统计端点依然必须经 Bearer 与 TeamGuard，SQL 的 where 条件同时限制 `teamId`、`projectId`。查不到专案回 `404`，没有任务时仍回传三种状态的零值。

## 跟做

在 `BoardService` 中加入统计方法，并在 `api/src/projects.ts` 的 `TasksController` 加入 `GET .../tasks/stats` 路由。任务板工程的 `PrismaService` 是 `src/prisma.service.ts`（博客工程才是 `src/prisma/prisma.service.ts`），`src/notifications/` 下的文件相对导入写 `../prisma.service`，不要混用两个工程的目录结构。此处的原生 SQL 片段放在已有 `BoardService`，表名需使用 Prisma 预设的 PostgreSQL 名称；如果专案设定了 `@@map` 或 `@map`，按实际资料表改名。参数化模板不可改成字串拼接。

```ts
// api/src/projects.ts，BoardService 内
async taskStats(teamId: string, projectId: string) {
  await this.requireProject(teamId, projectId);
  const rows = await this.db.$queryRaw<Array<{ status: string; count: bigint }>>`
    SELECT status::text AS status, COUNT(*)::bigint AS count
    FROM "Task"
    WHERE "teamId" = ${teamId} AND "projectId" = ${projectId}
    GROUP BY status
  `;
  return {
    todo: Number(rows.find(row => row.status === 'todo')?.count ?? 0n),
    doing: Number(rows.find(row => row.status === 'doing')?.count ?? 0n),
    done: Number(rows.find(row => row.status === 'done')?.count ?? 0n),
  };
}
```

`TaskStatus` 是 PostgreSQL enum，`status::text` 让回传型别可直接比较。此处数量限制在 JS 安全整数可表示的范围才适合回传 number；若业务资料可能超过安全整数，API 改回传十进位字串并让前端以字串显示。再在 `TasksController` 中加入：

```ts
// api/src/projects.ts，TasksController 内
@Get('stats')
stats(@Param('teamId') t: string, @Param('projectId') p: string) {
  return this.board.taskStats(t, p);
}
```

路由顺序上，先声明静态 `stats`，再声明 `@Get(':taskId')`，避免 `stats` 被当作任务 ID。用本机 HTTP 客户端向 `/api/teams/<甲队ID>/projects/<项目ID>/tasks/stats` 发 GET，带小周的 Bearer 令牌；此时预期 `todo`、`doing`、`done` 为数字，合计等于专案总任务数。新增一项及移动一项后重新读取。后续若加快取，写操作必须让统计快取失效；今天先直接查 PG，确保资料准确。

## 练习

小易以乙队令牌查甲队统计；小周查自己的空专案；再用小周查不存在的项目 ID。记录状态码、JSON 型别与数量。把统计值跟不分状态列表的全量结果对照，小资料量可用逐页查询，不要用单页长度代替总数。

## 参考答案与验收

小易收到 `403`；空专案回 `200 {"todo":0,"doing":0,"done":0}`；不存在的专案回 `404`。数字皆为 number，变更任务后再次查询反映最新状态。测试需同时断言权限状态和回应内容；不要因 ID 难猜就省掉团队条件。

## AI 搭档

先手算一次再问。「请根据我提供的三列合成任务状态，先问我预期计数，再核对 `COUNT`、空列和跨团队请求的结果。不要建议我以页面资料总结全量。不得贴真实客户资料或凭证。」

# 第 54 天：用 React 完成登入后的任务列表

原课：<https://xiguadev.com/node-60days/day-54>

## 今日先学

前端不要再造一份任务资料库：API 的 PostgreSQL 是唯一可信来源。今天做一条明确流程：登入取得 access token，选团队和专案，读取第一页列表，新增任务后重读。显示载入、空列表与错误三种状态；HTTP 错误不能伪装成「没有任务」。本机 Vite 将 `/api` 转发到 Nest，浏览器请求用相对路径，因此本机调整 API 主机时只需改代理设定。

## 跟做

在 `web` 执行 `npm install socket.io-client`，新增 `web/src/api.ts`。这是刻意精简的本机教学 API 用户端；`io('/board', { path:'/socket.io' })` 里 `/board` 是命名空间、`/socket.io` 是握手路径，与第 47 天 Vite 代理的 `/socket.io` 规则对应。Access token 暂存在记忆体，重整后需重新登入；正式产品应评估安全的 HttpOnly Cookie、CSRF 防护、CSP 与 HTTPS，不要长期把 token 放 localStorage。把 `web/src/App.tsx` 的启动画面替换成以下流程，CSS 继续放在既有 `App.css`。

```ts
// web/src/api.ts
import { io, type Socket } from 'socket.io-client';

export type Task = {
  id: string; title: string; status: 'todo' | 'doing' | 'done';
  teamId: string; projectId: string;
};
let token: string | undefined;
export function setToken(value?: string) { token = value; }
export function getToken() { return token; }

async function request<T>(path: string, init: RequestInit = {}): Promise<T> {
  const response = await fetch(`/api${path}`, {
    ...init,
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...init.headers,
    },
  });
  if (!response.ok) {
    const data = await response.json().catch(() => ({}));
    throw new Error(data.message ?? `请求失败（${response.status}）`);
  }
  return response.status === 204 ? undefined as T : response.json();
}
export const api = {
  login: (email: string, password: string) => request<{ accessToken: string }>('/auth/login', {
    method: 'POST', body: JSON.stringify({ email, password }),
  }),
  teams: () => request<Array<{ id: string; name: string; role: string }>>('/teams'),
  projects: (teamId: string) => request<Array<{ id: string; name: string }>>(
    `/teams/${encodeURIComponent(teamId)}/projects`,
  ),
  tasks: (teamId: string, projectId: string) => request<{ items: Task[]; nextOffset: number | null }>(
    `/teams/${encodeURIComponent(teamId)}/projects/${encodeURIComponent(projectId)}/tasks?limit=20&offset=0`,
  ),
  createTask: (teamId: string, projectId: string, title: string) => request<Task>(
    `/teams/${encodeURIComponent(teamId)}/projects/${encodeURIComponent(projectId)}/tasks`,
    { method: 'POST', body: JSON.stringify({ title }) },
  ),
};

let socket: Socket | undefined;
export function connectBoard(
  teamId: string,
  onTaskChanged: () => void,
  onError: (message: string) => void,
) {
  socket?.disconnect();
  const next = io('/board', {
    path: '/socket.io',
    auth: { token: getToken() ?? '' },
    transports: ['websocket'],
  });
  socket = next;
  next.on('connect', () => next.emit('team:join', { teamId }));
  next.on('connect_error', (error) => onError(error.message));
  next.on('task:changed', onTaskChanged);
  return () => {
    next.off('task:changed', onTaskChanged);
    next.disconnect();
    if (socket === next) socket = undefined;
  };
}
```

以下是 `web/src/App.tsx` 的完整替换内容。`useState` 保存页面状态；`useRef` 保存一个不会引起重绘的请求序号，用来忽略已经过时的请求结果。所有表单先 `preventDefault()`，防止浏览器刷新页面；所有请求先清错误并显示忙碌状态，最后清理忙碌状态。团队变更先清项目与任务，避免短暂展示上一个团队的数据。

```tsx
// web/src/App.tsx，完整替换
import { useEffect, useRef, useState, type FormEvent } from 'react';
import { api, connectBoard, setToken, type Task } from './api';
import './App.css';

type Team = { id: string; name: string; role: string };
type Project = { id: string; name: string };

export default function App() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [signedIn, setSignedIn] = useState(false);
  const [teams, setTeams] = useState<Team[]>([]);
  const [projects, setProjects] = useState<Project[]>([]);
  const [teamId, setTeamId] = useState('');
  const [projectId, setProjectId] = useState('');
  const [title, setTitle] = useState('');
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const sequence = useRef(0);
  const reloadRef = useRef<() => void>(() => {});

  useEffect(() => {
    reloadRef.current = () => { void loadProject(teamId, projectId, ++sequence.current); };
  });

  useEffect(() => {
    if (!signedIn || !teamId) return;
    return connectBoard(
      teamId,
      () => reloadRef.current(),
      (message) => setError(`实时连接失败：${message}`),
    );
  }, [signedIn, teamId]);

  async function perform(operation: (id: number) => Promise<void>) {
    const id = ++sequence.current;
    setError('');
    setLoading(true);
    try { await operation(id); }
    catch (reason) {
      if (id === sequence.current) {
        setError(reason instanceof Error ? reason.message : '请求失败');
      }
    } finally {
      if (id === sequence.current) setLoading(false);
    }
  }

  async function loadProject(team: string, project: string, id: number) {
    setProjectId(project);
    setTasks([]);
    if (!project) return;
    const page = await api.tasks(team, project);
    if (id === sequence.current) setTasks(page.items);
  }

  async function loadTeam(team: string, id: number) {
    setTeamId(team);
    setProjectId('');
    setProjects([]);
    setTasks([]);
    if (!team) return;
    const nextProjects = await api.projects(team);
    if (id !== sequence.current) return;
    setProjects(nextProjects);
    await loadProject(team, nextProjects[0]?.id ?? '', id);
  }

  async function signIn(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    await perform(async (id) => {
      setToken();
      setSignedIn(false);
      const result = await api.login(email, password);
      if (id !== sequence.current) return;
      setToken(result.accessToken);
      setPassword('');
      setSignedIn(true);
      const nextTeams = await api.teams();
      if (id !== sequence.current) return;
      setTeams(nextTeams);
      await loadTeam(nextTeams[0]?.id ?? '', id);
    });
  }

  async function addTask(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    await perform(async (id) => {
      await api.createTask(teamId, projectId, title.trim());
      if (id !== sequence.current) return;
      setTitle('');
      await loadProject(teamId, projectId, id);
    });
  }

  function signOut() {
    ++sequence.current;
    setToken();
    setSignedIn(false);
    setTeams([]);
    setProjects([]);
    setTeamId('');
    setProjectId('');
    setTasks([]);
    setTitle('');
    setPassword('');
    setError('');
    setLoading(false);
  }

  return <main className="board">
    <h1>协作任务板</h1>
    {!signedIn ? <form onSubmit={signIn}>
      <label>邮箱<input type="email" autoComplete="username" required
        value={email} onChange={event => setEmail(event.target.value)} /></label>
      <label>密码<input type="password" autoComplete="current-password" required
        value={password} onChange={event => setPassword(event.target.value)} /></label>
      <button disabled={loading}>登录</button>
    </form> : <>
      <button onClick={signOut}>退出本机登录</button>
      <p>刷新页面后需重新登录；这里只显示当前项目的前 20 条任务。</p>
      <label>团队<select disabled={loading} value={teamId}
        onChange={event => void perform(id => loadTeam(event.target.value, id))}>
        <option value="">请选择团队</option>
        {teams.map(team => <option key={team.id} value={team.id}>{team.name}</option>)}
      </select></label>
      {!loading && !error && teams.length === 0 && <p>尚未加入团队，请先完成第 48 天。</p>}
      <label>项目<select disabled={loading || !teamId} value={projectId}
        onChange={event => {
          const project = event.target.value;
          void perform(id => loadProject(teamId, project, id));
        }}>
        <option value="">请选择项目</option>
        {projects.map(project => <option key={project.id} value={project.id}>{project.name}</option>)}
      </select></label>
      {!loading && !error && teamId && projects.length === 0 && <p>该团队暂无项目，请先完成第 49 天。</p>}
      <form onSubmit={addTask}>
        <label>新任务<input value={title} maxLength={120}
          onChange={event => setTitle(event.target.value)} /></label>
        <button disabled={loading || !projectId || !title.trim()}>新增任务</button>
      </form>
      <button disabled={loading || !projectId}
        onClick={() => void perform(id => loadProject(teamId, projectId, id))}>刷新任务</button>
      {!loading && !error && projectId && tasks.length === 0 && <p>目前没有任务。</p>}
      {!loading && !error && tasks.length > 0 && <ul>
        {tasks.map(task => <li key={task.id}>[{task.status}] {task.title}</li>)}
      </ul>}
    </>}
    {loading && <p role="status">正在请求，请稍候……</p>}
    {error && <p role="alert">{error}</p>}
  </main>;
}
```

把 `web/src/App.css` 替换为最小可读样式：

```css
.board { max-width: 50rem; margin: 2rem auto; padding: 1rem; }
.board form { margin: 1rem 0; }
.board label { display: block; margin: .8rem 0; }
.board input, .board select { display: block; padding: .5rem; width: 100%; max-width: 28rem; }
.board button { margin: .5rem .5rem .5rem 0; padding: .5rem 1rem; cursor: pointer; }
.board [role="alert"] { color: #a02020; }
```

在 `web` 运行 `npm run build` 检查 TypeScript，再 `npm run dev`。API 同时在另一个终端运行，Vite 仍按第 47 天代理 `/api`。页面已接入第 51 天的 Socket.IO：登录后连接 `/board`，`team:join` 用当前团队 ID，收到 `task:changed` 就通过 HTTP 重读列表。它仍不包含注册、建团队和拖拽 UI，这些 API 先用前面的客户端验收。

### 接回原课：React Query 管理服务器状态

前面完整的 Vite 页面用 `useState` 手动管理加载与刷新，便于先理解请求流程。React Query（TanStack Query）把“服务器数据何时获取、缓存和失效”单独管理；tRPC 解决接口类型，React Query 解决客户端服务器状态，二者不是同一个东西。

回到第 47 天独立建立的 `trpc-lab`，执行 `npm install @tanstack/react-query@5`。将 `app/page.tsx` 完整替换为下面代码，原来的 `server/router.ts` 与 route handler 保留。此例直接在 Query 的函数中调用有类型的 tRPC client，便于看到两者的边界，不要求先学专用绑定库。

```tsx
// trpc-lab/app/page.tsx
'use client';
import { useState } from 'react';
import { QueryClient, QueryClientProvider, useQuery, useQueryClient } from '@tanstack/react-query';
import { createTRPCClient, httpBatchLink } from '@trpc/client';
import type { AppRouter } from '../server/router';

const trpc = createTRPCClient<AppRouter>({ links: [httpBatchLink({ url: '/api/trpc' })] });
function Greeting() {
  const queries = useQueryClient();
  const result = useQuery({
    queryKey: ['hello', '学习者'],
    queryFn: () => trpc.hello.query({ name: '学习者' }),
    staleTime: 30_000,
    retry: false,
  });
  if (result.isPending) return <p role="status">正在读取……</p>;
  if (result.isError) return <p role="alert">读取失败：{result.error.message}</p>;
  return <section><p>{result.data.message}</p><button disabled={result.isFetching}
    onClick={() => void queries.invalidateQueries({ queryKey: ['hello'] })}>
    {result.isFetching ? '正在刷新' : '使缓存失效并重读'}
  </button></section>;
}
export default function Page() {
  const [queries] = useState(() => new QueryClient());
  return <QueryClientProvider client={queries}><main><h1>tRPC + React Query</h1><Greeting /></main></QueryClientProvider>;
}
```

`queryKey` 标识缓存的查询，应该包含影响结果的参数。任务列表的 key 应含团队、项目、筛选与页码，不能让不同团队共享同一个固定 key。`staleTime` 只决定客户端何时认为结果过期，不是数据库权限；退出或切换身份时清理身份相关缓存。写操作成功后 `invalidateQueries()`，触发相关列表重取；不要只更新屏幕却忽略服务端结果。

运行 `npm run dev -- --port 3001`，观察读取、成功和刷新；服务断开后刷新应显示错误，不能显示空数据。再运行 `npm run build`。本例可以延伸到 `useMutation`：它接收一个执行写请求的 `mutationFn`，成功后失效相关列表，失败时显示错误。不要把写操作放在 `useQuery` 中。

**本日追加练习与答案：**把 `name` 改为一个页面输入值时，`queryKey` 与 `queryFn` 必须同时使用同一值；只有改请求参数而不改 key，会导致不同输入共用错误缓存。新增数据后，应失效对应团队与项目的 tasks key。验收观察请求面板，确定刷新确实重新调用服务器，而不是凭 AI 判断通过。


## 练习

沿第 48 天的假资料登入小周，选甲队与上线准备专案，确认看到第 49 天的任务，新增一条再刷新页面验证它仍存在。输入错误密码，确认错误可见；网路断开后载入任务，确认出错状态不是空列表。用小易登入并确认选单只出现乙队。再用两个浏览器分别以小周和小林登入同一团队：任一端新增任务，另一端列表应在没有手动刷新的情况下更新；切换到乙队后不应收到甲队事件。

## 参考答案与验收

成功登入会依序载入团队、专案及任务；新增返回 `201` 后重读列表并显示新任务。错误密码显示 `401` 对应讯息；断线显示请求错误；空专案显示「目前没有任务」；跨团队操作由伺服器拒绝。实时部分的可观察证据：两端都在线时，新增任务后另一端出现新列且浏览器 Network 面板多出一次 `GET .../tasks`；切换团队后不再收到原团队事件；退出登入后 Socket.IO 连线关闭。检查重新登入前 token 不存在于 localStorage、错误分支有 `finally` 清除载入状态。UI 隐藏选项不等于权限，API 的 `403` 才是服务端检查。

## AI 搭档

先操作一次再问。「请按照登入、载入团队、载入专案、载入任务、新增、错误六个状态逐项问我画面目前呈现什么。等我回答后，指出哪个事件可能没有清除旧错误或 loading。不要替我编写整个页面；只用合成帐号，不贴 token 或真实客户资料。」

# 第 55 天：准备部署设定与交付检查

原课：<https://xiguadev.com/node-60days/day-55>

## 今日先学

部署不是把本机 `.env` 和资料库搬到云端。正式环境要分离 Web 静态资产、Nest API、PostgreSQL、Redis，并以平台秘密管理器设定 `DATABASE_URL`、`REDIS_URL`、`JWT_SECRET`、允许的前端来源与 `PORT`。本日做部署准备与**本机生产发布演练**：API/Web 的 build、迁移套用、生产 Compose 启停都在本机完成；不登录真实云账号、不填账单、不连生产资源。前面阶段如已练习容器与 CI/CD，这里把 SaaS 的设定接回既有方法。

## 跟做

在 `api/.env.example` 只写变数名称和明显的占位文字，不放可用凭证；确认 `.env` 被忽略且不在版本控制中。`HOST=0.0.0.0` 不要漏：第 41 天要求容器内监听 `0.0.0.0`，而第 47 天代码默认 `127.0.0.1`，只绑定回环地址时容器外根本连不上。云端的资料库需启用 TLS 并限制网路存取，Redis 不对公网开放。`.env.example` 里的 `rediss://USER:PASSWORD@HOST:6379` 由第 52 天的 `redisOptions()` 用 `new URL()` 拆成 host/port/账号/密码并自动启用 `tls`，不要把整条 URL 直接塞给 `connection`。生产迁移使用 `prisma migrate deploy`，不要在伺服器启动流程中使用开发用的 `migrate dev`。映像或平台建置时先 `prisma generate`，再建置 API。

```dotenv
# api/.env.example，只能是占位值
DATABASE_URL=postgresql://USER:PASSWORD@HOST:5432/DB?schema=public
REDIS_URL=rediss://USER:PASSWORD@HOST:6379
JWT_SECRET=replace-with-platform-secret
PORT=3000
HOST=0.0.0.0
WEB_ORIGIN=https://example.invalid
```

让 Nest 健康端点有明确的活性检查；第 47 天的 `/api/health` 会碰资料库，适合做 readiness，但资料库短暂故障不应让平台不断重启应用。生产可分 `/api/health/live`（只确认程序）与 `/api/health/ready`（检查必要依赖），由平台用 ready 决定是否导流。CORS 白名单从 `WEB_ORIGIN` 解析，不允许任意来源；本机 Vite proxy 不需要开放 `*`。

```bash
# 本机：API 与 Web 分开建置，尚未部署
cd api
npx prisma generate
npm run build
npx prisma migrate deploy
cd ../web
npm run build
```

先在本机干净终端执行上述 build，预期 API 的 `dist` 与 Web 的 `dist` 生成。若 `migrate deploy` 指向本机 PG，会将已提交的 migration 套用到该资料库；确认 `DATABASE_URL` 后再执行，勿误指向共用或生产库。云端命令需在你选用的平台依其官方 CLI 与变数管理流程执行，本课不执行它们。部署后先由平台注入变数，再套用 migration、启动 API、发布 Web；不要把真实密码贴在终端截图或 AI 对话。

## 练习

写一份自己的部署前核对清单：Node runtime 22 / 24 / 26 LTS、资料库版本 PG16、Prisma 6.19.x、TLS 连线、秘密设定、migration、Web API base/proxy、健康检查和回滚策略。用本机假值执行 build，并在测试资料库套 migration。**本机生产发布演练**：配套包已提供 `60天配套/docker-compose.prod.yml`（API、Web、PG、Redis、一次性 migrate job、健康检查与 `depends_on: service_completed_successfully`）。先执行 `docker compose -f 60天配套/docker-compose.prod.yml config --quiet` 静态核对，把 `depends_on` 顺序、`HOST=0.0.0.0`、live/ready 探针和具名卷写进记录；镜像名按第 41 天实际构建的标签替换。若本机已有 Dockerfile 与全部镜像，再按文件注释起容器，观察迁移先完成、API 的 `/api/health/ready` 转绿再导流，分别停掉 PG 和 Redis 确认探针只停止导流、数据仍在、worker 不被误判为不健康，最后 `docker compose down` 清理。没有镜像时**只做静态核对即可**，不要把「config 通过」写成「演练已跑通」。不要建立云端资源、不要输入账单资料。

## 参考答案与验收

清单必须分清本机与云端：本机使用 loopback、假密码与 Vite proxy；云端使用平台注入的秘密、TLS PostgreSQL / Redis、正式网域与白名单。API、Web build 成功，migration 在测试资料库可套用；`.env` 不应出现在 `git status`。本机生产演练的最低证据是 `docker compose config --quiet` 通过，并能指出 migrate job 的 `restart: "no"`、`api.depends_on` 里的 `service_completed_successfully`、ready 只查 PG、live 只查进程；若已完成容器演练，再补迁移先于 API 就绪、停 PG 时 readiness 转红而 liveness 保持、停 Redis 时任务与通知已落库且恢复后补发、`docker compose down` 后无残留容器。健康端点沿用第 45 天 `HealthController`，路径按第 47 天的全局前缀改为 `/api/health/live` 与 `/api/health/ready`。确认部署次序是资料库迁移再切换应用，并说明失败时如何回到前一版。云端部分只做纸面规划，没有真实部署结果。

## 原版对照阅读

原版 Day55 用生产 Compose 完整走了一遍发布，本讲义只做纸面准备。补四点，把"发布"从动作变成可验证的工程步骤：

- **构建时变量与运行时变量的区别**：本文前端是 React + Vite，构建期变量以 `VITE_` 前缀注入并固化进静态产物；但 `web/src/api.ts` 全程用 `/api` 相对路径，由 Vite 代理或反向代理转发，**本文并不存在构建期 API 地址变量**。`NEXT_PUBLIC_*` 是第 47 天 Next.js 对照实验里的概念，不要套到本文的 Vite 工程。服务端运行时才有 `WEB_ORIGIN`（CORS 白名单）、`DATABASE_URL`、`REDIS_URL`、`JWT_SECRET`；数据库 URL、密钥等必须在运行时以环境变量注入，绝不打进镜像。把运行时变量写成构建参数，会导致同一镜像在不同环境行为不一致。
- **迁移是发布步骤，不是 Web 启动步骤**：让 Web 容器启动时跑迁移，多实例会并发冲突；应在流水线里作为一次性 job 执行，并且只做兼容变更——"代码可回滚，数据库未必可回滚"，所以加列先于删列分两次发布。
- **生产 Compose 还原发布**：配套包 `60天配套/docker-compose.prod.yml` 给出了 API、Web、PG、Redis 与一次性 migrate job 的完整编排。先用 `docker compose -f ... config --quiet` 静态核对，再在有镜像时 `up -d` 模拟一次滚动发布，观察迁移 job 先完成、api 再起来。停掉 Redis/PG 分别观察探针：应只停止导流、保留数据、不误判 worker 健康。
- **健康检查不是首页能打开**：首页 200 只说明静态资源在，不代表数据库可写、后台 worker 活着。readiness 要查关键依赖，liveness 只查进程，两者分开才能既不误杀、也不把流量导到坏实例。

## AI 搭档

先填清单再问。「请只做部署准备的口头检查，一次问一项：我在哪个环境、资料库是哪个、秘密由谁注入、迁移如何执行、怎样判断可导流。等我回答后再指出缺漏，不要帮我建立云端服务或操作帐号。请提醒我移除任何可能的凭证与真实客户资料。」


# 第 56 天：为权限和关键流程写可回归测试

原课：<https://xiguadev.com/node-60days/day-56>

## 今日先学

测试要固定用户最怕坏掉的承诺：未登录不能读写任务，团队之间不能互访，普通成员不能加人，合法成员可以新增并移动任务。单元测试用 mock 验证 `TeamAccess` 的成员判断，不连接数据库；HTTP 端到端测试通过真实 Nest 管道、守卫和 Prisma 验证状态码、响应体与持久化结果。下面给出完整文件，所有异步请求都在 `beforeAll`、`it` 或 `afterAll` 内，不能把 `await request(...)` 直接放在 `describe` 顶层。

## 跟做

### 1. 显式加载测试环境

沿用 Node 22 / 24 / 26 LTS、Nest 11、Prisma 6.19.x 和本机 PostgreSQL 16。在 `api` 目录操作；项目需已有 Jest、`@nestjs/testing`、Supertest 与相应类型。缺依赖时再由学习者补齐，本章不要求更换测试框架。关于选型：原版课程用 Vitest，并专门解释过「为什么是 Vitest 而不是大纲里的 Jest」。本改写版沿用 Nest CLI 脚手架默认生成的 Jest，因为它与 `nest new` 生成的 `test/jest-e2e.json` 和 `package.json` 测试脚本开箱即用，学员不必为了对齐原版再改一套配置，能更快跑通。两者的 API（`describe/it/expect`、mock）几乎一一对应，学会其中一种迁移成本很低；面试时能说清「原版选 Vitest 的理由（更快的 ESM 原生速度、与 Vite 前端同栈）」即可。先由学习者建立独立数据库 `board_test`，测试账号仅拥有该库权限，不复用开发、共享或生产库。

在本机运行下列命令，由你自己生成独立的测试签名密钥，把结果只保存到 `api/.env.test`；不要复制生产秘密，也不要提交生成结果。

```bash
node -p "require('node:crypto').randomBytes(32).toString('hex')"
```

`api/.env.test` 使用以下结构，密码和密钥占位符必须由你在本机替换；数据库密码中的特殊字符需做 URL 编码。确认 `.gitignore` 忽略 `.env.test`。

```dotenv
NODE_ENV=test
DATABASE_URL=postgresql://board_test_user:REPLACE_WITH_LOCAL_TEST_PASSWORD@127.0.0.1:5432/board_test?schema=public
JWT_SECRET=REPLACE_WITH_YOUR_GENERATED_TEST_SECRET
```

`NODE_ENV=test` 本身不会让 Nest 或 Jest 自动加载 `.env.test`。本章统一用 `node --env-file=.env.test ...` 在程序入口加载文件；文件不存在时直接失败。Node 优先保留已有进程环境变量，所以先在当前 Git Bash / Bash 终端清掉可能继承的三个变量，再检查库名，最后迁移和生成客户端。以下命令均在 `api` 执行，不打印连接串或密钥。

```bash
unset DATABASE_URL JWT_SECRET NODE_ENV
NODE_ENV=test node --env-file=.env.test -e 'const u=new URL(process.env.DATABASE_URL); const n=decodeURIComponent(u.pathname); if(process.env.NODE_ENV!=="test" || !["postgres:","postgresql:"].includes(u.protocol) || !/^\/[A-Za-z0-9_]+_test$/.test(n)) throw new Error("拒绝操作：必须是名字以_test结尾的独立PostgreSQL测试库"); console.log("测试库名称检查通过")'
NODE_ENV=test node --env-file=.env.test ./node_modules/prisma/build/index.js migrate deploy
NODE_ENV=test node --env-file=.env.test ./node_modules/prisma/build/index.js generate
```

测试库应先应用第 48–52 天的全部迁移，包含 `User`、`Team`、`Membership`、`Project`、`Task`、`Notification`。这里不依赖另一个手工 seed 脚本；下面的 `beforeAll` 就是本次测试的 seed：通过 HTTP 注册三个随机账号、分别登录取得 token、建立甲乙两队、添加甲队成员、建立项目，保存服务器返回的真实 ID。

### 2. 完整单元测试：`api/src/teams.spec.ts`

用 `useValue` 替换 Prisma，只提供本测试实际使用的查询方法；不要导入 `AppModule`，也不要创建真实 `PrismaService`。

```ts
import { ForbiddenException } from '@nestjs/common';
import { Test, TestingModule } from '@nestjs/testing';
import { TeamRole } from '@prisma/client';
import { PrismaService } from './prisma.service';
import { TeamAccess } from './teams';

// Jest 的 describe / beforeEach / it / expect / jest 由 Nest 脚手架的测试类型提供。
describe('TeamAccess（单元测试）', () => {
  const findUnique = jest.fn();
  let access: TeamAccess;
  let moduleRef: TestingModule;

  beforeEach(async () => {
    findUnique.mockReset();
    moduleRef = await Test.createTestingModule({
      providers: [
        TeamAccess,
        { provide: PrismaService, useValue: { membership: { findUnique } } },
      ],
    }).compile();
    access = moduleRef.get(TeamAccess);
  });

  afterEach(async () => {
    await moduleRef.close();
  });

  it.each([TeamRole.owner, TeamRole.member])('返回已有成员及角色 %s', async (role) => {
    const row = { teamId: 'team-a', userId: 'user-lin', role };
    findUnique.mockResolvedValue(row);

    await expect(access.requireMember('team-a', 'user-lin')).resolves.toEqual(row);
    expect(findUnique).toHaveBeenCalledTimes(1);
    expect(findUnique).toHaveBeenCalledWith({
      where: { teamId_userId: { teamId: 'team-a', userId: 'user-lin' } },
    });
  });

  it('不属于团队时抛出 403，而不是返回空结果', async () => {
    findUnique.mockResolvedValue(null);
    const result = access.requireMember('team-a', 'user-eve');

    await expect(result).rejects.toBeInstanceOf(ForbiddenException);
    await expect(result).rejects.toMatchObject({ status: 403 });
    expect(findUnique).toHaveBeenCalledTimes(1);
    expect(findUnique).toHaveBeenCalledWith({
      where: { teamId_userId: { teamId: 'team-a', userId: 'user-eve' } },
    });
  });
});
```

### 3. 完整 HTTP 测试：`api/test/board.e2e-spec.ts`

测试模块只写 `imports: [AppModule]`，沿用真实的认证、授权、业务服务和 Prisma。第 52 天明确给出了 `NotificationsModule` 并要求在 `AppModule` 注册；若按课程主线完成，导入 `AppModule` 就会带上这个 worker，`compile()` 会连 Redis 并把 Jest 挂住，必须先把队列与处理器换成假实现。只有确实没有创建并导入通知模块时，才不需要下面的替换，也不该凭空 import 一个不存在的模块。

已经接入 Redis/BullMQ、邮件或独立 worker 时，它们必须是可替换的 Nest provider：在 `compile()` 前用实际注入 token 的 `overrideProvider(...).useValue(...)` 替换外部队列、worker 启动器、邮件适配器；mock 要实现业务调用的方法，例如返回已完成 Promise 的 `add`、`addBulk`、`close`。保留真实数据库事务与 Notification 写入，只替换外部副作用。不能只删除 worker 模块却留下未满足的注入依赖，也不能在模块文件顶层 `new Worker(...)`，否则仅导入文件就可能连接 Redis、消费作业或使 Jest 无法退出。下面代码对应已接入 `NotificationsModule` 的情况；尚未接入者保持原来的 `Test.createTestingModule({ imports: [AppModule] }).compile()` 即可。

```ts
// api/test/board.e2e-spec.ts，beforeAll 中替换外部 provider
import { getQueueToken } from '@nestjs/bullmq';
import { Test } from '@nestjs/testing';
import { NotificationsProcessor } from '../src/notifications/notifications.processor';

const fakeQueue = {
  add: async () => undefined,
  addBulk: async () => [],
  close: async () => undefined,
};

moduleRef = await Test.createTestingModule({ imports: [AppModule] })
  .overrideProvider(getQueueToken('notifications'))
  .useValue(fakeQueue)
  // @Processor 在模块初始化时会启动 Worker 连 Redis，连处理器一起替换
  .overrideProvider(NotificationsProcessor)
  .useValue({ process: async () => undefined })
  .compile();
```

若 `NotificationsService` 还注入了别的外部适配器，按同样方式逐个 `overrideProvider`；`getQueueToken('notifications')` 必须与 `BullModule.registerQueue({ name: 'notifications' })` 的名字一致。替换后测试验证的是业务规则与权限，不要宣称它验证了真实队列投递。

第 51 天的 Socket.IO Gateway 不需要额外 `listen()`：`app.init()` 会初始化 Gateway，Supertest 使用 `app.getHttpServer()` 发 HTTP 请求，临时端口由工具管理。不启动第二个 HTTP 服务；本测试也不覆盖 Socket 房间授权或事件送达。必须重设第 47 天的全局前缀和 `ValidationPipe`，因为测试导入 `AppModule` 不会执行 `main.ts`。

```ts
import { randomBytes, randomUUID } from 'node:crypto';
import { INestApplication, ValidationPipe } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { Test, TestingModule } from '@nestjs/testing';
import request = require('supertest');
import { AppModule } from '../src/app.module';
import { PrismaService } from '../src/prisma.service';

function requireTestDatabase(): string {
  if (process.env.NODE_ENV !== 'test') {
    throw new Error('拒绝运行：NODE_ENV 必须为 test');
  }
  const raw = process.env.DATABASE_URL;
  if (!raw) throw new Error('缺少 DATABASE_URL；请使用 --env-file=.env.test');
  const url = new URL(raw);
  // 对解码后的整个库名做校验，不能仅检查 URL 中是否包含 test。
  if (!['postgres:', 'postgresql:'].includes(url.protocol)
      || !/^\/[A-Za-z0-9_]+_test$/.test(decodeURIComponent(url.pathname))) {
    throw new Error('拒绝运行或清理：PostgreSQL 数据库名称必须以 _test 结尾');
  }
  return raw;
}

// 在编译 Nest 模块、连接 Prisma 和写入数据之前检查；清理前还会复查。
const testDatabaseUrl = requireTestDatabase();
const secret = process.env.JWT_SECRET;
if (!secret || secret.startsWith('REPLACE_') || Buffer.byteLength(secret) < 32) {
  throw new Error('请先在 .env.test 设置自己生成的独立测试 JWT_SECRET');
}

jest.setTimeout(60_000);

describe('看板权限与 CRUD（HTTP + PostgreSQL）', () => {
  let moduleRef: TestingModule | undefined;
  let app: INestApplication | undefined;
  let db: PrismaService | undefined;

  // 每次执行都不同；不借用课上已有的 lin / zhou / yi 账号。
  const runId = randomUUID();
  const password = randomBytes(24).toString('hex');
  const emails = {
    owner: `d56-owner-${runId}@example.test`,
    member: `d56-member-${runId}@example.test`,
    other: `d56-other-${runId}@example.test`,
  };
  const teamNames = [`d56-a-${runId}`, `d56-b-${runId}`];
  const userIds: Record<'owner' | 'member' | 'other', string> = {
    owner: '', member: '', other: '',
  };
  let ownerToken = '';
  let memberToken = '';
  let otherTeamToken = '';
  let teamId = '';
  let otherTeamId = '';
  let projectId = '';
  let otherProjectId = '';

  // HTTP 工厂在 app.init() 之后才调用。
  const http = () => request(app!.getHttpServer());
  const auth = (token: string) => `Bearer ${token}`;
  const projectsPath = () => `/api/teams/${teamId}/projects`;
  const tasksPath = () => `${projectsPath()}/${projectId}/tasks`;

  async function registerAndLogin(role: keyof typeof emails): Promise<string> {
    const registered = await http().post('/api/auth/register')
      .send({ email: emails[role], password }).expect(201);
    expect(registered.body).toEqual({ id: expect.any(String), email: emails[role] });
    userIds[role] = registered.body.id;

    const loggedIn = await http().post('/api/auth/login')
      .send({ email: emails[role], password }).expect(200);
    expect(loggedIn.body.accessToken).toEqual(expect.any(String));
    expect(loggedIn.body.accessToken.length).toBeGreaterThan(0);
    return loggedIn.body.accessToken;
  }

  async function createTask(title: string) {
    const response = await http().post(tasksPath())
      .set('Authorization', auth(ownerToken)).send({ title }).expect(201);
    expect(response.body).toEqual({
      id: expect.any(String), title, status: 'todo', teamId, projectId,
    });
    return response.body as {
      id: string; title: string; status: string; teamId: string; projectId: string;
    };
  }

  beforeAll(async () => {
    moduleRef = await Test.createTestingModule({ imports: [AppModule] }).compile();
    // 已接入 NotificationsModule 时，按上一节示例在 compile() 前替换队列与处理器。
    db = moduleRef.get(PrismaService);
    if (moduleRef.get(ConfigService).get<string>('DATABASE_URL') !== testDatabaseUrl) {
      throw new Error('Nest 配置与已校验的测试库 URL 不一致');
    }
    app = moduleRef.createNestApplication();
    app.setGlobalPrefix('api');
    app.useGlobalPipes(new ValidationPipe({
      whitelist: true,
      forbidNonWhitelisted: true,
      transform: true,
    }));
    await app.init();

    // 顺序创建，避免初始化失败时还有并发写入未结束。
    ownerToken = await registerAndLogin('owner');
    memberToken = await registerAndLogin('member');
    otherTeamToken = await registerAndLogin('other');

    const ownerTeam = await http().post('/api/teams')
      .set('Authorization', auth(ownerToken)).send({ name: teamNames[0] }).expect(201);
    expect(ownerTeam.body).toMatchObject({ id: expect.any(String), name: teamNames[0] });
    teamId = ownerTeam.body.id;

    const otherTeam = await http().post('/api/teams')
      .set('Authorization', auth(otherTeamToken)).send({ name: teamNames[1] }).expect(201);
    expect(otherTeam.body).toMatchObject({ id: expect.any(String), name: teamNames[1] });
    otherTeamId = otherTeam.body.id;

    const member = await http().post(`/api/teams/${teamId}/members`)
      .set('Authorization', auth(ownerToken)).send({ email: emails.member }).expect(201);
    expect(member.body).toMatchObject({ teamId, userId: userIds.member, role: 'member' });
    expect(await db.membership.findUnique({
      where: { teamId_userId: { teamId, userId: userIds.owner } },
    })).toMatchObject({ role: 'owner' });

    const project = await http().post(projectsPath())
      .set('Authorization', auth(ownerToken)).send({ name: '甲队回归项目' }).expect(201);
    expect(project.body).toMatchObject({ id: expect.any(String), teamId });
    projectId = project.body.id;

    const otherProject = await http().post(`/api/teams/${otherTeamId}/projects`)
      .set('Authorization', auth(otherTeamToken)).send({ name: '乙队回归项目' }).expect(201);
    expect(otherProject.body).toMatchObject({ id: expect.any(String), teamId: otherTeamId });
    otherProjectId = otherProject.body.id;
  });

  it('合法成员完成任务新增、列表、读取、移动、删除，结果实际落库', async () => {
    const task = await createTask('回归检查');
    const path = `${tasksPath()}/${task.id}`;
    const listed = await http().get(tasksPath())
      .set('Authorization', auth(memberToken)).expect(200);
    expect(listed.body.items).toEqual(expect.arrayContaining([task]));
    const read = await http().get(path).set('Authorization', auth(memberToken)).expect(200);
    expect(read.body).toEqual(task);

    const moved = await http().patch(path).set('Authorization', auth(memberToken))
      .send({ title: '成员已移动', status: 'doing' }).expect(200);
    expect(moved.body).toEqual({ ...task, title: '成员已移动', status: 'doing' });
    expect(await db!.task.findUnique({ where: { id: task.id } }))
      .toMatchObject({ teamId, projectId, title: '成员已移动', status: 'doing' });
    const reread = await http().get(path).set('Authorization', auth(ownerToken)).expect(200);
    expect(reread.body).toEqual(moved.body);

    const removed = await http().delete(path).set('Authorization', auth(memberToken)).expect(204);
    expect(removed.text).toBe('');
    expect(await db!.task.findUnique({ where: { id: task.id } })).toBeNull();
    await http().get(path).set('Authorization', auth(ownerToken)).expect(404);
  });

  it('项目可以创建、列表、读取、改名并在无任务时删除', async () => {
    const created = await http().post(projectsPath()).set('Authorization', auth(ownerToken))
      .send({ name: '空项目' }).expect(201);
    const id = created.body.id;
    expect(created.body).toMatchObject({ id: expect.any(String), teamId, name: '空项目' });
    const path = `${projectsPath()}/${id}`;
    const list = await http().get(projectsPath()).set('Authorization', auth(memberToken)).expect(200);
    expect(list.body).toEqual(expect.arrayContaining([created.body]));
    const read = await http().get(path).set('Authorization', auth(memberToken)).expect(200);
    expect(read.body).toEqual(created.body);
    const renamed = await http().patch(path).set('Authorization', auth(ownerToken))
      .send({ name: '已改名' }).expect(200);
    expect(renamed.body).toMatchObject({ id, teamId, name: '已改名' });
    expect(await db!.project.findUnique({ where: { id } })).toMatchObject({ name: '已改名' });
    const deleted = await http().delete(path).set('Authorization', auth(ownerToken)).expect(204);
    expect(deleted.text).toBe('');
    expect(await db!.project.findUnique({ where: { id } })).toBeNull();
    await http().get(path).set('Authorization', auth(ownerToken)).expect(404);
  });

  it('未登录的任务读写一律 401', async () => {
    const task = await createTask('未登录保护');
    const path = `${tasksPath()}/${task.id}`;
    await http().get(tasksPath()).expect(401);
    await http().get(path).expect(401);
    await http().post(tasksPath()).send({ title: '不能创建' }).expect(401);
    await http().patch(path).send({ status: 'done' }).expect(401);
    await http().delete(path).expect(401);
    expect(await db!.task.findUnique({ where: { id: task.id } })).toMatchObject({ status: 'todo' });
  });

  it('乙队用户访问甲队任务的读写一律 403，甲队成员不能用甲队路径访问乙队项目', async () => {
    const task = await createTask('团队隔离');
    const path = `${tasksPath()}/${task.id}`;
    await http().get(tasksPath()).set('Authorization', auth(otherTeamToken)).expect(403);
    await http().get(path).set('Authorization', auth(otherTeamToken)).expect(403);
    await http().post(tasksPath()).set('Authorization', auth(otherTeamToken))
      .send({ title: '越权创建' }).expect(403);
    await http().patch(path).set('Authorization', auth(otherTeamToken))
      .send({ status: 'done' }).expect(403);
    await http().delete(path).set('Authorization', auth(otherTeamToken)).expect(403);
    // 有甲队身份也不能绕过项目所属团队条件；这一层应返回 404。
    await http().get(`${projectsPath()}/${otherProjectId}`)
      .set('Authorization', auth(ownerToken)).expect(404);
    await http().post(`${projectsPath()}/${otherProjectId}/tasks`)
      .set('Authorization', auth(ownerToken)).send({ title: '错配项目' }).expect(404);
    expect(await db!.task.findUnique({ where: { id: task.id } }))
      .toMatchObject({ teamId, projectId, status: 'todo' });
  });

  it('普通成员不能加人，所有者重复添加成员得到 409', async () => {
    await http().post(`/api/teams/${teamId}/members`)
      .set('Authorization', auth(memberToken)).send({ email: emails.other }).expect(403);
    expect(await db!.membership.findUnique({
      where: { teamId_userId: { teamId, userId: userIds.other } },
    })).toBeNull();
    await http().post(`/api/teams/${teamId}/members`)
      .set('Authorization', auth(ownerToken)).send({ email: emails.member }).expect(409);
    expect(await db!.membership.count({ where: { teamId, userId: userIds.member } })).toBe(1);
  });

  it('空白标题、额外字段、非法状态、null 与空 PATCH 得到 400', async () => {
    const count = await db!.task.count({ where: { teamId, projectId } });
    for (const body of [{ title: '' }, { title: '   ' }, { title: '测试', admin: true }]) {
      await http().post(tasksPath()).set('Authorization', auth(ownerToken)).send(body).expect(400);
    }
    expect(await db!.task.count({ where: { teamId, projectId } })).toBe(count);
    const task = await createTask('输入校验');
    for (const body of [{ status: 'invalid' }, { status: null }, {}]) {
      await http().patch(`${tasksPath()}/${task.id}`)
        .set('Authorization', auth(memberToken)).send(body).expect(400);
    }
    expect(await db!.task.findUnique({ where: { id: task.id } })).toMatchObject({ status: 'todo' });
  });

  it('重复注册、删除有任务的项目得到 409，原记录仍存在', async () => {
    await http().post('/api/auth/register').send({ email: emails.owner, password }).expect(409);
    expect(await db!.user.count({ where: { email: emails.owner } })).toBe(1);
    const task = await createTask('阻止删除项目');
    await http().delete(`${projectsPath()}/${projectId}`)
      .set('Authorization', auth(ownerToken)).expect(409);
    expect(await db!.project.findUnique({ where: { id: projectId } })).toMatchObject({ teamId });
    expect(await db!.task.findUnique({ where: { id: task.id } })).not.toBeNull();
  });

  afterAll(async () => {
    try {
      // 即使 beforeAll 中途失败，也只按本次随机且精确的标记回收已提交记录。
      // 清理期间不允许环境或 Nest 配置切换到另一条连接串。
      if (requireTestDatabase() !== testDatabaseUrl) {
        throw new Error('测试库 URL 已改变，拒绝清理');
      }
      if (db && moduleRef) {
        if (moduleRef.get(ConfigService).get<string>('DATABASE_URL') !== testDatabaseUrl) {
          throw new Error('Nest 数据库配置已改变，拒绝清理');
        }
        const users = await db.user.findMany({
          where: { email: { in: Object.values(emails) } }, select: { id: true },
        });
        const teams = await db.team.findMany({
          where: { name: { in: teamNames } }, select: { id: true },
        });
        const ids = teams.map((team) => team.id);
        const usersToDelete = users.map((user) => user.id);
        // 一次事务，严格按依赖顺序；没有无条件 deleteMany / TRUNCATE。
        await db.$transaction(async (tx) => {
          await tx.notification.deleteMany({ where: { OR: [
            { teamId: { in: ids } }, { userId: { in: usersToDelete } },
          ] } });
          await tx.task.deleteMany({ where: { teamId: { in: ids } } });
          await tx.project.deleteMany({ where: { teamId: { in: ids } } });
          await tx.membership.deleteMany({ where: { teamId: { in: ids } } });
          await tx.team.deleteMany({ where: { id: { in: ids } } });
          await tx.user.deleteMany({ where: { id: { in: usersToDelete } } });
        });
      }
    } finally {
      // 清理报错也要释放 HTTP / Gateway / Prisma，且让错误使测试失败。
      if (app) await app.close();
      else if (moduleRef) await moduleRef.close();
    }
  });
});
```

这里的清理限定为三个本次生成的完整邮箱和两个本次生成的完整团队名，再由查询结果取得真实 ID，不按 `d56-` 前缀批量删，也不清空整个测试库。任务与项目都限定在本次团队，顺序为 Notification → Task → Project → Membership → Team → User。外部 worker 必须在测试中替换，避免清理同时还有消费者回写数据。进程被强制终止时 `afterAll` 无法保证执行，残留数据可按这一次完整随机标记人工核对，不能改成全库清理。库名后缀是防误操作门槛，仍需独立测试库和最小权限；PrismaService 应沿用第 47 天的 `DATABASE_URL`，若自行覆写 datasource，必须同步校验实际连接目标。

### 4. 修正脚手架测试，再运行

第 47 天已给 `AppController` 新增 Prisma 构造依赖。Nest 脚手架的 `api/src/app.controller.spec.ts` 若只提供 `AppService`，会在测试编译时失败。删除不再适用的模板断言，或保留控制器测试并提供 `useValue` mock；不要通过导入真实 `AppModule` 给单测补数据库。若当前构造器仍是 `AppService` + `PrismaService`，可以用以下完整测试替换模板：

```ts
import { Test } from '@nestjs/testing';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { PrismaService } from './prisma.service';

describe('AppController（单元测试）', () => {
  it('health 在数据库探测成功后返回 ok', async () => {
    const queryRaw = jest.fn().mockResolvedValue([{ value: 1 }]);
    const moduleRef = await Test.createTestingModule({
      controllers: [AppController],
      providers: [
        { provide: AppService, useValue: { getHello: jest.fn() } },
        { provide: PrismaService, useValue: { $queryRaw: queryRaw } },
      ],
    }).compile();
    try {
      await expect(moduleRef.get(AppController).health()).resolves.toEqual({ ok: true });
      expect(queryRaw).toHaveBeenCalledTimes(1);
    } finally {
      await moduleRef.close();
    }
  });
});
```

脚手架 `api/test/app.e2e-spec.ts` 的 `Hello World!` 模板也应删除或改成项目实际契约，避免它仍导入真实 AppModule 却没有测试库检查、前缀或清理。以下 e2e 命令只选择 `board.e2e-spec.ts`；将来扩大运行范围时，每个连接数据库的套件都要采用相同环境校验和清理约束。

仍在 `api` 的同一终端运行，使用脚手架已有 `package.json` 的 Jest 单测配置和 `test/jest-e2e.json`；若你已改配置路径，按实际文件调整。

```bash
NODE_ENV=test node --env-file=.env.test ./node_modules/jest/bin/jest.js --config=package.json --runInBand
NODE_ENV=test node --env-file=.env.test ./node_modules/jest/bin/jest.js --config=./test/jest-e2e.json --runInBand --runTestsByPath test/board.e2e-spec.ts
```

不要以 `--forceExit` 掩盖 Prisma、Gateway 或队列连接未释放。预期单测包含 `TeamAccess` 的三项断言用例以及已修正的控制器测试，HTTP 套件为 `PASS test/board.e2e-spec.ts`、7 项测试通过，进程正常退出；连续重跑不会冲突，测试后没有本次用户和团队。实际其他单测数量以项目为准。数据库未就绪、迁移缺失或业务实现不符时应失败，先查第一条错误，不放宽状态码。

本章仅提供代码与预期结果，未连接 PostgreSQL 实测，也未执行安装、迁移或 Jest；上述 `PASS` 不是本环境的实测输出。

## 练习

从空的独立测试库迁移后重跑两次，记录真实命令和脱敏输出。故意让成员判断或任务查询漏掉团队条件，确认对应测试能报错，再恢复实现。补一条「只改 title 时保留旧 status」的回归测试，并用 HTTP 重读与数据库断言一起验证。

## 参考答案与验收

未登录读写为 `401`；乙队访问甲队任务、普通成员加人为 `403`；有效团队身份搭配其他团队项目为 `404`；输入错误为 `400`；重复邮箱、重复成员与删除非空项目为 `409`。合法任务新增为 `201`、初始 `todo`，成员更新为 `200`、数据库变为 `doing`，删除为 `204` 且记录消失。环境在入口显式加载，token 与 ID 在 `beforeAll` 建立，测试库名称必须以 `_test` 结尾，`afterAll` 仅删除本次数据且无论清理结果如何都关闭应用。HTTP 测试不代表 worker 交付或 WebSocket 房间权限已验证。

## AI 搭档

先自己列期望状态码再问。「请以测试审查者身份检查我的完整测试：环境是否在入口加载、beforeAll 是否真正注册和登录、token 与 ID 是否来自 HTTP、是否验证持久化、cleanup 是否只影响本次数据、连接是否关闭。一次指出一个缺口，让我解释为什么应是 401、403、404、409 或 400。只接收脱敏代码和输出，不上传令牌、密码、连接串或真实数据。」

# 第 57 天：用数据定位看板性能瓶颈

原课：<https://xiguadev.com/node-60days/day-57>

## 今日先学

性能优化要先测量再改。先固定接口、数据量、并发数、Node 版本、PG16 状态和 Redis 状态，记录 p50、p95、错误率及数据库查询时间。看板列表的常见问题是没有联合索引、一次取太多列、偏移量很大，或每个任务再查一次关联数据。不要把浏览器感觉或一次请求耗时当成结论，也不要对生产系统做压力实验。

## 跟做

为测试库生成合成数据，例如 10 个团队、每队 5 个项目、每项目 2,000 条任务。使用项目已有 seed 脚本或 `prisma.task.createMany`，标题全部写成 `perf-demo-` 前缀，测试后删除。先在 `api` 运行一条本机查询计划；只对测试库使用 `EXPLAIN (ANALYZE, BUFFERS)`，因为 `ANALYZE` 会真正执行语句。

```sql
-- 本机测试数据库：不要粘到生产库
EXPLAIN (ANALYZE, BUFFERS)
SELECT "id", "title", "status", "teamId", "projectId"
FROM "Task"
WHERE "teamId" = '合成团队ID' AND "projectId" = '合成项目ID' AND "status" = 'todo'
ORDER BY "createdAt" DESC, "id" DESC
LIMIT 20 OFFSET 0;
```

如果计划显示大量扫描，再在 `schema.prisma` 的 `Task` 模型加入与查询顺序匹配的索引，并生成迁移。示意片段放在模型的 `@@index` 附近，不要另建第二个 Task 模型：

```prisma
// api/prisma/schema.prisma 的 Task 模型内
@@index([teamId, projectId, status, createdAt, id])
```

执行本机 `npx prisma migrate dev --name task_board_list_index`，重新跑同一 SQL，保存优化前后计划。然后用已有测试账号运行受控基准：`npx autocannon -c 5 -d 10 -H "Authorization: Bearer $TOKEN" "http://127.0.0.1:3000/api/teams/<合成团队ID>/projects/<合成项目ID>/tasks?status=todo&limit=20&offset=0"`。这只对本机合成数据执行；不要用真实令牌、真实 URL 或云端地址。

如果 p95 下降但数据库缓冲读取上升，继续查看计划，不要宣称所有场景都变快。缓存统计或列表时必须有明确 key，例如 `teamId:projectId:status:offset:limit`，任务创建、移动、删除和项目删除都要失效相关 key；缓存未命中或 Redis 故障时仍能回源 PG。先用正确索引和分页降低复杂度，再评估缓存，避免缓存旧权限数据。

## 练习

固定同一条请求、5 并发、10 秒和同一批合成数据，记录优化前后 p50、p95、错误数、计划中的扫描方式。把 `offset=10000` 与第一页分别测一次，并说明为什么偏移分页越深越慢。删除测试数据或销毁本机临时数据库。

## 参考答案与验收

报告至少写清环境、数据量、接口、请求参数和测量工具。优化后应能解释计划发生了什么变化；不要求特定毫秒数。错误率为零，结果仍只含当前团队任务。不能以一次偶然较快就认定优化成功，也不能在没有失效策略时加入缓存。

## AI 搭档

先贴脱敏指标表再问。「请只根据环境、数据量、p50、p95、错误率和 EXPLAIN 摘要，帮我提出三个可验证假设；每次让我先选一个实验，不直接改代码。请提醒我不要对生产地址压测，也不要提交令牌、连接串或客户数据。」

# 第 58 天：把协作任务板画成可扩展的系统

原课：<https://xiguadev.com/node-60days/day-58>

## 今日先学

系统设计先从边界和不变量开始。协作任务板的核心不变量是：任务属于一个项目，项目属于一个团队，操作者必须是该团队成员；写成功后，列表最终能读到新状态。Nest API 是无状态应用，PG16 保存事务数据，Redis/BullMQ 处理可重试的通知工作，React 静态资源由 Web 层发布。实时网关只是加速刷新，不承担唯一数据来源。

## 跟做

在 `docs` 之外的现有 `README.md` 增加一张文字架构图（不要新建额外文档文件）：

```text
浏览器 React
  | HTTPS / REST + WebSocket 提示
Web/API Nest 11（当前单实例；多实例前须先接 Redis adapter）
  | Prisma 6.19.x       | BullMQ
PostgreSQL 16（事实数据） Redis（队列与短期状态）
```

图里的「多实例」是目标态不是当前实现：第 51 天说明过多实例必须接 `@socket.io/redis-adapter` 才能跨实例广播房间事件，本文没有给出 adapter 代码，因此当前按单实例理解，扩容前要先补 adapter 与共享 Redis 连接。写一条请求路径：小周移动任务时，API 验证 JWT 得到 `sub`，TeamGuard 查询 Membership，事务更新 Task 并写 Notification，提交后投递 job；网关通知已加入房间的成员；页面收到事件后重新 GET 列表。任一步重试都不应让任务移动两次，服务可用时查询结果必须以 PG 为准。

接着写容量假设：1,000 个团队、每队 50 人、每项目 100,000 任务、峰值 100 次列表请求/秒。用它讨论索引、连接池、读副本、队列积压和分页策略，而不是只说「上 Kubernetes」。长列表可改用游标分页，接口响应带 `nextCursor`；迁移期间保持旧的 `offset` 接口，待前端切换后再下线。通知以 Outbox 表和唯一事件键确保数据库提交与后续投递之间可恢复；若 Redis 中断，补偿扫描器重新排队。

画三个故障场景：PG 不可读时 readiness 失败且只停止导流，不能假装空看板；Redis 不可用时任务和通知列仍按事务保存，恢复后补发；WebSocket 断线时页面重新取得快照。再写安全边界：TLS、秘密注入、最小角色、团队条件必须出现在每个查询，日志只记录请求 ID 与状态码，不记录密码、令牌和客户内容。

## 练习

用一页 README 文字回答：如何水平扩展 API、如何避免跨团队读写、如何处理通知重复、如何把列表从 offset 换成 cursor、哪个指标触发告警。为每个选择写一个代价，例如一致性、复杂度、成本或延迟。

## 参考答案与验收

答案应把 PG 定为事实源，把 Redis 定为可重建的加速/队列组件；所有资源查询带团队和项目条件；通知通过唯一键幂等；断线从 HTTP 快照恢复；健康检查区分存活和就绪。架构图、容量假设、故障处理和取舍都具体到本项目，不能只列技术名词。

## AI 搭档

先自己画架构再问。「请以面试官身份给我一个故障场景，一次只问一个追问：数据在哪、谁负责重试、用户看到什么、如何恢复。等我回答后指出遗漏的团队隔离或一致性条件，不替我完成整张设计图。只使用合成容量数据。」

# 第 59 天：把项目整理成作品、简历和面试答案

原课：<https://xiguadev.com/node-60days/day-59>

## 今日先学

作品展示的是可验证的工程判断，不是堆砌依赖名。围绕协作任务板准备四类材料：运行截图或本机录屏、脱敏 README、接口和数据模型图、测试与性能结果。README 要说明 Node 22 / 24 / 26 LTS、Nest 11、PG16、Prisma 6.19.x、Redis/BullMQ 和 React+Vite+TS，注明哪些命令只在本机执行、哪些是部署建议，禁止上传 `.env`、JWT、数据库导出或真实客户数据。

## 跟做

在现有项目 README 的末尾增加「作品说明」段，不新建宣传文档。用事实写三条简历子弹：动作、技术和结果必须可追溯。示例只作改写模板，不要谎称已经云端部署：

```text
协作任务板 SaaS：使用 Nest 11、Prisma 6.19.x 与 PostgreSQL 16 建立团队隔离的项目/任务 API，按 teamId/projectId 约束查询并用 401/403/404/409 回归测试验证权限。
实现 React + Vite + TypeScript 登录后看板流程，以 HTTP 快照为事实源、WebSocket 仅作刷新提示，并用 BullMQ 处理可重试通知。
在本机合成数据上用 EXPLAIN 和 autocannon 比较复合索引前后 p95，记录环境、数据量、错误率及取舍；未执行云端部署的部分明确标注为部署准备。
```

准备 90 秒自我介绍：先说用户问题，再说纵向链路，然后讲一个取舍和一个失败复盘。面试题可按以下顺序练习：为什么团队条件不能只在前端做；JWT 与权限查询怎样分工；WebSocket 漏事件怎么办；事务提交与队列投递如何恢复；为什么先测 p95；PG 索引如何证明有效。回答时先给结论，再给请求路径、数据证据和限制。

本机执行 `npm test -- --runInBand`、`npm run build`，把通过输出和性能表中的秘密删除后保存。若没有真实部署，就写「未执行部署，已完成本机 build 与部署清单」，不要用假 URL 冒充上线。简历上的数字必须来自今天记录，不能把估计的用户量写成线上成绩。

## 练习

录下或写下 90 秒介绍，再用 STAR 写一次跨团队访问被 `403` 的排错故事：情境、任务、行动、结果。列出三项尚未完成的生产工作，并说明下一步验证方法。让同学只根据 README 重建本机测试，不给他们秘密。

## 参考答案与验收

作品材料能让别人复现登录、选择团队、读列表、新增任务和错误状态；简历不夸大部署和性能；面试回答提到服务端授权、数据库事实源、幂等与指标。README 不含秘密、真实客户数据和不可访问的私有链接。90 秒内能说清一个取舍和一个限制。

## AI 搭档

先写自己的答案再问。「请模拟 Node 全栈面试，每次问一个和协作任务板相关的问题，等待我的回答后按正确性、证据、边界三项各打分；只指出一处最值得改进的地方，不代写答案。提醒我删除令牌、连接串、密码和真实客户信息。」

# 第 60 天：验收、复盘并规划下一段学习

原课：<https://xiguadev.com/node-60days/day-60>

## 今日先学

复盘不是重新阅读全部课程，而是用一条可重复的验收路径证明系统仍然成立。最终项目的最小纵向切片是：注册并登录，创建团队和项目，邀请成员，成员读取同团队任务，新增与移动任务，看板按状态列出，通知可重试，前端呈现成功、空和错误状态。然后用权限、测试、性能和交付记录说明哪些已完成、哪些只是设计。

## 跟做

在现有 README 写「最终验收记录」，保留日期、Node 版本、依赖版本、本机数据库名称（不要写密码）、命令和结果。按下面顺序在独立测试库重跑；每一步记录 HTTP 状态和可观察输出：

```text
1. prisma migrate deploy + seed（配套包 `60天配套/board-api/prisma/seed.mjs`）：成功，团队/项目/任务演示数据就绪；账号仍用注册接口创建
2. 假账号登录：200，得到短期 accessToken
3. 甲队所有者创建项目和任务：201，任务为 todo
4. 甲队成员列表读取并移动任务：200，状态为 doing
5. 乙队成员读取甲队：403；未登录：401
6. 无效标题：400；不存在资源：404；重复成员/邮箱：409
7. stats 返回 todo/doing/done；前端显示列表、空状态、错误状态
8. 测试通过；本机 build 通过；性能报告含 p95 和测试条件
```

验收后做一次复盘表：保留了什么、删除了什么、哪个假设错了、哪个指标证明改动有效、下一步是什么。下一阶段可以选一条：把 offset 分页迁移成 cursor、增加审计日志、实现 Outbox 补偿、加 OAuth 或完善可观测性；每条都先写用户价值、数据迁移和回滚方案。不要同时开五条大功能。

最后做安全收尾：停止本机服务，删除临时合成数据和可用令牌，检查 `.env`、数据库 dump、截图和录屏没有秘密；确认日志不含密码和完整 Authorization 头。部署仍只是一份准备清单时，就如实写明没有云端验证。把失败的测试保留为回归案例，而不是删掉让报告变绿。

## 练习

从空测试库完成一次验收，故意让一条权限断言失败，再修复并重跑。写 300 字复盘，包含一个技术取舍、一个可观测证据、一个未完成风险和下一步实验。最后向同伴演示「登录后列表/新增/错误」完整流程。

## 参考答案与验收

最终记录覆盖数据准备、认证、团队隔离、CRUD、看板、通知、前端、测试与性能；每个失败状态都有触发输入和预期响应。复盘不把「未部署」写成「已上线」，不把本机基准写成生产指标。秘密检查通过，测试可从干净库重跑，下一步只有一至两项且可测量。完成这些即达到本 60 天项目的学习验收标准。

## AI 搭档

先独立完成验收和复盘再问。「请作为结课评审，按需求、实现、权限、测试、性能、交付五项逐项提问，每次只问一个可验证问题；我的回答后指出证据是否足够和下一步最小实验。不要替我润色成虚假成果，也不要让我上传秘密、真实客户数据、令牌或数据库导出。」


