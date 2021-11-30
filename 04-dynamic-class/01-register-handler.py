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


# ^ framework source code
# --------------------x8-------------------------
# v user source code


class IndexHandler:
    path = '/index'


class BlogHandler:
    path = '/blog'


register(IndexHandler.path, IndexHandler)
register(BlogHandler.path, BlogHandler)

show_banner()
list_handlers()
