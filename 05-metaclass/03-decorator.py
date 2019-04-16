# -*- encoding: utf-8 -*-
import registry


def command(cls):
    registry.register(cls)
    return cls


@command
class CommandA:
    pass


registry.ls()
