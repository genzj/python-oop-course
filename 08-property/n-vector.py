# -*- encoding: utf-8 -*-
class NVector:
    ITEM_NAMES = ['x', 'y', 'z']

    def __init__(self, *args):
        self.v = list(args)

    def __mul__(self, other):
        assert len(self.v) == len(other.v), 'vectors must be in same dimension'
        ans = 0
        for i in range(len(self.v)):
            ans += self.v[i] * other.v[i]
        return ans

    def __add__(self, other):
        assert len(self.v) == len(other.v), 'vectors must be in same dimension'
        ans = []
        for i in range(len(self.v)):
            ans.append(self.v[i] + other.v[i])
        return NVector(*ans)

    def __str__(self):
        return str(self.v)

    def __getattr__(self, item):
        if item not in self.ITEM_NAMES:
            raise AttributeError()
        idx = self.ITEM_NAMES.index(item)
        return self.v[idx]

    def __setattr__(self, name, value):
        if name not in self.ITEM_NAMES:
            super().__setattr__(name, value)
            return
        idx = self.ITEM_NAMES.index(name)
        self.v[idx] = value


v1 = NVector(1, 2, 3)
v2 = NVector(-3, -2, -1)
s = v1 + v2
print(str(s))

m = v1 * v2
print(m)

print(s.x, s.y, s.z)
s.x = 1000
print(s.x, s.y, s.z)
