class BaseHandler:
    def handle(self, method):
        raise NotImplementedError

    def __getattr__(self, attr):
        if attr in {'get', 'post', 'put', 'patch', 'delete'}:
            return lambda: self.handle(method=attr)
        raise AttributeError(f'{self} does not have attribute {attr}')


class IndexHandler(BaseHandler):
    def get(self):
        print('GET /index')

    def handle(self, method):
        print(f'handle {method.upper()} /index')


print('=' * 20)

handler = IndexHandler()
handler.get()
handler.post()
handler.patch()

# handler.xxx()
