# 前端新后台代码生成器
## 前言
为什么要写这个程序？  
在写OA后台的时候会发现其实很多工作都**是重复性的**，后台的格式，模版基本都是大差不差，区别只是在**业务逻辑**上的不同。因此，像这些重复性的工作，其实可以让程序一键生成，我们只需要关注业务逻辑本身，修改逻辑代码，大大提高了工作效率，减少重复性工作
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
## 根据配置文件生成的代码展示

1. config.json
```json
{
  "_comment": "这个配置文件包含用户相关的标签和工具按钮",
  "form_item_list": [
    {
      "label": "工号",
      "key": "user"
    },
    {
      "label": "姓名",
      "key": "user"
    },
    {
      "label": "部门",
      "key": "user"
    },
    {
      "label": "职位",
      "key": "user"
    },
    {
      "label": "入职时间",
      "key": "user"
    },
    {
      "label": "是否在职",
      "key": "user"
    }
  ],
  "tool_button_list": [
    {
      "button_name": "导入数据",
      "handler": "handleInput",
      "icon_component": "ArrowDownCircleOutline"
    },
    {
      "button_name": "导出数据",
      "handler": "handleExport",
      "icon_component": "ArrowDownCircleOutline"
    },
    {
      "button_name": "批量删除",
      "handler": "handleBatchDelete",
      "icon_component": "ArrowDownCircleOutline"
    },
    {
      "button_name": "批量修改",
      "handler": "handleBatchEdit",
      "icon_component": "ArrowDownCircleOutline"
    }
  ],
  "table_list": [
    {
      "label": "工号",
      "key": "user"
    },
    {
      "label": "姓名",
      "key": "hireDate"
    },
    {
      "label": "部门",
      "key": "contractStart"
    },
    {
      "label": "职位",
      "key": "renewalCount"
    },
    {
      "label": "入职日期",
      "key": "renewalMethod"
    },
    {
      "label": "最近续签状态",
      "key": "renewalMethod"
    },
    {
      "label": "第一次劳动合同期限",
      "key": "renewalMethod"
    },
    {
      "label": "第二次劳动合同期限",
      "key": "renewalMethod"
    },
    {
      "label": "第三次劳动合同期限",
      "key": "renewalMethod"
    },
    {
      "label": "第四次劳动合同期限",
      "key": "renewalMethod"
    },
    {
      "label": "第五次劳动合同期限",
      "key": "renewalMethod"
    },
    {
      "label": "备注",
      "key": "renewalMethod"
    }
  ]
}

```

2. output/index.vue
```vue
<template>
  <div class="page_container">
    <div class="filter_wrap">
      <n-form ref="formRef" inline :label-width="100" :model="searchParams" label-placement="left">
        <n-form-item label="工号">
          <n-input v-model:value="searchParams.user" type="text" />
        </n-form-item>
        <n-form-item label="姓名">
          <n-input v-model:value="searchParams.user" type="text" />
        </n-form-item>
        <n-form-item label="部门">
          <n-input v-model:value="searchParams.user" type="text" />
        </n-form-item>
        <n-form-item label="职位">
          <n-input v-model:value="searchParams.user" type="text" />
        </n-form-item>
        <n-form-item label="入职时间">
          <n-input v-model:value="searchParams.user" type="text" />
        </n-form-item>
        <n-form-item label="是否在职">
          <n-input v-model:value="searchParams.user" type="text" />
        </n-form-item>
        <n-form-item>
          <n-button type="primary" :loading="loading" @click="handleSearch">
            <template #icon>
              <n-icon :component="Search" />
            </template>
            搜索
          </n-button>
          <n-button style="margin-left: 10px" @click="resetForm">重置</n-button>
        </n-form-item>
      </n-form>

      <div class="tool_wrap">
        <div class="btn_wrap">
          <n-button type="primary" :loading="loading" @click="handleInput">
            <template #icon>
              <n-icon :component="ArrowDownCircleOutline" />
            </template>
            导入数据
          </n-button>
          <n-button type="primary" :loading="loading" @click="handleExport">
            <template #icon>
              <n-icon :component="ArrowDownCircleOutline" />
            </template>
            导出数据
          </n-button>
          <n-button type="primary" :loading="loading" @click="handleBatchDelete">
            <template #icon>
              <n-icon :component="ArrowDownCircleOutline" />
            </template>
            批量删除
          </n-button>
          <n-button type="primary" :loading="loading" @click="handleBatchEdit">
            <template #icon>
              <n-icon :component="ArrowDownCircleOutline" />
            </template>
            批量修改
          </n-button>
        </div>
      </div>
    </div>

    <div class="table_wrap">
      <n-data-table
        class="page_table"
        :columns="columns"
        :single-line="false"
        :data="tableData"
        :row-key="row => row.id"
        :scroll-x="minXScroll"
        flex-height
      ></n-data-table>
    </div>
    <div class="page_wrap">
      <n-pagination
        v-model:page="searchParams.page"
        v-model:page-size="searchParams.size"
        :item-count="total"
        show-size-picker
        :page-sizes="[20, 50, 100]"
        @update:page="queryData()"
        @update:page-size="queryData()"
      >
        <template #prefix="{ itemCount }">共 {{ itemCount }} 条</template>
      </n-pagination>
    </div>
  </div>
</template>

<script setup>
import { ArrowDownCircleOutline, Search } from '@vicons/ionicons5'
import { createColumns } from './tableConfig.jsx'
import { usePageSearch } from '@/hooks/pageSearch'

const searchParams = ref({})
const columns = ref(createColumns({ handleDelete, handleEdit }))
const minXScroll = computed(() => {
  const cols = columns.value || []
  const colsWidth = cols.reduce((pre, cur) => pre + (cur.width || cur.minWidth || 100), 0)
  return colsWidth
})

/**
 * 删除
 */
function handleDelete(row) {
  console.log('删除')
  console.log(row)
}

/**
 * 编辑
 */
function handleEdit(row) {
  console.log('编辑')
  console.log(row)
}

/**
 * 搜索相关
 */
// const { loading, tableData, total, searchParams, handleSearch, queryData, resetForm } = usePageSearch(getInStockList, {
//   page: 1,
//   size: 20
// })

/**
 * 导入数据
 */
function handleInput() {
  console.log('导入数据')
}

/**
 * 导出数据
 */
function handleExport() {
  console.log('导出数据')
}

/**
 * 批量删除
 */
function handleBatchDelete() {
  console.log('批量删除')
}

/**
 * 批量修改
 */
function handleBatchEdit() {
  console.log('批量修改')
}
</script>

<style lang="scss" scoped>
@import '@/style/tablePage.scss';
</style>

```

2. output/tableConfig.jsx
```jsx
export const createColumns = ({ handleDelete, handleEdit }) => {
  return [
    { type: 'selection', width: 50 },
    { title: '工号', key: 'user', width: 110 },
    { title: '姓名', key: 'hireDate', width: 110 },
    { title: '部门', key: 'contractStart', width: 110 },
    { title: '职位', key: 'renewalCount', width: 110 },
    { title: '入职日期', key: 'renewalMethod', width: 110 },
    { title: '最近续签状态', key: 'renewalMethod', width: 110 },
    { title: '第一次劳动合同期限', key: 'renewalMethod', width: 110 },
    { title: '第二次劳动合同期限', key: 'renewalMethod', width: 110 },
    { title: '第三次劳动合同期限', key: 'renewalMethod', width: 110 },
    { title: '第四次劳动合同期限', key: 'renewalMethod', width: 110 },
    { title: '第五次劳动合同期限', key: 'renewalMethod', width: 110 },
    { title: '备注', key: 'renewalMethod', width: 110 },
    {
      title: '操作',
      key: '',
      fixed: 'right',
      width: 170,
      render(row) {
        return (
          <div className="table_btn_wrap">
            <NButton text type="primary" onClick={() => handleEdit(row)}>
              编辑
            </NButton>
            <n-popconfirm onPositiveClick={() => handleDelete(row)}>
              {{
                trigger: () => (
                  <NButton text type="error">
                    删除
                  </NButton>
                ),
                default: () => '是否确认删除数据'
              }}
            </n-popconfirm>
          </div>
        )
      }
    }
  ]
}

```

## 
