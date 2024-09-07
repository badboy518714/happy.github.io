import os
import time

def update_txt_file():
    file_path = "0.txt"  # 替换为实际的文件路径

    # 读取文件内容
    with open(file_path, "r") as file:
        content = file.read()

    # 更新内容（这里只是简单地添加一些文本）
    updated_content =  f"{int(time.time()*1000)}--This is an updated line."

    # 写入更新后的内容
    with open(file_path, "w") as file:
        file.write(updated_content)

if __name__ == "__main__":
    update_txt_file()
