# -*- encoding: utf-8 -*-
class ToDictMixin:
    fields = []

    def to_dict(self):
        return {attr: getattr(self, attr) for attr in self.fields}


class A(ToDictMixin):
    a = 1
    b = 2
    c = 3

    fields = ['a', 'b', 'c']


class B(A):
    d = 4

    fields = A.fields + ['d']


print(A().to_dict())
print(B().to_dict())
