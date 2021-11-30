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
    pass


def new_handler(cls):
    assert cls.path, f'path property of {cls} should not be empty'
    new_class = type(
        f'{cls.__name__}Registration', (BaseHandler, cls), {'registered': True}
    )
    register(new_class.path, new_class)
    return new_class


# ^ framework source code
# --------------------x8-------------------------
# v user source code


class IndexHandler:
    path = '/index'


class BlogHandler:
    path = '/blog'


IndexHandlerRegistration = new_handler(IndexHandler)
BlogHandlerRegistration = new_handler(BlogHandler)
show_banner()
list_handlers()
