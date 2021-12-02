class MyBoundMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return lambda *args, **kwargs: self.func(instance, *args, **kwargs)


class MyClassMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return lambda *args, **kwargs: self.func(owner, *args, **kwargs)


class MyStaticMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return lambda *args, **kwargs: self.func(*args, **kwargs)


def func(param1, param2):
    print("-" * 20)
    print(f'{param1=}')
    print(f'{param2=}')


class A:
    bound_method = MyBoundMethod(func)
    class_method = MyClassMethod(func)
    static_method = MyStaticMethod(func)

    @MyClassMethod
    def real_class_method(cls, param):
        print("-" * 20)
        print('calling a real class method')
        print(f'{cls=}')
        print(f'{param=}')


a = A()
a.bound_method('parameter')
a.class_method('parameter')
a.static_method('parameter A', 'parameter B')

a.real_class_method('parameter')
