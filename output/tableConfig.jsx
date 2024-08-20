export const createColumns = ({ handleDelete, handleEdit }) => {
      return [
        { type: 'selection', width: 50 },
        { title: '工号', key: 'user' , width:110 },
    { title: '姓名', key: 'hireDate' , width:110 },
    { title: '部门', key: 'contractStart' , width:110 },
    { title: '职位', key: 'renewalCount' , width:110 },
    { title: '入职日期', key: 'renewalMethod' , width:110 },
    { title: '最近续签状态', key: 'renewalMethod' , width:110 },
    { title: '第一次劳动合同期限', key: 'renewalMethod' , width:110 },
    { title: '第二次劳动合同期限', key: 'renewalMethod' , width:110 },
    { title: '第三次劳动合同期限', key: 'renewalMethod' , width:110 },
    { title: '第四次劳动合同期限', key: 'renewalMethod' , width:110 },
    { title: '第五次劳动合同期限', key: 'renewalMethod' , width:110 },
    { title: '备注', key: 'renewalMethod' , width:110 },
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
    