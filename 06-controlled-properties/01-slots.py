# -*- encoding: utf-8 -*-
class A:
    __slots__ = ('a', 'b')
    def __init__(self):
        self.a = 1
        self.b = 2

a = A()
print(a.a, a.b)

# a.c = 100
