class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise NotImplementedError()

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        raise NotImplementedError()

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'


print('=' * 20)
v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(f'{v1 + v2=}')
print(f'{v1 * v2=}')
