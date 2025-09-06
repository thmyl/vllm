# Usage: python als.py <log_file> <txt_file>
# 计算resume的step在nsys分析的txt文件中的Duration总和
# NVTX Push/Pop Range Trace
import re
import sys

def clean_number(num_str):
    """清理数字字符串，去除省略号等非数字字符"""
    return num_str.split('…')[0].strip()

def extract_step_before_resume(log_file):
    """从log文件中提取[Resume req]前面的step编号"""
    step_before_resume = []
    with open(log_file, 'r') as f:
        previous_line = None
        for line in f:
            if '[Resume req]' in line and previous_line is not None:
                # 从前一行提取step编号
                match = re.search(r'step_(\d+)', previous_line)
                if match:
                    step_before_resume.append(int(match.group(1)))
            previous_line = line
    return step_before_resume

def extract_step_info(txt_file, target_steps, start_step=2000):
    """从txt文件中提取step信息"""
    step_info = {}  # [Resume req]相关step的Duration
    all_steps_durations = []  # 所有step的Duration
    selected_steps_durations = []  # 从start_step开始的step的Duration
    
    with open(txt_file, 'r') as f:
        for line in f:
            if ':Step:' in line:
                parts = line.split()
                if len(parts) >= 4:
                    # 提取step编号
                    step_match = re.search(r':Step:(\d+)', line)
                    if step_match:
                        step = int(step_match.group(1))
                        try:
                            duration = int(clean_number(parts[2]))
                            all_steps_durations.append(duration)
                            
                            # 如果是目标step，记录持续时间
                            if step in target_steps:
                                step_info[step] = duration
                            
                            # 如果step >= start_step，记录持续时间
                            if step >= start_step:
                                selected_steps_durations.append(duration)
                        except ValueError as e:
                            print(f"Warning: Could not parse duration in line: {line.strip()}")
                            continue
    
    # 计算[Resume req]相关step的总Duration
    resume_total = sum(step_info.values())
    
    # 计算从start_step开始到最后一个step的总Duration
    selected_total = sum(selected_steps_durations)
    
    # 计算所有step的总Duration
    all_total = sum(all_steps_durations)
    
    return step_info, resume_total, selected_total, all_total

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <log_file> <txt_file>")
        sys.exit(1)
    
    log_file = sys.argv[1]
    txt_file = sys.argv[2]
    start_step = 2658  # 可以修改这个值
    
    # 1. 从log文件中提取[Resume req]前面的step编号
    target_steps = extract_step_before_resume(log_file)
    print(f"Found steps before [Resume req]: {target_steps}")
    
    # 2. 从txt文件中提取step信息
    step_durations, resume_total, selected_total, all_total = extract_step_info(txt_file, target_steps, start_step)
    
    # 输出结果
    print("\n[Resume req] related step durations (ns):")
    for step, duration in sorted(step_durations.items()):
        print(f"Step {step}: {duration} ns")
    
    print(f"\nTotal duration for [Resume req] steps: {resume_total} ns")
    print(f"Total duration for [Resume req] steps: {resume_total / 1_000_000:.2f} ms")
    
    # 输出从start_step开始到最后一个step的Duration总和
    print(f"\nDuration sum from step {start_step} to last step:")
    print(f"Total duration: {selected_total} ns")
    print(f"Total duration: {selected_total / 1_000_000:.2f} ms")
    
    # 输出所有step的Duration总和
    print(f"\nDuration sum for all steps:")
    print(f"Total duration: {all_total} ns")
    print(f"Total duration: {all_total / 1_000_000:.2f} ms")

if __name__ == "__main__":
    main()