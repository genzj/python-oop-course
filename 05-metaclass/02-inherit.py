# -*- encoding: utf-8 -*-
import registry


class CommandBase:
    @classmethod
    def register(cls):
        registry.register(cls)


class CommandA(CommandBase):
    pass


CommandA.register()

registry.ls()
