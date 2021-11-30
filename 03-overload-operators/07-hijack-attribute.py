class BaseHandler:
    def handle(self, method):
        raise NotImplementedError

    def __getattribute__(self, attr: str):
        if attr == 'forbidden':
            raise AttributeError(f'attribute {attr} is not allowed')
        return super().__getattribute__(attr)

    def __getattr__(self, attr):
        if attr in {'get', 'post', 'put', 'patch', 'delete'}:
            return lambda: self.handle(method=attr)
        raise AttributeError(f'{self} does not have attribute {attr}')


class IndexHandler(BaseHandler):
    forbidden = 'test'

    def get(self):
        print('GET /index')

    def handle(self, method):
        print(f'handle {method.upper()} /index')


print('=' * 20)

handler = IndexHandler()
handler.get()
handler.post()
print(f'{IndexHandler.forbidden=}')
# 以下语句会抛出异常
# print(f'{handler.forbidden=}')
