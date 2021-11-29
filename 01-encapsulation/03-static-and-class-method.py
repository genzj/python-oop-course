class IndexHandler:
    path = "/index"

    def bound_get_path(self):
        return IndexHandler.path

    @staticmethod
    def static_get_path():
        return IndexHandler.path

    @classmethod
    def class_get_path(cls):
        return cls.path


print('=' * 20)
print(f'{IndexHandler.static_get_path()=}')
print(f'{IndexHandler.class_get_path()=}')

handler = IndexHandler()
print(f'{handler.bound_get_path()=}')
print(f'{handler.static_get_path()=}')
print(f'{handler.class_get_path()=}')
