import os
import json
from template.vue_template import filter_wrap_template, form_item_template, main_template, tool_wrap_template, \
    table_page, \
    button_template
from template.script_template import import_icon_template, import_column_template, hooks_template, script_main_template, \
    search_template, tool_handler_template
from template.table_template import generate_columns
from template.style_template import style_main_template

# 读取配置
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
# 获取配置项
form_item_list = config['form_item_list']
tool_button_list = config['tool_button_list']
table_list = config['table_list']


# vue模版部分
def template():
    form_item = ''
    for item in form_item_list:
        form_item += form_item_template.substitute(form_item_label=item['label'], form_item_key=item['key'])

    tool_button = ''
    for item in tool_button_list:
        tool_button += button_template.substitute(button_name=item['button_name'], handler=item['handler'],
                                                  icon_component=item['icon_component'])
    tool_wrap = tool_wrap_template.substitute(tool_wrap=tool_button)

    filter_wrap = filter_wrap_template.substitute(form_item=form_item, tool_wrap=tool_wrap)
    return main_template.substitute(main=filter_wrap + table_page)


# vue script部分
def script():
    # 引入导入模版
    # 导入的icon的列表
    import_icon_list = ['Search']
    # 工具函数列表
    handler_list = []

    for item in tool_button_list:
        import_icon_list.append(item['icon_component'])
        handler_list.append({
            "handlerName": item['button_name'],
            "handler": item['handler']
        })
    import_string = import_icon_template.substitute(
        importIcon=','.join(
            list(set(import_icon_list)))) + import_column_template.substitute() + hooks_template.substitute()

    # 生成工具函数
    tool_handler_str = ''
    # 去重
    handler_list_handler_set = set()
    handler_deduplication = list(filter(
        lambda x: x["handler"] not in handler_list_handler_set and not handler_list_handler_set.add(x["handler"]),
        handler_list))
    for item in handler_deduplication:
        tool_handler_str += tool_handler_template.substitute(handler=item['handler'], handlerName=item['handlerName'])

    # 导入搜索模版
    search_string = search_template.substitute()

    # 导入主要模版
    script_main_string = script_main_template.substitute(import_template=import_string,
                                                         other_template=search_string + tool_handler_str)
    return script_main_string


# style部分
def style():
    return style_main_template.substitute()


# tableConfig 部分
def tableConfig_generate():
    return generate_columns(table_list)


# 写入文件
def out_file(out_put_name, write_file):
    # 固定的文件夹名
    dir_name = 'output'

    # 创建文件夹（如果不存在的话）
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # 将文件路径与文件夹结合
    full_path = os.path.join(dir_name, out_put_name)

    # 在指定的文件夹中写入文件
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(write_file)


def run():
    print('======开始=========')
    out_file('index.vue', template() + script() + style())
    table = tableConfig_generate()
    out_file("tableConfig.jsx", table)
    print('====== 代码生成完成，请到output/ 文件夹中查看 =========')
