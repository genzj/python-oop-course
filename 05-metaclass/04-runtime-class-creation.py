# -*- encoding: utf-8 -*-
import registry


class CommandBase:
    pass


def new_command_cls(name, run):
    cls = type(
        name,
        (CommandBase,),
        {'run': run}
    )
    registry.register(cls)
    return cls


CommandA = new_command_cls('CommandA', lambda self: print('good'))
registry.ls()
CommandA().run()
