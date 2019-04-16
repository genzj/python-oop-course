# -*- encoding: utf-8 -*-
from functools import wraps


def not_implemented(f):
    @wraps(f)
    def _f(*args, **kwargs):
        raise NotImplementedError()

    _f._not_implemented = True
    return _f


class Bird:
    color = None

    @not_implemented
    def fly(self):
        pass


class Swallow(Bird):
    color = 'black & white'

    def fly(self):
        print('%r can fly' % (self,))


class Ostrich(Bird):
    color = 'grey & brown'


print(Swallow().color)
Swallow().fly()
print(Ostrich().color)


# not work
# Ostrich().fly()


def flyable(instance):
    return hasattr(instance, 'fly') and not getattr(instance.fly, '_not_implemented', False)


print('swallow can fly:', flyable(Swallow()))
print('ostrich can fly:', flyable(Ostrich()))
