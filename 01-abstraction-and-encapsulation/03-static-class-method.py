# -*- encoding: utf-8 -*-
class Human:
    species = "H. sapiens"

    @staticmethod
    def grunt():
        return "*grunt*"

    @classmethod
    def get_species(cls):
        return cls.species


print(Human.grunt())
print(Human.get_species())


# 尝试如果通过实例调用静态方法会怎样？有办法修正吗？
i = Human()
print(i.grunt())

# 尝试如果通过实例调用类方法会怎样？有办法修正吗？
i = Human()
print(i.get_species())

i.species = 'H. neanderthalensis'
print(i.get_species())
print(Human.get_species())
