# -*- encoding: utf-8 -*-
import json
from urllib.error import HTTPError
from urllib.request import urlopen


def get(url):
    try:
        with urlopen(url) as resp:
            return json.load(resp)
    except HTTPError as ex:
        if ex.code == 404:
            return None
        else:
            raise


class Resource:
    def __init__(self, url, offset=1):
        self.url = url
        self.offset = offset

    def __iter__(self):
        return ResourceIterator(self.url, self.offset)


class ResourceIterator:
    def __init__(self, url, offset):
        self.url = url
        self.offset = offset

    def __next__(self):
        resp = get(self.url + str(self.offset))
        self.offset += 1
        if resp:
            return resp
        else:
            raise StopIteration()


users = Resource('https://jsonplaceholder.typicode.com/users/')
for user in users:
    print(user['id'] , '-', user['name'])


def gather_resource(url, offset):
    while True:
        resp = get(url + str(offset))
        if resp:
            yield resp
            offset += 1
        else:
            break

print('-' * 40)

for user in gather_resource('https://jsonplaceholder.typicode.com/users/', 8):
    print(user['id'] , '-', user['name'])
