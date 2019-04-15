# -*- encoding: utf-8 -*-
import time
from threading import Thread, Lock


class SingletonMeta(type):
    lock = Lock()
    singletons = {}

    def __call__(cls, *args, **kwargs):
        if cls in cls.singletons:
            return cls.singletons[cls]

        with SingletonMeta.lock:
            if cls not in cls.singletons:
                time.sleep(1)
                cls.singletons[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
            return cls.singletons[cls]


class Singleton(metaclass=SingletonMeta):
    pass


class A(Singleton):

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<%s id=0x%08x name=%s>' % (self.__class__.__qualname__, id(self), self.name)


def print_singleton_a(idx):
    print('A singleton ', idx, A('singleton'))


class B(A):
    pass


def print_singleton_b(idx):
    print('B singleton ', idx, B('singleton'))


Thread(target=print_singleton_a, args=[1, ]).start()
Thread(target=print_singleton_a, args=[2, ]).start()
Thread(target=print_singleton_b, args=[1, ]).start()
Thread(target=print_singleton_b, args=[2, ]).start()
