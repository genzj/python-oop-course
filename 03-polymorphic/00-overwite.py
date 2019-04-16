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


class Superhero(Human):
    # 子类继承基类的所有方法，但方法可以被重写，如增加参数
    def __init__(self, name, movie=False,
                 superpowers=("super strength", "bulletproofing")):
        # add additional class attributes:
        self.fictional = True
        self.movie = movie
        self.superpowers = superpowers
        # 可以使用super调用父类的方法
        super().__init__(name)


sup = Superhero(name="Tick")
print(sup.name)
print(sup.superpowers)
