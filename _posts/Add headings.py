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
    """按文件名中的日期找出最新的文章。"""
    posts = [(post_date(p), p) for p in posts_dir.glob("*.md")]
    posts = [(d, p) for d, p in posts if d is not None]
    if not posts:
        raise FileNotFoundError(f"在 {posts_dir} 中没有找到带日期的文章")
    return max(posts, key=lambda item: item[0])[1]


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

    # 定位 <!-- more -->，没有则处理到文件末尾。
    end = len(lines)
    for i in range(start, len(lines)):
        if lines[i].strip() == MORE_MARKER:
            end = i
            break

    changed = 0
    for i in range(start, end):
        line = lines[i]
        if line.strip() == "":          # 跳过空行
            continue
        if "####" in line:              # 已有 #### 的行不再添加
            continue
        lines[i] = "#### " + line
        changed += 1

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return changed


def main():
    latest = find_latest_post(POSTS_DIR)
    changed = add_heading_prefix(latest)
    print(f"已处理最新文章：{latest.name}")
    print(f"新增 '#### ' 前缀的行数：{changed}")


if __name__ == "__main__":
    main()
