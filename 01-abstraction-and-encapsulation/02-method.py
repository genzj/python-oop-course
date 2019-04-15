# -*- encoding: utf-8 -*-
from collections import namedtuple


class Human:
    def __init__(self, name):
        # 实例方法第一个参数为self，指代当前实例
        # 根据参数初始化实例属性
        self.name = name

        # 也可以用常量等初始化实例属性
        self._age = 0

    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))


# 构造函数带参数时，如一般函数那样传参
i = Human("Ian")
# 或
j = Human(name="Joel")

# 调用绑定方法时必须通过实例调用
i.say("hi")
j.say("hello")

# 试试Human.say(“hi”) 结果如何？是否有办法修正？
# Human.say(a, "hi")
