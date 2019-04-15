class A(object):
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


print(B.p)
B.c()
B.s()
B().__len__()
len(B())
print(B.__z__)

print(dir(A))
print(dir(B))

# not work
# print(B.__y)

