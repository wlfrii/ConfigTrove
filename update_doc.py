import re

def extract_title_and_intro(input_file, output_file):
    # 读取 Markdown 文件
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 使用正则表达式提取标题
    title_match = re.search(r'^# (.+)', content, re.MULTILINE)
    title = title_match.group(1) if title_match else '无标题'

    # 提取标题后的内容
    # 假设介绍是标题后的第一段
    content_after_title = content[title_match.end():] if title_match else content
    intro = re.search(r'^\n*(.+?)(\n\s*\n|$)', content_after_title, re.DOTALL)
    intro_text = intro.group(1).strip() if intro else '无介绍'

    # 将提取的内容写入新的 Markdown 文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write(f"{intro_text}\n")

# 使用示例
extract_title_and_intro('./Windows_SoftwareInstallation/Install_Jekyll.md', 'output.md')