# -*- encoding: utf-8 -*-
from registry import register, ls


class CommandA:
    pass


class CommandB:
    pass


register(CommandA)
register(CommandB)
ls()
