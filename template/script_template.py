from string import Template

# script模版
# 导入模版
import_icon_template = Template("""import { ${importIcon} } from '@vicons/ionicons5'
""")
import_column_template = Template(""" import { createColumns } from './tableConfig.jsx' 
""")
# hooks 模版
hooks_template = Template(""" import { usePageSearch } from '@/hooks/pageSearch' 
""")

# script基本模版
script_main_template = Template(""" 
<script setup>
${import_template}

 const searchParams = ref({})
const columns = ref(createColumns({handleDelete, handleEdit}))
const minXScroll = computed(() => {
  const cols = columns.value || []
  const colsWidth = cols.reduce((pre, cur) => pre + (cur.width || cur.minWidth || 100), 0)
  return colsWidth
})

/**
 * 删除
 */
function handleDelete(row){
    console.log("删除")
    console.log(row)
}

/**
 * 编辑
 */
function handleEdit(row){
    console.log("编辑")
    console.log(row)
}

${other_template}
</script>
 """)

# 搜索逻辑
search_template = Template("""
/**
 * 搜索相关
 */
 // const { loading, tableData, total, searchParams, handleSearch, queryData, resetForm } = usePageSearch(getInStockList, {
 //   page: 1,
 //   size: 20
 // })
""")

# 工具函数模版
tool_handler_template = Template("""
/**
 * ${handlerName}
 */
function ${handler}(){
    console.log("${handlerName}")
}
""")
