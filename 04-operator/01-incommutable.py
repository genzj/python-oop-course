class A(object):
    def __init__(self, i):
        self.i = i

    def __add__(self, other):
        if isinstance(other, A):
            return A(self.i + other.i)
        else:
            return A(self.i + other)

    def __repr__(self):
        return '<A %s>' % (self.i,)


print(A(1) + A(2))
print(A(2) + A(1))
print(A(1) + 2)

# not work!
# print(2 + A(1))
