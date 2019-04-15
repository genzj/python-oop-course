# -*- encoding: utf-8 -*-
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y


v1 = Vector(1, 1)
v2 = Vector(-1, -1)
s = v1 + v2
print(s.x, s.y)

m = v1 * v2
print(m)
