from core.core import run
from core.edit_generate import run as edit_run

if __name__ == '__main__':
    # 生成主要代码
    run()
    # 生成EditModal代码
    edit_run()
