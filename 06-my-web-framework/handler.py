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


class MetaHandler(type):
    def __new__(cls, name, bases, namespace, **kwargs):
        # 元类里可以对具体类进行修改
        namespace.pop('forbidden', None)

        # 一定要记得调用父元类方法创建新的具体类
        new_class = super().__new__(cls, name, bases, namespace)

        if bases != tuple() and bases != (object,):
            assert (
                hasattr(new_class, 'path') and new_class.path
            ), f'path property of {name} should not be empty'
            register(new_class.path, new_class)

        return new_class


class BaseHandler(metaclass=MetaHandler):
    def handle(self, method, data):
        raise NotImplementedError

    def __getattr__(self, attr):
        if attr in {'get', 'post', 'put', 'patch', 'delete'}:
            return lambda data: self.handle(method=attr, data=data)
        raise AttributeError(f'{self} does not have attribute {attr}')
