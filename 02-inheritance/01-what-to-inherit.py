class A:
    p = 1
    __y = 2
    __z__ = 3

    def __len__(self):
        print('__x__')
        return 0

    @staticmethod
    def s():
        print('s')

    @classmethod
    def c(cls):
        print('c')


class B(A):
    pass


print('=' * 20)
print(f'{B.p=}')
B.c()
B.s()

b = B()
b.__len__()
len(b)
print(f'{B._A__y=}')
print(f'{B.__z__=}')
print(f'{b.p=}')

print('=' * 20)
print(f'{A.__dict__=}')
print(f'{B.__dict__=}')
print(f'{b.__dict__=}')

print('=' * 20)
print('# Method Resolution Order(MRO)')
print(f'{B.__mro__=}')
