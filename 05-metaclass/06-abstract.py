# -*- encoding: utf-8 -*-
import abc
import registry


class MetaCommand(abc.ABCMeta):
    def __new__(cls, name, bases, namespace, **kwargs):
        ret = super().__new__(cls, name, bases, namespace)
        if bases != tuple() and bases != (object, ):
            registry.register(ret)
        return ret


class CommandBase(metaclass=MetaCommand):
    @abc.abstractmethod
    def run(self):
        raise NotImplementedError()


class CommandA(CommandBase):
    def run(self):
        print('running command A')


registry.ls()

# CommandBase()
CommandA().run()
