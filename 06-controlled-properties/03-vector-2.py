# -*- encoding: utf-8 -*-
class Vector:
    def __init__(self, x, y):
        self.v = [x, y]

    @property
    def x(self):
        return self.v[0]

    @x.setter
    def x(self, n):
        self.v[0] = n

    @property
    def y(self):
        return self.v[1]

    @y.setter
    def y(self, n):
        self.v[1] = n

    def __add__(self, other):
        return Vector(self.v[0] + other.v[0], self.v[1] + other.v[1])

    def __mul__(self, other):
        return self.v[0] * other.v[0] + self.v[1] * other.v[1]


v1 = Vector(1, 1)
v2 = Vector(-1, -1)
s = v1 + v2
print(s.x, s.y)

m = v1 * v2
print(m)
