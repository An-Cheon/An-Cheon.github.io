"""
extract_notes.py
从 Google Play Books 导出的 .docx 笔记文件中提取所有高亮/笔记。

用法:
    python extract_notes.py <input.docx> [output.txt]

依赖:
    pip install python-docx
"""

import re
from pathlib import Path
from docx import Document
from docx.oxml.ns import qn


def get_tc_texts(tbl_el) -> list[str]:
    """返回表格所有 tc 的文本列表（含空字符串）。"""
    return [
        ''.join(e.text or '' for e in tc.iter(qn('w:t')))
        for tc in tbl_el.iter(qn('w:tc'))
    ]


def extract_notes(docx_path: str, output_path: str | None = None) -> list[dict]:
    """
    解析 docx，返回笔记列表。
    每条笔记是一个 dict:
        {
            "chapter": str,   # 所属章节
            "text":    str,   # 高亮/笔记正文
            "date":    str,   # 标注日期（如 "2026年3月12日"）
            "page":    str,   # 页码（可能为空）
        }

    Play Books 导出格式说明
    -----------------------
    每条笔记对应一个独立的 <w:tbl>，内含 4 个 <w:tc>：
        tc[0]  正文 + 日期 + 页码（含超链接格式）
        tc[1]  空
        tc[2]  正文 + 日期（纯文本，无页码）
        tc[3]  页码（纯数字字符串）
    章节标题以 Heading1 / Heading2 段落形式穿插在表格之间。
    """
    doc = Document(docx_path)
    body = doc.element.body

    date_pattern = re.compile(r'(\d{4}年\d{1,2}月\d{1,2}日|[A-Z][a-z]+ \d{1,2}, \d{4})$')

    notes = []
    current_chapter = ""

    for child in body:
        tag = child.tag.split('}')[-1]

        # ── 段落：捕获章节标题 ──────────────────────────────────────────────
        if tag == 'p':
            style_el = child.find('.//' + qn('w:pStyle'))
            style = style_el.get(qn('w:val'), '') if style_el is not None else ''
            text = ''.join(e.text or '' for e in child.iter(qn('w:t'))).strip()

            if 'Heading' in style and text:
                # 过滤掉文件顶部的固定标题
                if text not in ('All your annotations',) and not re.match(r'^\d+\s*notes', text):
                    current_chapter = text

        # ── 表格：提取笔记 ─────────────────────────────────────────────────
        elif tag == 'tbl':
            tcs = get_tc_texts(child)

            if not tcs:
                continue

            # Play Books 格式：tc[2] = 正文+日期，tc[3] = 页码
            # 兼容格式变体（tc 数量不足 3 的情况）
            if len(tcs) >= 3:
                raw_text = tcs[2].strip()
                page = tcs[3].strip() if len(tcs) >= 4 else ""
            else:
                raw_text = tcs[0].strip()
                page = ""

            # 必须含日期才算笔记
            m = date_pattern.search(raw_text)
            if not m:
                continue

            date = m.group(1)
            note_text = raw_text[:m.start()].strip()

            if note_text:
                notes.append({
                    "chapter": current_chapter,
                    "text":    note_text,
                    "date":    date,
                    "page":    page,
                })

    # ── 格式化输出（纯笔记正文，每条之间空一行）────────────────────────────
    output_text = '\n\n'.join(note['text'] for note in notes)

    if output_path:
        Path(output_path).write_text(output_text, encoding='utf-8')
        print(f"Done: saved to {output_path} ({len(notes)} notes)\n")

    print(output_text)

    return notes


if __name__ == '__main__':
    # ── 在这里修改输入/输出路径 ────────────────────────────────────────────
    INPUT_FILE  = r"C:\Users\reala\Downloads\Notes from _合作的复杂性：基于参与者竞争与合作的模型_.docx"
    OUTPUT_FILE = r"C:\Users\reala\Downloads\notes_output.txt"
    # ──────────────────────────────────────────────────────────────────────

    extract_notes(INPUT_FILE, OUTPUT_FILE)
