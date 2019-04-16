# -*- encoding: utf-8 -*-
class C:
    def __init__(self):
        self._x = 0

    @property
    def x(self):
        print('in c.x getter')
        return self._x

    @x.setter
    def x(self, value):
        print('in c.x setter')
        self._x = value if value >= 0 else 0


c = C()
print(c.x)
c.x = -10
print(c.x)
c.x = 10
print(c.x)
