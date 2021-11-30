def show_banner():
    print('-' * 50)
    print(
        r'''
___  ____   __ ________   __  _    _ ___________ 
|  \/  \ \ / / | ___ \ \ / / | |  | |  ___| ___ \
| .  . |\ V /  | |_/ /\ V /  | |  | | |__ | |_/ /
| |\/| | \ /   |  __/  \ /   | |/\| |  __|| ___ \
| |  | | | |   | |     | |   \  /\  / |___| |_/ /
\_|  |_/ \_/   \_|     \_/    \/  \/\____/\____/ 
'''
    )
    print('-' * 50)


registry = dict()


def register(path, handler):
    registry[path] = handler


def list_handlers():
    print('Registered handlers:')
    for path in sorted(registry):
        print(f'  {path} -> {registry[path]}')


class BaseHandler():
    path = ''

    def __init_subclass__(cls, **kwargs):
        # 一定要记得调用父类的相同方法，以支持链式钩子
        super().__init_subclass__(**kwargs)
        assert cls.path, f'path property of {cls} should not be empty'
        register(cls.path, cls)


# ^ framework source code
# --------------------x8-------------------------
# v user source code


class IndexHandler(BaseHandler):
    path = '/index'
    forbidden = 'test'

    def get(self):
        pass


class BlogHandler(BaseHandler):
    path = '/blog'


show_banner()
list_handlers()
