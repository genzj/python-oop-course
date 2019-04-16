# -*- encoding: utf-8 -*-


class Resource:
    def use(self):
        print('open the resource', self)

    def close(self):
        print('close the resource', self)

    def __enter__(self):
        self.use()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


with Resource() as resource:
    print('using resource', resource)

print('-' * 40)

import contextlib


@contextlib.contextmanager
def managed_resource(resource=None):
    resource = resource or Resource()
    resource.use()
    try:
        yield resource
    finally:
        resource.close()


with managed_resource(Resource()) as resource:
    print('using resource', resource)

print('-' * 40)


resource = Resource()
resource.use()
with contextlib.closing(resource) as resource:
    print('using resource', resource)
