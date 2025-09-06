# 用于简化tensor parallel = 8时，输出flash_attn_varlen_func日志的重复操作
import re

def deduplicate_log(input_path, output_path):
    # 正则匹配日志块开始行
    block_start_pattern = re.compile(r'>>> flash_attn_varlen_func')
    # 正则提取三个核心字段的值
    max_query_pattern = re.compile(r'max_query_len:\s*(\d+)')
    cu_seqlens_pattern = re.compile(r'cu_seqlens_q:\s*(\[.*?\])')
    seqused_pattern = re.compile(r'seqused_k:\s*(\[.*?\])')
    # 匹配空行（日志块结束标志）
    empty_line_pattern = re.compile(r'^\s*$')

    # 存储已出现的核心字段组合（用于去重）
    seen_signatures = set()
    # 当前处理的日志块
    current_block = []
    # 记录当前块的三个核心值
    current_vals = {}
    # 是否开始处理日志块（跳过开头启动信息）
    start_processing = False

    with open(input_path, 'r', encoding='utf-8', errors='ignore') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:

        for line in infile:
            # 清理行尾特殊字符（如^M）
            cleaned_line = line.rstrip('\r\n')
            raw_line = line  # 保留原始行（含格式符）

            # 阶段1：处理开头的启动信息（直接输出）
            if not start_processing:
                outfile.write(raw_line)
                # 当遇到第一个日志块开始行时，切换到处理阶段
                if block_start_pattern.search(cleaned_line):
                    start_processing = True
                    current_block.append(raw_line)
                continue

            # 阶段2：处理日志块内容
            if start_processing:
                # 检测是否为新日志块的开始
                if block_start_pattern.search(cleaned_line):
                    # 先处理上一个日志块
                    if current_block:
                        # 提取三个核心值并生成签名
                        sig = (
                            current_vals.get('max_query'),
                            current_vals.get('cu_seqlens'),
                            current_vals.get('seqused')
                        )
                        # 仅保留首次出现的签名对应的日志块
                        if sig not in seen_signatures and all(sig):
                            outfile.writelines(current_block)
                            seen_signatures.add(sig)
                        # 重置当前块
                        current_block = []
                        current_vals = {}
                    # 添加新块的第一行
                    current_block.append(raw_line)

                # 提取三个核心字段的值
                max_match = max_query_pattern.search(cleaned_line)
                if max_match:
                    current_vals['max_query'] = max_match.group(1)
                    current_block.append(raw_line)
                    continue

                cu_match = cu_seqlens_pattern.search(cleaned_line)
                if cu_match:
                    current_vals['cu_seqlens'] = cu_match.group(1)
                    current_block.append(raw_line)
                    continue

                seq_match = seqused_pattern.search(cleaned_line)
                if seq_match:
                    current_vals['seqused'] = seq_match.group(1)
                    current_block.append(raw_line)
                    continue

                # 处理空行（日志块结束标志）
                if empty_line_pattern.match(cleaned_line):
                    current_block.append(raw_line)
                    # 处理当前完整块
                    sig = (
                        current_vals.get('max_query'),
                        current_vals.get('cu_seqlens'),
                        current_vals.get('seqused')
                    )
                    if sig not in seen_signatures and all(sig):
                        outfile.writelines(current_block)
                        seen_signatures.add(sig)
                    # 重置
                    current_block = []
                    current_vals = {}
                    continue

                # 其他行（如设备信息行）直接加入当前块
                current_block.append(raw_line)

        # 处理最后一个日志块
        if current_block and all(current_vals.values()):
            sig = (
                current_vals['max_query'],
                current_vals['cu_seqlens'],
                current_vals['seqused']
            )
            if sig not in seen_signatures:
                outfile.writelines(current_block)

if __name__ == '__main__':
    input_log = '../server_benchmark_1.log'    # 替换为你的输入日志路径
    output_log = './tmp.log'  # 去重后的输出路径
    deduplicate_log(input_log, output_log)
    print(f"去重完成，结果保存至 {output_log}")