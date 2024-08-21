from string import Template


# vue部分
# 主要的model
def mainModel(main_template):
    template = Template("""
    <template>
        <n-modal v-model:show="show" class="edit_model" preset="dialog" title="编辑" :show-icon="false" @after-leave="close">
        ${main_template}
            <template #action>
              <n-button :loading="loading" @click="close">取消</n-button>
              <n-button type="primary" :loading="loading" @click="handleSubmit">
                <template #icon>
                  <n-icon :component="ArrowUpOutline" />
                </template>
                保存
              </n-button>
            </template>
        </n-modal>
    </template>
    """)
    return template.substitute(main_template=main_template)


# form
def form_template(replace):
    template = Template("""<n-form ref="formRef" class="dialog_form" :label-width="110" :model="form" :rules="rules" label-placement="left" label-align="left">
        ${replace}
     </n-form>""")
    return template.substitute(replace=replace)


# form-item
def form_item_template(label, value):
    template = Template("""<n-form-item label="${label}" path="${value}">
        <n-input v-model:value="form.${value}" type="text" />
      </n-form-item>
    """)
    return template.substitute(label=label, value=value)


# script 部分
def script_main_template():
    template = Template("""
    <script setup>
        import { ArrowUpOutline } from '@vicons/ionicons5'
        
        const show = ref(false)
        const form = ref({})
        
        const emit = defineEmits(['success'])
        
        /**
         * 提交
         */
        function handleSubmit() {
          console.log("提交")
          emit('success')
        }
        
        defineExpose({
          open
        })
        function open(row = {}) {
          show.value = true
          form.value = { ...row }
        }
        function close() {
          show.value = false
        }
    </script>
    """)
    return template.substitute()
