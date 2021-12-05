from field import IntegerField, TextField
from handler import BaseHandler
from entry import startserver

from json import loads


class CreateOrderRequestModel:
    item = TextField(1)
    username = TextField(3)
    quantity = IntegerField(0, 100)

    @staticmethod
    def parse(data):
        if isinstance(data, (str, bytes)):
            data = loads(data)
        model = CreateOrderRequestModel()
        model.item = data.get('item', '')
        model.username = data.get('username', '')
        model.quantity = data.get('quantity', 0)
        return model


class OrderHandler(BaseHandler):
    path = '/order'

    def post(self, data):
        model = CreateOrderRequestModel.parse(data)
        print(
            '==> create order:',
            model.item,
            'x',
            model.quantity,
            'for',
            model.username,
        )
        return 'OK'


if __name__ == '__main__':
    startserver(listen='127.0.0.1:18080')
