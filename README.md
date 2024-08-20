# 前端新后台代码生成器
## 前言
为什么要写这个程序？  
在写OA后台的时候会发现其实很多工作都是重复性的，后台的格式，模版基本都是大差不差，区别只是在业务逻辑上的不同。因此，像这些重复性的工作，其实可以让程序一键生成，我们只需要关注业务逻辑本身，通过逻辑修改代码，大大提高了工作效率，减少重复性工作
## 使用说明
只需要在配置文件中加入自己需要的内容即可
```json
{
  "form_item_list":[
    {
      "label": "工号",
      "key": "user"
    }
  ], // 搜索筛选项
  "tool_button_list":[
    {
      "button_name": "导入数据", // 按钮名称
      "handler": "handleInput", // 事件函数名称
      "icon_component": "ArrowDownCircleOutline" // icon名称
    } // 工具行
  ],
  "table_list":[
    {
      "label": "工号",
      "key": "user"
    } // jsx中表格字段
  ]
}
```
运行 `index.py `文件，或者执行命令`python index.py`便可以生成代码
生成的代码位于`output`文件夹中
包含 `index.vue`和`tableConfig.jsx `文件，只需要将该文件复制粘贴到后台项目中便可以执行
注意：代码是没有进行格式化的（但任然不影响阅读），因此需要在vscode中格式化一下代码（最好！）

## 待更新内容

- 搜索筛选项中目前只有 input 模版，后续会加入下拉，时间，部门等常用模版
- 编辑弹窗也是经常会使用到的功能，后续加入编辑弹窗模版
- api文件以及常用增删改查逻辑等...
## 演示
![演示gif](https://cdn.nlark.com/yuque/0/2024/gif/26376404/1724150902921-3a43c14a-729d-4ecb-b4a0-171d91d50a9f.gif)
## 根据配置文件生成的代码展示
[查看代码](./doc/demoCode.md)
