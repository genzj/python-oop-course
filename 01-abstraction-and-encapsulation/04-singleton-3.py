# -*- encoding: utf-8 -*-
import time
from threading import Thread


class A(object):
    singleton = None

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<%s id=0x%08x name=%s>' % (self.__class__.__qualname__, id(self), self.name)

    @classmethod
    def get_singleton(cls):
        if cls.singleton is None:
            time.sleep(1)
            cls.singleton = cls('singleton')
            print('Singleton %r created' % (cls.singleton,))
        return cls.singleton


def print_singleton(idx):
    print('A singleton ', idx, A.get_singleton())


Thread(target=print_singleton, args=[1,]).start()
Thread(target=print_singleton, args=[2,]).start()

