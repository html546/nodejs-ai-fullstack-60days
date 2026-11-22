#!/usr/bin/env python3
"""教程仓库一致性校验（零第三方依赖，CI 可直接运行）。

检查项对应 Review 报告第五节第 8 条：
- 60 天日号连续、无缺号/重号
- 代码围栏成对且都有语言标注
- 每天都有指向原课的 day-XX 链接且编号匹配
- 繁体字扫描（正文、离线 HTML 与 zip 内源码快照）
- 过时版本号表述
- Markdown / HTML / zip 三份正文一致
- HTML 中的 inline 占位符 / 字面加粗标记不得回归
- zip 内源码相对 import 完整性
"""
import os
import posixpath
import re
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD = os.path.join(ROOT, "Node.js_AI全栈60天教程.md")
HTML = os.path.join(ROOT, "index.html")
ZIP = os.path.join(ROOT, "Node.js_AI全栈60天学习包.zip")

failures = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("  " + detail if detail else ""))
    if not ok:
        failures.append(name + (": " + detail if detail else ""))


def norm(b):
    return b.replace(b"\r\n", b"\n")


def main():
    if not all(os.path.exists(p) for p in (MD, HTML, ZIP)):
        check("required files present", False, "缺少 md/html/zip")
        return 1

    md_b = open(MD, "rb").read()
    html_b = open(HTML, "rb").read()
    md = norm(md_b).decode("utf-8")
    html = norm(html_b).decode("utf-8")

    # 1) 日号连续
    days = [int(x) for x in re.findall(r"^# 第\s*(\d+)\s*天", md, re.M)]
    check("60 days present", len(days) == 60, "found=%d" % len(days))
    check("day numbers 1..60 continuous",
          days == list(range(1, 61)),
          "missing=%s dup=%s" % (
              sorted(set(range(1, 61)) - set(days)),
              sorted({d for d in days if days.count(d) > 1}),
          ))

    # 2) 代码围栏成对且有语言标注（只统计开围栏）
    inside = False
    open_fences = 0
    no_lang = []
    for i, line in enumerate(md.splitlines(), 1):
        if line.startswith("```"):
            if not inside:
                open_fences += 1
                if not line[3:].strip():
                    no_lang.append(i)
                inside = True
            else:
                inside = False
    check("code fences balanced", not inside and md.count("```") % 2 == 0)
    check("all code fences have language", not no_lang, "no-lang at %s" % no_lang[:5])
    check("html highlighted blocks", html.count("<pre><code") == open_fences,
          "html=%d md=%d" % (html.count("<pre><code"), open_fences))

    # 3) 每天的原课链接编号匹配
    starts = [(int(m.group(1)), i) for i, line in enumerate(md.splitlines())
              for m in [re.match(r"^# 第\s*(\d+)\s*天", line)] if m]
    starts.append((61, len(md.splitlines())))
    lines = md.splitlines()
    bad_links = []
    for k in range(60):
        d, a = starts[k]
        b = starts[k + 1][1]
        seg = "\n".join(lines[a:b])
        found = [int(x) for x in re.findall(r"xiguadev\.com/node-60days/day-(\d+)", seg)]
        if not found:
            bad_links.append((d, "NO_LINK"))
        elif any(int(x) != d for x in found):
            bad_links.append((d, found))
    check("per-day original-course links", not bad_links, str(bad_links[:6]))

    # 4) 繁体字扫描（读取 t2s 会改变的字表，命中即失败；零依赖）
    trad_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "trad_chars.txt")
    with open(trad_path, encoding="utf-8") as f:
        trad = set(f.read().strip())
    trad_hits = sorted({ch for ch in md if ch in trad})
    check("no traditional chars (md)", not trad_hits, "hits=%s" % "".join(trad_hits))
    html_hits = sorted({ch for ch in html if ch in trad})
    check("no traditional chars (html)", not html_hits, "hits=%s" % "".join(html_hits))

    # 5) 过时版本表述
    check("no stale Node version", "22.22" not in md and "24 LTS" not in md)

    # 6) 三份正文一致
    z = zipfile.ZipFile(ZIP)
    check("zip integrity", z.testzip() is None)
    names = z.namelist()
    check("zip has tutorial md", "Node.js_AI全栈60天教程.md" in names)
    check("zip has tutorial html", "Node.js_AI全栈60天教程.html" in names)
    check("zip md == root md", norm(z.read("Node.js_AI全栈60天教程.md")) == norm(md_b))
    check("zip html == root html", norm(z.read("Node.js_AI全栈60天教程.html")) == norm(html_b))

    # 7) HTML 结构
    check("html 61 day articles", html.count('<article class="day"') == 61,
          "found=%d" % html.count('<article class="day"'))
    check("html 60 answer details", html.count("<details") == 60,
          "found=%d" % html.count("<details"))

    # 8) 历史渲染缺陷不得回归
    check("no inline placeholders in html", "\x00" not in html)
    check("no literal bold markers in html", "**" not in html)
    prose = re.sub(r"<pre><code.*?</code></pre>", "", html, flags=re.S)
    check("no literal backticks outside code blocks", "`" not in prose)

    # 9) zip 内源码快照：繁体字与相对 import
    src_names = [n for n in names if n.startswith("60天配套/")
                and n.endswith((".ts", ".tsx", ".md", ".mjs", ".yml", ".yaml", ".json"))]
    zip_trad = []
    for n in src_names:
        text = z.read(n).decode("utf-8")
        found = sorted({ch for ch in text if ch in trad})
        if found:
            zip_trad.append((n, "".join(found[:12])))
    check("no traditional chars (zip sources)", not zip_trad, str(zip_trad[:5]))

    roots = ("60天配套/blog-api/", "60天配套/board-api/", "60天配套/day54-web/")
    unresolved = []
    for n in names:
        if not n.endswith((".ts", ".tsx")) or not n.startswith(roots):
            continue
        src = z.read(n).decode("utf-8")
        for m in re.finditer(r"(?:from|import)\s*\(?\s*['\"](\.[^'\"]+)['\"]", src):
            base = posixpath.normpath(posixpath.join(posixpath.dirname(n), m.group(1)))
            candidates = [base + ext for ext in (".ts", ".tsx", ".js", ".mjs", ".json", ".css", "")]
            candidates += [posixpath.join(base, "index" + ext) for ext in (".ts", ".tsx")]
            if not any(c in names for c in candidates):
                unresolved.append(n + " -> " + m.group(1))
    check("snapshot relative imports resolve", not unresolved, str(unresolved[:5]))

    print("\n%d checks failed" % len(failures))
    for f in failures:
        print("  - " + f)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
