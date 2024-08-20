from string import Template


# 示例数据
# column_data = [
#     ('用户', 'user'),
#     ('入职日期', 'hireDate'),
#     ('合同签订开始时间', 'contractStart'),
#     ('第几次续签', 'renewalCount'),
#     ('续签方式', 'renewalMethod')
# ]
def generate_columns(column_data):
    columns_string = ",\n    ".join(
        "{{ title: '{label}', key: '{key}' , width:110 }}".format(label=item['label'], key=item['key']) for item in column_data
    )
    table_config_template = Template("""export const createColumns = ({ handleDelete, handleEdit }) => {
      return [
        { type: 'selection', width: 50 },
        ${columns_string},
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
    """)
    return table_config_template.substitute(columns_string=columns_string)
