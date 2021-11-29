class A:
    def m(self):
        print('in class A')


class B(A):
    def m(self):
        print('in class B')


class C(A):
    def m(self):
        print('in class C')


class D(B, C):
    def m(self):
        A.m(self)
        B.m(self)
        C.m(self)
        print('in class D')


print('=' * 20)
d = D()
d.m()


class E:
    def m(self):
        print('in a separate class E')


def call_m(obj):
    return obj.m()


print('# 鸭规则')
e = E()
call_m(d)
call_m(e)
