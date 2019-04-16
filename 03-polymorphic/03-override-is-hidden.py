# -*- encoding: utf-8 -*-
class A:
    def func1(self):
        print('in A.func1')


class B(A):
    def func1(self):
        print('in B.func1')


a = A()
b = B()
a.func1()
b.func1()

print('-' * 40)

A.func1(b)
super(B, b).func1()

print('-' * 40)

for cls in B.mro():
    if hasattr(cls, 'func1'):
        cls.func1(b)
