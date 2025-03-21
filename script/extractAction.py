import os
import re
import json


def extract_actions_from_logs(log_dir):
    actions = set()

    # 遍历目录下的所有文件
    for filename in os.listdir(log_dir):
        file_path = os.path.join(log_dir, filename)

        # 确保是普通文件（防止误处理子目录）
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    match1 = re.search(r'Run (\S+/\S+)@\S+', line)
                    match2 = re.search(r"Download action repository '([\w.-]+/[\w.-]+)@[\w.-]+'", line)
                    if match1:
                        actions.add(match1.group(1))
                    if match2:
                        actions.add(match2.group(1))

    return actions


# 指定日志文件目录
log_dir = "newlogs"

# 解析目录下所有日志文件
actions_from_logs = extract_actions_from_logs(log_dir)

# 构建 JSON 数据结构
output_data = {
    "total_unique_actions": len(actions_from_logs),
    "identified_actions": list(actions_from_logs)  # 将 set 转换为 list 以兼容 JSON
}

# 将结果写入 JSON 文件
output_file = "actions_output.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, indent=4, ensure_ascii=False)

print(f"JSON file '{output_file}' has been generated.")