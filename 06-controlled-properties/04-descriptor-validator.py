# -*- encoding: utf-8 -*-
class ValidatedProperty:
    def __init__(self, initial, min, max):
        self.max = max
        self.min = min
        self.initial = initial
        self.name = None

    def func(self):
        print('calling func of', self)

    def __set_name__(self, owner, name):
        self.name = '_validated_' + name

    def __get__(self, instance, owner):
        # print('in getter', instance, owner)
        return getattr(instance, self.name, self.initial)

    def __set__(self, instance, value):
        # print('in setter', instance, value)
        if value <= self.max and value >= self.min:
            setattr(instance, self.name, value)

    def __delete__(self, instance):
        print('in deleter', instance)
        if hasattr(instance, self.name):
            delattr(instance, self.name)


class A:
    a = ValidatedProperty(0, min=0, max=10)
    b = ValidatedProperty(0, min=-10, max=0)


a = A()
print('initial values: a =', a.a, ', b =', a.b)

a.a = 5
a.b = -5
print('after valid value settings: a =', a.a, ', b =', a.b)

a.a = 50
a.b = 100
print('after invalid value settings: a =', a.a, ', b =', a.b)

# print(dir(a))

del a.a
del a.b
print('after delete / resetting: a =', a.a, ', b =', a.b)

# a.a.func()
# A.a.func()
A.__dict__['a'].func()
A.__dict__['b'].func()
