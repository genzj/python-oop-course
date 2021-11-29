class IndexHandler:
    path = "/index"

    def __init__(self):
        self.db = 'something'

    def post(self, name):
        print(f'handling POST to /index with {name=}')
        return 200, "OK"


print('=' * 20)
handler = IndexHandler()
print(f'{IndexHandler.post=}')
print(f'{handler.post=}')
handler.post('my name')

# 绑定方法一般通过实例调用，下面的调用是错误的
# IndexHandler.post('my name')

print('# 但是只要正确传参，也可以通过类调用绑定方法')
print('=' * 20)
IndexHandler.post(handler, 'my name')

print('# 绑定方法是一种传递self的快捷方式')
