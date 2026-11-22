#!/usr/bin/env python3
"""源码快照静态检查（零第三方依赖，CI 可直接运行）。

检查 blog-api / board-api / day54-web 三个快照：
- 目录与关键文件齐备
- 相对 import 都能解析到快照内的文件（避免 tsc 的 Cannot find module）
- 源码与说明里没有繁体字残留
- 关键实现已合入（列表 / 统计 / 网关 / Socket.IO 代理）
"""
import os
import posixpath
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZIP = os.path.join(ROOT, "Node.js_AI全栈60天学习包.zip")
TRAD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "trad_chars.txt")

failures = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("  " + detail if detail else ""))
    if not ok:
        failures.append(name + (": " + detail if detail else ""))


def main():
    with open(TRAD, encoding="utf-8") as f:
        trad = set(f.read().strip())
    z = zipfile.ZipFile(ZIP)
    names = set(z.namelist())

    roots = ["60天配套/blog-api/", "60天配套/board-api/", "60天配套/day54-web/"]
    for r in roots:
        check("snapshot " + r, any(n.startswith(r) for n in names))

    required = [
        "60天配套/blog-api/src/posts/post.ts",
        "60天配套/blog-api/src/uploads/uploads.controller.ts",
        "60天配套/blog-api/src/uploads/upload.validation.ts",
        "60天配套/blog-api/src/uploads/uploads.service.ts",
        "60天配套/board-api/src/projects.ts",
        "60天配套/board-api/src/board.gateway.ts",
        "60天配套/day54-web/vite.config.ts",
        "60天配套/day54-web/src/api.ts",
        "60天配套/docker-compose.prod.yml",
    ]
    for n in required:
        check("required " + n, n in names)

    # 1) 相对 import 完整性
    missing = []
    for n in sorted(names):
        if not n.endswith((".ts", ".tsx")) or not any(n.startswith(r) for r in roots):
            continue
        src = z.read(n).decode("utf-8")
        for m in re.finditer(r"(?:from|import)\s*\(?\s*['\"](\.[^'\"]+)['\"]", src):
            base = posixpath.normpath(posixpath.join(posixpath.dirname(n), m.group(1)))
            candidates = [base + ext for ext in (".ts", ".tsx", ".js", ".mjs", ".json", ".css", "")]
            candidates += [posixpath.join(base, "index" + ext) for ext in (".ts", ".tsx")]
            if not any(c in names for c in candidates):
                missing.append(n + " -> " + m.group(1))
    check("relative imports resolve", not missing, str(missing[:6]))

    # 2) 繁体字扫描（源码与说明）
    hits = []
    for n in sorted(names):
        if not n.startswith("60天配套/") or not n.endswith((".ts", ".tsx", ".md", ".mjs", ".yml", ".yaml", ".json")):
            continue
        text = z.read(n).decode("utf-8")
        found = sorted({ch for ch in text if ch in trad})
        if found:
            hits.append((n, "".join(found[:20])))
    check("no traditional chars in snapshots", not hits, str(hits[:6]))

    # 3) 关键实现已合入
    if "60天配套/board-api/src/projects.ts" in names:
        p = z.read("60天配套/board-api/src/projects.ts").decode("utf-8")
        check("projects.ts has listTasks / taskStats / stats route",
              all(k in p for k in ("listTasks", "taskStats", "@Get('stats')", "BoardGateway")))
        check("projects.ts declares static routes before :taskId",
              p.find("@Get('stats')") < p.find("@Get(':taskId')"))
    if "60天配套/day54-web/vite.config.ts" in names:
        v = z.read("60天配套/day54-web/vite.config.ts").decode("utf-8")
        check("vite proxy covers /socket.io", "'/socket.io'" in v and "'/board'" not in v)
    if "60天配套/day54-web/src/api.ts" in names:
        a = z.read("60天配套/day54-web/src/api.ts").decode("utf-8")
        check("api.ts uses simplified Chinese and explicit path",
              "請求失敗" not in a and "path: '/socket.io'" in a)

    print("\n%d checks failed" % len(failures))
    for f in failures:
        print("  - " + f)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
