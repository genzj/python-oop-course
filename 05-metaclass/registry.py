# -*- encoding: utf-8 -*-
REGISTRATION = set()


def register(cls):
    REGISTRATION.add(cls.__name__)


def ls():
    print('available commands:')
    print('\n'.join(REGISTRATION))

