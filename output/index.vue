
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
import { Search,ArrowDownCircleOutline } from '@vicons/ionicons5'
 import { createColumns } from './tableConfig.jsx' 
 import { usePageSearch } from '@/hooks/pageSearch' 


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
function handleInput(){
    console.log("导入数据")
}

/**
 * 导出数据
 */
function handleExport(){
    console.log("导出数据")
}

/**
 * 批量删除
 */
function handleBatchDelete(){
    console.log("批量删除")
}

/**
 * 批量修改
 */
function handleBatchEdit(){
    console.log("批量修改")
}

</script>
 
<style lang="scss" scoped>
@import '@/style/tablePage.scss';
</style>
