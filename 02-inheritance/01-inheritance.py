# -*- encoding: utf-8 -*-
class Human:
    species = "H. sapiens"

    def __init__(self, name):
        # 实例方法第一个参数为self，指代当前实例
        # 根据参数初始化实例属性
        self.name = name

        # 也可以用常量等初始化实例属性
        self._age = 0

    @classmethod
    def get_species(cls):
        return cls.species

    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))


# 定义类时用括号包裹基类，可以多继承
class Superhero(Human):
    # 子类可以覆盖基类的类属性
    species = 'Superhuman'


sup = Superhero(name="Tick")
print(sup.get_species())  # => Superhuman
