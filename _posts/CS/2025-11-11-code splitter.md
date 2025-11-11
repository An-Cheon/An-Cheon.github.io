---
layout: post
title: 动态规划实现Python代码分割
categories: [CS, Python]
tags: [python]
---

以函数为最小单元用动态规划将python文件分割成代码行数类似的指定个文件

```python
import os
import re


def get_indentation(line):
    """获取行的缩进空格数"""
    if not line or line[0] not in (' ', '\t'):
        return 0
    match = re.match(r'^([ \t]*)', line)
    return len(match.group(1)) if match else 0


def extract_header_and_imports(lines):
    """提取文件头部、导入语句和代码体"""
    n = len(lines)
    used = [False] * n
    header_lines = []
    idx = 0

    # 1. shebang
    if n > 0 and lines[0].startswith("#!"):
        header_lines.append(lines[0])
        used[0] = True
        idx = 1

    # 2. encoding comment
    if idx < n and re.search(r'coding[:=]\s*([-\w.]+)', lines[idx]):
        header_lines.append(lines[idx])
        used[idx] = True
        idx += 1

    # 3. 跳过前导空行和注释，直到第一个代码行或模块级 docstring
    first_code_idx = idx
    while first_code_idx < n and (lines[first_code_idx].strip() == "" or
                                  lines[first_code_idx].lstrip().startswith("#")):
        first_code_idx += 1

    # 4. 检查并提取模块级docstring
    docstring_end_idx = first_code_idx
    if first_code_idx < n:
        line = lines[first_code_idx].strip()
        # 匹配 docstring 的开始: """ 或 ''' (可选 r/u/R/U 前缀)
        match = re.match(r'^([ruRU]{0,2})("""|\'\'\')', line)
        if match:
            quote = match.group(2)
            i = first_code_idx

            # 找到 docstring 结束位置
            if line.endswith(quote) and len(line) > len(quote * 2):
                # 单行 docstring
                docstring_end_idx = i + 1
            else:
                # 多行 docstring
                i += 1
                while i < n:
                    if lines[i].strip().endswith(quote) and lines[i].strip() != quote:  # 避免匹配到非结束行中间的 quote
                        i += 1
                        break
                    if lines[i].strip() == quote:  # 匹配只有 quote 的行
                        i += 1
                        break
                    i += 1
                docstring_end_idx = i

    # 提取 docstring 之前的所有注释和空行 (如果存在)
    for j in range(idx, docstring_end_idx):
        header_lines.append(lines[j])
        used[j] = True
    idx = docstring_end_idx

    # 5. 【修正】收集顶层 import 语句、空行和注释
    import_lines = []
    seen_imports = set()

    i = idx
    while i < n:
        if used[i]:
            i += 1
            continue

        line = lines[i]
        stripped = line.strip()
        indentation = get_indentation(line)

        # 检查是否是顶层 import 语句
        is_import_line = re.match(r'^(from\s+[\w.]+\s+import|import\s+)', stripped)

        # 遇到第一个非空、非注释、非import的顶层代码行，停止收集
        if stripped != "" and not stripped.startswith("#") and not is_import_line and indentation == 0:
            break  # 遇到第一个顶层代码块的开始

        # 遇到任何顶层空行、注释或导入，都将其添加到 import_lines
        if stripped == "" or stripped.startswith("#") or is_import_line:

            if is_import_line:
                # 处理导入块
                import_block = [line]
                used[i] = True

                # 处理多行 import (未闭合的括号)
                if line.count('(') > line.count(')'):
                    k = i + 1
                    while k < n:
                        # 仅在同一缩进级别或导入块内，且不包含顶层代码
                        if lines[k].strip() != "" and get_indentation(lines[k]) == 0 and not lines[
                            k].lstrip().startswith("#"):
                            # 如果多行import跨越到了下一个顶层代码块，停止
                            break

                        import_block.append(lines[k])
                        used[k] = True
                        if lines[k].count(')') > lines[k].count('('):  # 检查是否闭合
                            break
                        k += 1
                    i = k - 1  # i 在循环末尾会 +1，所以这里指向多行 import 的最后一行

                import_str = ''.join(import_block)
                # 避免重复导入（尽管这个去重逻辑可能过于简单，但保留原意）
                if import_str.strip() not in seen_imports:
                    import_lines.extend(import_block)
                    seen_imports.add(import_str.strip())
            else:
                # 顶层空行或注释，直接加入
                import_lines.append(line)
                used[i] = True  # 标记为空行或注释已使用

        i += 1

    # i 现在指向第一个未使用的代码行

    # 6. 剩余部分为 body
    body_lines = [lines[j] for j in range(idx, n) if not used[j]]

    # 修正：将 body_lines 中开头的空行和注释移到 import_lines 的末尾
    # 因为它们属于模块级别的声明（导入之后，顶层代码之前）

    # 找到 body_lines 中第一个非空、非注释的行
    body_start_idx = 0
    while body_start_idx < len(body_lines) and \
            (body_lines[body_start_idx].strip() == "" or body_lines[body_start_idx].lstrip().startswith("#")):
        body_start_idx += 1

    # 将 body_lines 开头的所有空行和注释移到 import_lines 的末尾
    if body_start_idx > 0:
        import_lines.extend(body_lines[:body_start_idx])
        body_lines = body_lines[body_start_idx:]

    return header_lines, import_lines, body_lines


def find_all_blocks(body_lines):
    """【修正】找出所有块，确保块的 start 包含前导空行和注释"""
    n = len(body_lines)
    blocks = []
    i = 0  # 当前处理 body_lines 的起始索引

    while i < n:

        # 记录当前块的实际起始位置 (包括前面的空行和注释)
        start = i

        # 找到第一个有效代码行
        first_code_line_i = i
        while first_code_line_i < n and (
                body_lines[first_code_line_i].strip() == '' or body_lines[first_code_line_i].lstrip().startswith('#')):
            first_code_line_i += 1

        if first_code_line_i >= n:
            break

        # i 现在指向第一个有效代码行
        i = first_code_line_i

        indent = get_indentation(body_lines[i])

        # 只处理顶层代码（缩进为0）
        if indent > 0:
            # 这是一个缩进的代码，意味着它可能是前一个块的延续，
            # 或者文件是以缩进代码开始的（不常见，但作为“正常”块处理直到遇到顶层代码或文件末尾）
            # 由于前面的循环已经确保 i 是第一个有效代码行，如果缩进不为0，那么它不是一个新块的开始，
            # 此时的逻辑应该取决于上下文，但在顶层代码分割中，我们只关心顶层块（indent=0）。
            # 为了稳健性，如果它不是顶层块，我们只前进一行。
            # 但是，由于 find_all_blocks 是对 body_lines（即代码体）的解析，
            # 这里的 indent > 0 可能意味着 body_lines 之前有导入语句，而 i 是一个缩进行。
            # 为了防止跳过代码，将其作为普通块处理到文件末尾或下一个顶层块。

            curr_i = i + 1
            while curr_i < n:
                curr_indent = get_indentation(body_lines[curr_i])
                curr_stripped = body_lines[curr_i].strip()

                if curr_stripped == '':
                    curr_i += 1
                    continue

                # 遇到同级或更低缩进的代码（即回到顶层代码）
                if curr_indent <= indent:
                    break

                curr_i += 1

            blocks.append({
                'type': 'normal_indented',  # 标记为缩进的普通块
                'start': start,
                'end': curr_i,
                'class_start': None,
                'class_end': None
            })
            i = curr_i
            continue

        stripped = body_lines[i].strip()

        # 检查是否是class定义
        if stripped.startswith('class '):
            class_start = start  # 块的开始是包含前导空行/注释的 start
            class_indent = indent
            curr_i = i + 1

            # 收集class内的所有方法/函数
            class_methods = []

            # class 块的结束位置
            class_end = curr_i

            # 找到第一个方法/代码行之前的部分（class header）
            first_method_start = -1
            temp_i = curr_i

            while temp_i < n:
                curr_indent = get_indentation(body_lines[temp_i])
                curr_stripped = body_lines[temp_i].strip()

                if curr_stripped == '':
                    class_end = temp_i + 1
                    temp_i += 1
                    continue

                if curr_indent <= class_indent:  # 遇到下一个同级或更高层级代码块
                    class_end = temp_i
                    break

                # 检查是否是方法定义（class内的def或装饰器）
                if curr_stripped.startswith('def ') or curr_stripped.startswith('@'):
                    if first_method_start == -1:
                        first_method_start = temp_i

                    # 找到当前方法的结束
                    method_start = temp_i
                    method_indent = curr_indent

                    # 找到方法定义行后第一个有效行
                    j = temp_i
                    while j < n and (body_lines[j].strip() == "" or body_lines[j].lstrip().startswith("#")):
                        j += 1

                    # 如果方法定义行后是 docstring
                    if j < n:
                        line = body_lines[j].strip()
                        match = re.match(r'^([ruRU]{0,2})("""|\'\'\')', line)
                        if match:
                            quote = match.group(2)
                            k = j
                            # 确定 docstring 结束位置
                            is_multiline = not (line.endswith(quote) and len(line) > len(quote * 2))
                            if is_multiline:
                                k += 1
                                while k < n:
                                    # 必须确保缩进不低于方法缩进
                                    if get_indentation(body_lines[k]) < method_indent and body_lines[k].strip() != "":
                                        # 缩进不正确，可能有问题，停止
                                        break

                                    if body_lines[k].strip().endswith(quote) and \
                                            (len(body_lines[k].strip()) > len(quote) or body_lines[k].strip() == quote):
                                        k += 1
                                        break
                                    k += 1
                            else:
                                k += 1  # 单行 docstring 占用一行

                            temp_i = k - 1  # 下一个方法/代码从 docstring 结束行后开始扫描

                    # 从方法 docstring 结束后开始扫描方法体

                    # 找到下一个方法或类/模块级代码
                    k = temp_i + 1
                    while k < n:
                        mi = get_indentation(body_lines[k])
                        ms = body_lines[k].strip()

                        if ms == '':
                            k += 1
                            continue

                        # 遇到同级或更低缩进的代码 (即回到 class 缩进或顶层)
                        if mi <= method_indent and mi > class_indent:  # 方法结束，但仍在 class 内部
                            # 如果是另一个方法/@装饰器，则它开始于 method_start
                            # 否则，它可能是 class 内部的变量赋值等
                            if ms.startswith('def ') or ms.startswith('@'):
                                break

                        if mi <= class_indent:  # 遇到下一个顶层代码块
                            break

                        k += 1

                    method_end = k
                    class_methods.append((method_start, method_end))
                    temp_i = method_end - 1  # -1 是因为 for 循环的 temp_i 递增
                    class_end = method_end  # class 结束位置被方法结束位置更新

                temp_i += 1

            # 处理 class 声明到第一个方法之间的内容 (class header)
            if first_method_start == -1:
                first_method_start = class_end  # 如果没有方法，则整个 class 是一个块

            # 决定是否拆分class
            class_lines = class_end - class_start

            if class_lines > 200 and len(class_methods) > 1:
                # 大class，拆分成多个块

                # 块1: class声明 + 第一个方法之前的内容 (包括注释/docstring/空行)
                blocks.append({
                    'type': 'class_header',
                    'start': class_start,
                    'end': first_method_start,
                    'class_start': class_start,
                    'class_end': class_end
                })

                # 每个方法作为一个块
                for method_start, method_end in class_methods:
                    blocks.append({
                        'type': 'class_method',
                        'start': method_start,
                        'end': method_end,
                        'class_start': class_start,
                        'class_end': class_end
                    })
            else:
                # 小class，不拆分
                blocks.append({
                    'type': 'class_whole',
                    'start': class_start,
                    'end': class_end,
                    'class_start': class_start,
                    'class_end': class_end
                })

            i = class_end  # 下一个循环从 class_end 开始

        else:
            # 普通顶层代码（def或其他）
            # start 已经指向了包含空行和注释的起始位置

            curr_i = i + 1
            while curr_i < n:
                curr_indent = get_indentation(body_lines[curr_i])
                curr_stripped = body_lines[curr_i].strip()

                if curr_stripped == '':
                    curr_i += 1
                    continue

                if curr_indent == 0:
                    break

                curr_i += 1

            blocks.append({
                'type': 'normal',
                'start': start,
                'end': curr_i,
                'class_start': None,
                'class_end': None
            })

            i = curr_i  # 下一个循环从 curr_i 开始

    return blocks


def split_body_by_blocks(body_lines, parts, blocks):
    """使用动态规划分割块"""
    num_blocks = len(blocks)

    if num_blocks == 0:
        return []

    block_lines = [b['end'] - b['start'] for b in blocks]
    total_lines = sum(block_lines)
    target_lines = total_lines / parts

    print(f"\n总行数: {total_lines}, 目标每部分: {target_lines:.1f}行")
    print(f"共有 {num_blocks} 个块")

    cumsum = [0]
    for lines in block_lines:
        cumsum.append(cumsum[-1] + lines)

    def range_sum(i, j):
        return cumsum[j] - cumsum[i]

    INF = float('inf')
    dp = [[INF] * (parts + 1) for _ in range(num_blocks + 1)]
    parent = [[-1] * (parts + 1) for _ in range(num_blocks + 1)]

    dp[0][0] = 0

    for i in range(1, num_blocks + 1):
        for k in range(1, min(i, parts) + 1):
            for j in range(k - 1, i):
                if dp[j][k - 1] == INF:
                    continue

                part_lines = range_sum(j, i)
                deviation = abs(part_lines - target_lines)
                max_deviation = max(dp[j][k - 1], deviation)

                if max_deviation < dp[i][k]:
                    dp[i][k] = max_deviation
                    parent[i][k] = j

    split_points = []
    curr_i = num_blocks
    curr_k = parts

    while curr_k > 0:
        prev_i = parent[curr_i][curr_k]
        if prev_i == -1:
            if curr_k == parts:  # 第一次回溯就失败，说明 num_blocks < parts
                split_points = list(range(1, num_blocks))
            break
        split_points.append(prev_i)
        curr_i = prev_i
        curr_k -= 1

    split_points.sort()
    split_points.append(num_blocks)

    segments = []
    prev = 0
    for sp in split_points:
        if sp > prev:
            segments.append((prev, sp))
            prev = sp
        elif sp == num_blocks and prev < num_blocks:  # 确保最后一个分段被添加
            segments.append((prev, sp))
            prev = sp

    # 再次检查，如果块数小于 parts，确保每个块一个 part
    if not segments and num_blocks > 0:
        for i in range(num_blocks):
            segments.append((i, i + 1))

    print("\n分割结果:")
    for i, (start_idx, end_idx) in enumerate(segments):
        lines = sum(block_lines[j] for j in range(start_idx, end_idx))
        deviation = abs(lines - target_lines)
        deviation_pct = (deviation / target_lines) * 100 if target_lines > 0 else 0
        print(
            f"  Part {i + 1}: {lines} 行, 块索引: [{start_idx}, {end_idx}), 偏差: {lines - target_lines:+.0f} ({deviation_pct:.1f}%)")

    return segments


def write_part_file(f, header_lines, import_lines, body_lines, blocks, block_indices, is_first_part, is_last_part,
                    file_ends_with_newline):
    """写入分割后的文件，确保与原始文件结构一致 (通过切片写入 body)"""

    # 1. 写入 header
    if is_first_part:
        for ln in header_lines:
            f.write(ln)

        # 2. 写入 imports (现在包含导入之间的空行和注释)
        if import_lines:

            # 确保 import 之前有一个空行 (如果前面有内容且最后一行没有换行)
            if header_lines and not header_lines[-1].endswith("\n") and header_lines[-1].strip() != "":
                f.write("\n")

            # 写入 imports
            for ln in import_lines:
                f.write(ln)

    # 3. 写入 body 块
    if not block_indices:
        return

    # 获取 Part N 在 body_lines 中的实际起始行索引
    start_block_index = block_indices[0]
    start_body_line_index = blocks[start_block_index]['start']

    # 找出 Part N 在 body_lines 中的实际结束行索引
    end_block_index = block_indices[-1]
    end_body_line_index = blocks[end_block_index]['end']

    # 遍历 Part N 对应的 body_lines 范围
    lines_to_write = body_lines[start_body_line_index:end_body_line_index]

    # 【移除的空行修正】: 因为 extract_header_and_imports 已经将导入后的所有空行和注释包含在 import_lines 中，
    # 或者 body_lines 的第一块包含了它自己的前导空行和注释。
    # 额外的空行逻辑会导致重复。
    # 原始文件在多行导入之后没有空行，所以不应添加。
    # if is_first_part and import_lines and lines_to_write:
    #     import_ends_with_empty_line = import_lines[-1].strip() == ""
    #     body_starts_with_empty_line = lines_to_write[0].strip() == ""
    #     if not import_ends_with_empty_line and not body_starts_with_empty_line:
    #         if body_lines[start_body_line_index].strip() != "":
    #             f.write("\n")

    # 针对最后一个文件和文件末尾换行进行修正
    if is_last_part and lines_to_write and not file_ends_with_newline:
        last_line = lines_to_write[-1]
        if last_line.endswith('\n'):
            # 移除最后一行内容的换行符，以匹配原始文件末尾没有换行符的情况
            lines_to_write[-1] = last_line[:-1]

    # 写入所有行
    for ln in lines_to_write:
        f.write(ln)


def split_python_code(source_code_path, parts, destination_path):
    """将Python代码文件分割成多个部分"""

    # 读取原始文件内容和行列表
    with open(source_code_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

        # 判断原始文件是否以换行符结尾
    file_ends_with_newline = lines and lines[-1].endswith('\n')

    # 提取 header, imports 和 body
    header_lines, import_lines, body_lines = extract_header_and_imports(lines)

    # 找出所有块（支持拆分大class）
    blocks = find_all_blocks(body_lines)

    # 分割
    segments = split_body_by_blocks(body_lines, parts, blocks)

    os.makedirs(destination_path, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(source_code_path))[0]

    output_files = []

    for i, (start_idx, end_idx) in enumerate(segments):
        out_path = os.path.join(destination_path, f"{base_name}_part{i + 1}.split")

        with open(out_path, "w", encoding="utf-8") as f:
            block_indices = list(range(start_idx, end_idx))

            # 使用 Part 索引来判断是否是最后一个文件
            is_last_part = (i == len(segments) - 1)

            write_part_file(f, header_lines, import_lines, body_lines,
                            blocks, block_indices,
                            is_first_part=(i == 0),
                            is_last_part=is_last_part,
                            file_ends_with_newline=file_ends_with_newline)

        output_files.append(out_path)

    return output_files


def merge_split_files(split_files, output_path):
    """将分割后的文件合并成一个完整文件用于验证"""
    print(f"\n正在合并文件到: {output_path}")

    with open(output_path, "w", encoding="utf-8") as out_f:
        for i, file_path in enumerate(split_files):
            print(f"  合并 Part {i + 1}: {file_path}")
            with open(file_path, "r", encoding="utf-8") as in_f:
                content = in_f.read()
                out_f.write(content)

    print(f"✓ 合并完成: {output_path}")


# ========== 配置参数 ==========
source_code_path = "pyqt6_v5.5.py"  # 源代码文件路径
parts = 3  # 分割成几部分
destination_path = "./Split code"  # 输出目录
# ==============================

if __name__ == "__main__":

    # 检查源文件是否存在
    if not os.path.exists(source_code_path):
        print(f"错误: 源代码文件未找到: {source_code_path}")

    # 开始分割
    try:
        result = split_python_code(source_code_path, parts, destination_path)
        print("\n生成的文件路径如下：")
        for p in result:
            print(p)

        # 检查每个part的开头
        '''
        print("\n每个part的前10行:")
        for i, file_path in enumerate(result):
            print(f"\n--- Part {i + 1} ({file_path}) ---")
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            print(f"总行数: {len(lines)}")
            for j, line in enumerate(lines[:10]):
                print(f"  {j + 1}: {repr(line.rstrip())}")
        '''
        # 合并文件用于验证
        base_name = os.path.splitext(os.path.basename(source_code_path))[0]
        merged_path = os.path.join(destination_path, f"{base_name}_merged.py")
        merge_split_files(result, merged_path)

        # 验证行数和内容
        print("\n验证结果:")
        with open(source_code_path, "r", encoding="utf-8") as f:
            original_content = f.read()

        with open(merged_path, "r", encoding="utf-8") as f:
            merged_content = f.read()

        # 确保计算行数时，原始文件和合并文件的逻辑一致
        original_lines = original_content.count('\n') + (
            1 if original_content and not original_content.endswith('\n') else 0)
        merged_lines = merged_content.count('\n') + (1 if merged_content and not merged_content.endswith('\n') else 0)

        print(f"  原始文件: {original_lines} 行")
        print(f"  合并文件: {merged_lines} 行")

        # 比较内容
        if original_content == merged_content:
            print("  ✓ 内容完全一致")
        else:
            print("  ✗ 内容有差异")

            # 逐行对比找出差异
            original_lines_list = original_content.split('\n')
            merged_lines_list = merged_content.split('\n')

            # 找到第一个不同的行
            for i in range(min(len(original_lines_list), len(merged_lines_list))):
                if original_lines_list[i] != merged_lines_list[i]:
                    print(f"\n  第 {i + 1} 行开始不同:")
                    print(f"    原始: {repr(original_lines_list[i])}")
                    print(f"    合并: {repr(merged_lines_list[i])}")

                    # 显示上下文
                    print(f"\n  上下文（第{max(1, i - 2)}到{min(len(original_lines_list), i + 5)}行）:")
                    print("  原始文件:")
                    for j in range(max(0, i - 2), min(len(original_lines_list), i + 5)):
                        marker = ">>> " if j == i else "    "
                        print(f"  {marker}{j + 1}: {repr(original_lines_list[j][:80])}")

                    print("\n  合并文件:")
                    for j in range(max(0, i - 2), min(len(merged_lines_list), i + 5)):
                        marker = ">>> " if j == i else "    "
                        print(f"  {marker}{j + 1}: {repr(merged_lines_list[j][:80])}")
                    break
            else:
                if len(original_lines_list) != len(merged_lines_list):
                    print(f"\n  文件长度不同。原始 {len(original_lines_list)} 行, 合并 {len(merged_lines_list)} 行.")

    except Exception as e:
        print(f"\n发生错误: {e}")
```

示例运行结果

```
总行数: 1854, 目标每部分: 618.0行
共有 76 个块

分割结果:
  Part 1: 598 行, 块索引: [0, 25), 偏差: -20 (3.2%)
  Part 2: 602 行, 块索引: [25, 53), 偏差: -16 (2.6%)
  Part 3: 654 行, 块索引: [53, 76), 偏差: +36 (5.8%)

生成的文件路径如下：
./Split code\pyqt6_v5.5_part1.split
./Split code\pyqt6_v5.5_part2.split
./Split code\pyqt6_v5.5_part3.split

正在合并文件到: ./Split code\pyqt6_v5.5_merged.py
  合并 Part 1: ./Split code\pyqt6_v5.5_part1.split
  合并 Part 2: ./Split code\pyqt6_v5.5_part2.split
  合并 Part 3: ./Split code\pyqt6_v5.5_part3.split
✓ 合并完成: ./Split code\pyqt6_v5.5_merged.py

验证结果:
  原始文件: 1874 行
  合并文件: 1874 行
  ✓ 内容完全一致
```
