import json

# 定义所需字段及其输出顺序
fields = [
    "request_throughput",
    "output_throughput",
    "total_token_throughput",
    "mean_ttft_ms",
    "median_ttft_ms",
    "p90_ttft_ms",
    "p99_ttft_ms",
    "mean_tpot_ms",
    "median_tpot_ms",
    "p90_tpot_ms",
    "p99_tpot_ms",
    "mean_itl_ms",
    "median_itl_ms",
    "p90_itl_ms",
    "p99_itl_ms"
]

# 输入和输出文件路径
input_path = "benchmark_results.json"
output_path = "summary_results.tsv"

# 打开输入文件和输出文件
with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
    # 先写入 TSV 表头（字段名）
    outfile.write("\t".join(fields) + "\n")

    # 逐行读取 JSON Lines 文件
    for line in infile:
        record = json.loads(line.strip())

        # 按字段顺序提取值，缺失字段填 0.0
        row = []
        for field in fields:
            value = record.get(field)
            if value is None:
                row.append("0.0")
            else:
                row.append(f"{value:.2f}")  # 保留两位小数

        # 写入 TSV 文件
        outfile.write("\t".join(row) + "\n")

print(f"每行原始数据已按字段顺序输出到 {output_path}")