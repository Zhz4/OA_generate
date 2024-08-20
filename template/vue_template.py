from string import Template

# filter_wrap 模版 -- form_item,tool_wrap
filter_wrap_template = Template("""
    <div class="filter_wrap">
      <n-form ref="formRef" inline :label-width="100" :model="searchParams" label-placement="left">
        ${form_item}
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
      ${tool_wrap}
    </div>
""")

# form_item 模版 -- form_item_label
form_item_template = Template("""<n-form-item label="${form_item_label}">
  <n-input v-model:value="searchParams.${form_item_key}" type="text" />
</n-form-item>
""")

# tool_wrap 模版 -- tool_wrap
tool_wrap_template = Template("""
<div class="tool_wrap">
    <div class="btn_wrap">
    ${tool_wrap}
    </div>
</div>
""")

# button 模版 --- button_name
button_template = Template("""<n-button type="primary" :loading="loading" @click="${handler}">
    <template #icon>
      <n-icon :component="${icon_component}" />
    </template>
    ${button_name}
</n-button>
""")

# 分页
table_page = """
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
"""

# 主要模版-main
main_template = Template("""
<template>
  <div class="page_container">
  ${main}
  </div>
</template>
""")

