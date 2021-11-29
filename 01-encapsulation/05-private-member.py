class IndexHandler:
    __path = '/index'

    def __init__(self) -> None:
        self.__db = 'database'

    def get(self):
        print(f'{IndexHandler.__path} {self.__path=} {self.__db=}')


print('=' * 20)
handler = IndexHandler()
handler.get()

# 下面三个语句都无法执行
# print(IndexHandler.__path)
# print(handler.__path)
# print(handler.__db)

print('# 私有变量被解释器自动加上了前缀')
print(IndexHandler.__dict__)
print(handler.__dict__)
print('# 了解机制后任然可以访问私有变量')
print(f'{IndexHandler._IndexHandler__path=}')
print(f'{handler._IndexHandler__path=}')
print(f'{handler._IndexHandler__db=}')
