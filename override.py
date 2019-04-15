# -*- encoding: utf-8 -*-
# ref: https://en.wikipedia.org/wiki/Method_overriding

class Thought(object):
    def __init__(self):
        print("I'm a new object of type Thought!")

    def message(self):
        print("I feel like I am diagonally parked in a parallel universe.")


class Advice(Thought):
    def __init__(self):
        super(Advice, self).__init__()

    def message(self):
        print("Warning: Dates in calendar are closer than they appear")


t = Thought()
t.message()

a = Advice()
a.message()

Thought.message(a)
