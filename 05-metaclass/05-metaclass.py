# -*- encoding: utf-8 -*-
import registry


class MetaCommand(type):
    def __new__(cls, name, bases, namespace, **kwargs):
        ret = super().__new__(cls, name, bases, namespace)
        if bases != tuple() and bases != (object, ):
            registry.register(ret)
        return ret


class CommandBase(metaclass=MetaCommand):
    pass


class CommandA(CommandBase):
    pass


registry.ls()
