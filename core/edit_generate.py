from template.modal_template import mainModel, form_template, form_item_template, script_main_template
import json
import os


def getConfig():
    with open('./config/edit_config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config


# 写入文件
def out_file(out_put_name, write_file):
    # 固定的文件夹名
    dir_name = './output/components'

    # 创建文件夹（如果不存在的话）
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # 将文件路径与文件夹结合
    full_path = os.path.join(dir_name, out_put_name)

    # 在指定的文件夹中写入文件
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(write_file)


def run():
    print('======开始生成Edit代码=========')
    config = getConfig()
    form_item_list = config['form_item_list']
    form_item_str = ''
    for item in form_item_list:
        form_item_str += form_item_template(item['label'], item['value'])
    form_str = form_template(form_item_str)
    mainModel_str = mainModel(form_str)
    out_file("EditModal.vue", mainModel_str + script_main_template())
    print('====== 代码生成完成，请到output/components 文件夹中查看 =========')

