# -*- encoding: utf-8 -*-


# 使用class关键字定义一个类
class Human:
    # 定义一个类属性
    species = "H. sapiens"


i = Human()
print(i.species)
Human.species = "H. neanderthalensis"
print(i.species)  # 类属性的共享性
