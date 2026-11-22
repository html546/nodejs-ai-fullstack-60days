# Node.js 60 天：从零基础到 AI 协作全栈

[![教程校验与编译](https://github.com/html546/nodejs-ai-fullstack-60days/actions/workflows/ci.yml/badge.svg)](https://github.com/html546/nodejs-ai-fullstack-60days/actions/workflows/ci.yml)

一套 60 天的中文 Node.js 全栈教程，主线是**三个逐渐升级的项目**：Node 原生任务 API → NestJS + PostgreSQL/Prisma 博客 API → Nest + React 协作任务板。每天都有原课链接、学习目标、跟做代码、练习、可折叠的参考答案与验收，以及「AI 搭档」提示词；原课链接后附一段按本文技术栈重写的「原课知识精讲」，全书按原版六阶段组织，正文和侧边栏目录都有阶段边界。

## 与原版课程的关系

本仓库依据 [原版 Node.js 60 天课程](https://xiguadev.com/node-60days) 的日序与公开主题重新编写讲解、练习和项目，保留每天的原课入口便于对照。原版放在附录里的 NestJS、PostgreSQL、Prisma、认证、Redis、队列、Docker、部署与 SaaS 综合项目，在这一版进入正文；同时补充了 Next.js / tRPC / React Query 的对照实验。**它不是原版的逐段复刻**，实现细节与展开深度不同，主项目沿用 Nest REST + React，而非原版的技术选型组合。感谢原版作者提供的日序框架与主题索引。

## 三种阅读方式

| 方式 | 文件 | 说明 |
| --- | --- | --- |
| 在线 / 离线网页（推荐） | `index.html` | 双击即可离线阅读，带六阶段分组目录、标题搜索、顶部阅读进度、代码复制、折叠答案和本地学习进度（只存在当前浏览器，不上传） |
| Markdown 原稿 | `Node.js_AI全栈60天教程.md` | 完整正文，便于笔记、diff 与二次加工 |
| 离线学习包 | `Node.js_AI全栈60天学习包.zip` | 打包了网页 + Markdown + `先读我.md` + `60天配套/` 全部代码快照，解压后离线可用 |

`_headers` 用于静态托管时声明 `index.html` 与 zip 的下载/编码行为；GitHub Pages 类的静态站点直接发布仓库根目录即可。

## 目录结构

```
.
├── index.html                        # 离线阅读页（由 Markdown 渲染）
├── Node.js_AI全栈60天教程.md          # 教程正文
├── Node.js_AI全栈60天学习包.zip        # 离线学习包（内含上述两份 + 配套代码）
├── _headers                          # 静态托管响应头
├── README.md                         # 本文件
├── .github/workflows/ci.yml          # 一致性校验 + 前端编译 + 快照静态检查
└── scripts/
    ├── verify.py                    # 三份产物一致性 / 结构 / 繁简 / 链接校验
    ├── check_snapshots.py           # blog-api / board-api / day54-web 快照静态检查
    └── trad_chars.txt               # t2s 会改变的字表（繁体扫描用，零依赖）
```

学习包解压后的 `60天配套/` 含四组内容，各自 README 写明了「已收录 / 未收录」：

- `基础实验/`：第 01—05 天可直接 `node dayXX.mjs` 运行的小程序。
- `day54-web/`：第 54 天完整的 React + Vite 前端，是 CI 里唯一做真实 `npm ci && npm run build` 的工程。
- `blog-api/`：第 16—45 天博客 API 的源码快照（补齐了被 import 的 `post.ts`、`uploads.controller.ts`、`upload.validation.ts`）。
- `board-api/`：第 47—53 天协作任务板后端快照，`projects.ts` 已合入第 50 天列表、第 51 天网关广播与第 53 天统计。
- `docker-compose.prod.yml`：第 55 天本机生产发布演练用的 Compose，先做 `docker compose config` 静态核对。

> **两个后端快照不是开箱即用的工程**：它们是从教程代码块抽取的源码，不含 `nest new` 脚手架、`package.json`、`.env`、`prisma/schema.prisma` 与迁移历史，需要按正文顺序补齐后才能编译运行。

## 本地验证

零第三方依赖，Python 3.9+ 即可：

```bash
python scripts/verify.py            # 28 项：日号、围栏、外链、繁简、三份一致、60 天精讲、六阶段、HTML 结构
python scripts/check_snapshots.py   # 快照必需文件、import 完整性、繁简、关键实现
```

CI 在每次 push / PR 会跑三个 job：`verify`（一致性校验）、`build-web`（Vite 类型检查 + 生产构建）、`check-snapshots`（两个后端快照与前端快照的静态检查）。前端构建从 zip 解压源码后执行 `npm ci && npm run build`。

`scripts/verify.py` 会检查 Markdown / `index.html` / zip 内两份教程正文完全一致，以及代码围栏、60 天日号、原课链接编号、繁体字、HTML 里的历史渲染残留；`check_snapshots.py` 会检查 zip 内所有 `.ts/.tsx` 的相对 import 都能解析到本地文件，避免出现 `Cannot find module`。

## 验证范围（请如实理解）

本机实际运行过第 01—05 天基础实验、第 54 天前端的类型检查与生产构建，并对三份产物做了自动一致性校验。**PostgreSQL 迁移与端到端读写、Redis/BullMQ、OIDC、Docker 镜像、云端发布和完整 SaaS 用户流程没有全部实测**；教程里给出的是学习者应验收的预期结果，不代表这些外部服务已经跑通。仓库中的 CI 与编译脚本只覆盖静态检查与前端构建，不代替数据库/队列的集成测试。

## 使用约定

- 学习数据一律使用虚构内容；不要把 `.env`、JWT、数据库 URL、令牌或真实业务数据写进提交，也不要发给 AI。
- 正文代码分「完整文件」与「追加片段」，片段必须放进标注的位置，不能把每个代码块都当成独立程序。
- 一天是一个学习单元，可分多次完成；进度勾选只保存在当前浏览器。
