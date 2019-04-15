# -*- encoding: utf-8 -*-

class Base:
    def x(self):
        print('in Base class')


class A(Base):
    pass


class B(Base):
    def x(self):
        print('in B class')


class C(A, B):
    pass


C().x()
