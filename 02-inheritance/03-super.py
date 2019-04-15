# -*- encoding: utf-8 -*-

class A(object):
    cls_int = 1

    def method(self):
        print('in A.method', self)

    @staticmethod
    def static_method():
        print('in A.static_method')

    @classmethod
    def class_method(cls):
        print('in A.class_method', cls)
        print('cls_int =', cls.cls_int)


class B(A):
    cls_int = 2

    def method_1(self):
        A.method(self)

    def method_2(self):
        super(B, self).method()

    def method_3(self):
        super().method()

    @staticmethod
    def static_method_1():
        A.static_method()

    @staticmethod
    def static_method_2():
        super(__class__, __class__).static_method()

    @classmethod
    def class_method_1(cls):
        A.class_method()

    @classmethod
    def class_method_2(cls):
        A.__dict__['class_method'].__get__(None, cls)()

    @classmethod
    def class_method_3(cls):
        super(B, cls).class_method()


b = B()
b.method_1()
b.method_2()
b.method_3()
B.static_method_1()
B.static_method_2()
B.class_method_1()
B.class_method_2()
B.class_method_3()

print('-' * 40)

B.parent = super(B)
b.parent.method()
b.parent.static_method()
b.parent.class_method()
