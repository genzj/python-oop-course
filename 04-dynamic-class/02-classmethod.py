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


class BaseHandler:
    path = ''

    @classmethod
    def register(cls):
        assert cls.path, f'path property of {cls} should not be empty'
        register(cls.path, cls)


# ^ framework source code
# --------------------x8-------------------------
# v user source code


class IndexHandler(BaseHandler):
    path = '/index'


class BlogHandler(BaseHandler):
    path = '/blog'


IndexHandler.register()
BlogHandler.register()


show_banner()
list_handlers()
