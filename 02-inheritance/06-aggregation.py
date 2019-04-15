# -*- encoding: utf-8 -*-
class Human:
    def __init__(self, name):
        # 实例方法第一个参数为self，指代当前实例
        # 根据参数初始化实例属性
        self.name = name

        # 也可以用常量等初始化实例属性
        self._age = 0

    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))


class Couple:
    def __init__(self, one, other):
        self.one = one
        self.other = other

    def say(self, message):
        self.one.say(message)
        self.other.say(message)


c = Couple(Human("one"), Human("other"))
c.say("hi")
