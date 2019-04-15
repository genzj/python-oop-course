# -*- encoding: utf-8 -*-
import time
from threading import Thread, Lock


class Singleton:
    __singleton = {}
    __singleton_lock = Lock()

    @classmethod
    def get_singleton(cls):
        if cls in cls.__singleton:
            return cls.__singleton[cls]

        with cls.__singleton_lock:
            if cls not in cls.__singleton:
                time.sleep(1)
                cls.__singleton[cls] = cls('singleton')
                print('Singleton %r created to %r' % (cls.__singleton[cls], cls.__singleton))
            return cls.__singleton[cls]


class A(Singleton):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<%s id=0x%08x name=%s>' % (self.__class__.__qualname__, id(self), self.name)


def print_singleton_a(idx):
    print('A singleton ', idx, A.get_singleton())


class B(A):
    pass


def print_singleton_b(idx):
    print('B singleton ', idx, B.get_singleton())


Thread(target=print_singleton_a, args=[1, ]).start()
Thread(target=print_singleton_a, args=[2, ]).start()
Thread(target=print_singleton_b, args=[1, ]).start()
Thread(target=print_singleton_b, args=[2, ]).start()
