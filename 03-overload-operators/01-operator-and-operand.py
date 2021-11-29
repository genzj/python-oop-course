class A:
    def __init__(self, i):
        self.i = i

    def __add__(self, other):
        if isinstance(other, A):
            return A(self.i + other.i)
        else:
            return A(self.i + other)

    def __repr__(self):
        return f'<A i={self.i}>'


print('=' * 20)
print(A(1) + A(2))
print(A(1) + 2)
# 不满足交换律，因为“2”并没有支持类型A的加法重载
# print(2 + A(1))


def swappable_add(one, two):
    one = one if isinstance(one, A) else A(one)
    two = two if isinstance(two, A) else A(two)
    return one + two


print('# 一个满足交换律的参考实现')
print(swappable_add(A(1), 2))
print(swappable_add(2, A(1)))
print(swappable_add(1, 2))
