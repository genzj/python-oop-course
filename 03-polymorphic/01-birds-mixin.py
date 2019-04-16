class Flyable(object):
    def fly(self):
        print('%r can fly' % (self, ))


class Bird(object):
    color = None


class Swallow(Bird, Flyable):
    color = 'black & white'


class Ostrich(Bird):
    color = 'grey & brown'


print(Swallow().color)
Swallow().fly()
print(Ostrich().color)


# not work
# Ostrich().fly()


def flyable(instance):
    return isinstance(instance, Flyable)


print('swallow can fly:', flyable(Swallow()))
print('ostrich can fly:', flyable(Ostrich()))
