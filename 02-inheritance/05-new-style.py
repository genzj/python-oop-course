# -*- encoding: utf-8 -*-

class Base(object):
    def x(self):
        print('in Base class')


class A(Base):
    # def x(self):
    #     print('in A class, call super().x()')
    #     super().x()
    pass


class B(Base):
    def x(self):
        print('in B class')


class C(A, B):
    pass


C().x()

# cannot be defined:
# class D(A, Base, B):
#     pass
