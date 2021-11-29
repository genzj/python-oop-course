class Vector:
    def __init__(self, *args):
        self.pts = tuple(args)

    def __add__(self, other):
        if isinstance(other, Vector) and len(self.pts) == len(other.pts):
            return Vector(*[i + j for i, j in zip(self.pts, other.pts)])
        raise NotImplementedError()

    def __mul__(self, other):
        if isinstance(other, Vector):
            return sum([i * j for i, j in zip(self.pts, other.pts)])
        raise NotImplementedError()

    def __repr__(self):
        return f'Vector{self.pts}'


print('=' * 20)
v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(f'{v1 + v2=}')
print(f'{v1 * v2=}')

print('=' * 20)
v1 = Vector(1, 2, 3, 4)
v2 = Vector(5, 6, 7, 8)

print(f'{v1 + v2=}')
print(f'{v1 * v2=}')
