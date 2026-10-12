"""
Add headings.py
给 _posts 里最新一篇文章的摘要部分逐行加上 '#### '。

用法:
    python "Add headings.py"

    按文件名里的日期（年-月-日-书名.md）找出最新的文章，
    同一天有多篇时取最后编辑时间最晚的那篇，
    把 front matter 结束的 '---' 与 '<!-- more -->' 之间的每一行前面加上 '#### '。
    空行、已带 #### 的行不动；'<!-- more -->' 之后的笔记正文不动。

配合 Extract notes.py 使用:
    1. 跑 Extract notes.py 生成 md
    2. 手动把挑出来的摘要句子贴到 '---' 和 '<!-- more -->' 之间
    3. 跑本脚本统一加上 '#### '

注意:
    文章里没有 '<!-- more -->' 时拒绝处理（红色提示），不做任何修改。
    没有需要加 '#### ' 的行时不写文件。
"""

import os
import re
from pathlib import Path

POSTS_DIR = Path(r"C:\D\Web\An-Cheon.github.io\_posts")

# Jekyll 文件名形如 2026-6-19-Title.md
DATE_RE = re.compile(r"^(\d{4})-(\d{1,2})-(\d{1,2})-")
MORE_MARKER = "<!-- more -->"


def post_date(path):
    """从文件名解析日期，无法解析返回 None。"""
    m = DATE_RE.match(path.name)
    if not m:
        return None
    return tuple(int(g) for g in m.groups())


def find_latest_post(posts_dir):
    """按文件名中的日期找出最新的文章；同一天有多篇时取最后编辑时间最晚的。"""
    posts = [(post_date(p), p) for p in posts_dir.glob("*.md")]
    posts = [(d, p) for d, p in posts if d is not None]
    if not posts:
        raise FileNotFoundError(f"在 {posts_dir} 中没有找到带日期的文章")
    return max(posts, key=lambda item: (item[0], item[1].stat().st_mtime_ns))[1]


def add_heading_prefix(path):
    """给 front matter 与 <!-- more --> 之间、未带 #### 的行逐行加上 '#### '。"""
    lines = path.read_text(encoding="utf-8").splitlines()

    # 动态定位 front matter：首行 '---' 起，至下一个 '---' 止（内容因文章而异）。
    fm_close = None
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                fm_close = i
                break
    start = fm_close + 1 if fm_close is not None else 0

    # 定位 <!-- more -->，没有则拒绝处理（否则会把整篇正文都加上 ####）。
    end = None
    for i in range(start, len(lines)):
        if lines[i].strip() == MORE_MARKER:
            end = i
            break
    if end is None:
        return None

    changed = 0
    for i in range(start, end):
        line = lines[i]
        if line.strip() == "":          # 跳过空行
            continue
        if "####" in line:              # 已有 #### 的行不再添加
            continue
        lines[i] = "#### " + line
        changed += 1

    if changed:                         # 没有改动就不写文件，不刷新编辑时间
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return changed


def main():
    os.system('')   # 让 Windows 控制台识别 ANSI 颜色码
    latest = find_latest_post(POSTS_DIR)
    changed = add_heading_prefix(latest)
    print(f"最新文章：{latest.name}")
    if changed is None:
        print(f"\033[91mFAIL: 文章里没有 '{MORE_MARKER}'，未做任何修改。\033[0m")
    elif changed == 0:
        print("没有需要加 '#### ' 的行，文件未改动。")
    else:
        print(f"\033[92mDone: 新增 '#### ' 前缀的行数：{changed}\033[0m")


if __name__ == "__main__":
    main()
