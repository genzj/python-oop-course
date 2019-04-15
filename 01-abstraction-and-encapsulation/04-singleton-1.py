# -*- encoding: utf-8 -*-

class A:
    singleton = None

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<%s id=0x%08x name=%s>' % (self.__class__.__qualname__, id(self), self.name)

    @staticmethod
    def get_singleton():
        if A.singleton is None:
            A.singleton = A('singleton')
            print('Singleton %r created' % (A.singleton,))
        return A.singleton


print('A singleton 1:', A.get_singleton())
print('A singleton 2:', A.get_singleton())


class B(A):
    singleton = None


print('B singleton 1:', B.get_singleton())
print('B singleton 2:', B.get_singleton())
