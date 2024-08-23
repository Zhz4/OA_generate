from string import Template


# 默认api接口模板
def main_template(url, method, handlerName, remark):
    template = Template("""
        // ${remark}
        export const ${handlerName} = data => {
          return service.request({
            url: '${url}',
            method: '${method}',
            data
          })
        }
    """)
    return template.substitute(url=url, method=method, handlerName=handlerName, remark=remark)
