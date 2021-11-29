class IndexHandler:
    path = "/index"

    def __init__(self):
        self.db = 'something'

    def get(self):
        print("handling GET /index")
        return 200, "OK"


print('=' * 20)
print(f'{IndexHandler.path=}')

handler = IndexHandler()
print(f'{handler.path=}')
print(f'{handler.db=}')
print(f'{handler.get()=}')

print('=' * 20)
print('# 修改类属性，所有实例都能看到对应变化')
IndexHandler.registered = False
print(f'{handler.registered=}')

print('=' * 20)
print('# 实例属性能“覆盖”类属性，但只对单个实例有效')
handler.path = "/newpage"
print(f'{handler.path=}')
print(f'{IndexHandler.path=}')
print(f'{IndexHandler().path=}')
