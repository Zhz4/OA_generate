import json
import os


def getConfig(url):
    with open(url, 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config


# 写入文件
def out_file(dir_name, out_put_name, write_file):
    # 固定的文件夹名
    dir_name = './output/' + dir_name

    # 创建文件夹（如果不存在的话）
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # 将文件路径与文件夹结合
    full_path = os.path.join(dir_name, out_put_name)

    # 在指定的文件夹中写入文件
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(write_file)
