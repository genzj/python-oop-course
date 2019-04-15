# -*- encoding: utf-8 -*-

class A(object):
    singleton = None

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<%s id=0x%08x name=%s>' % (self.__class__.__qualname__, id(self), self.name)

    @classmethod
    def get_singleton(cls):
        if cls.singleton is None:
            cls.singleton = cls('singleton')
            print('Singleton %r created' % (cls.singleton,))
        return cls.singleton


print('A singleton 1:', A.get_singleton())
print('A singleton 2:', A.get_singleton())


class B(A):
    singleton = None


print('B singleton 1:', B.get_singleton())
print('B singleton 2:', B.get_singleton())
