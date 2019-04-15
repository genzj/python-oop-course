# -*- encoding: utf-8 -*-
class A:
    __private = 1

    def print_private(self):
        print('in A.print_private')
        print(self.__private)

    @staticmethod
    def print_private_static():
        print('in A.print_private_static')
        print(A.__private)

    @classmethod
    def print_private_class(cls):
        print('in A.print_private_class')
        print(cls)
        print(cls.__private)


a = A()
a.print_private()
a.print_private_static()
a.print_private_class()

print('-' * 40)


class B(A):
    __private = 2

    # def print_private(self):
    #     super().print_private()
    #
    # @staticmethod
    # def print_private_static():
    #     super(__class__, __class__).print_private_static()
    #
    @classmethod
    def print_private_class(cls):
        super().print_private_class()


b = B()
b.print_private()
b.print_private_static()
b.print_private_class()
