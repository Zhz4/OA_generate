from comment.comment import getConfig, out_file
from template.api_template import main_template

config = getConfig('./config/main_config.json')


def run():
    import_template = """
    import service from '@/utils/request/index'
    """
    template = ''
    for item in config["apiList"]:
        template += main_template(url=item['url'], method=item['method'], handlerName=item['handlerName'],
                                  remark=item['remark'])
    if config["apiFileName"] != '':
        out_file('api', config["apiFileName"] + '.js', import_template + template)
