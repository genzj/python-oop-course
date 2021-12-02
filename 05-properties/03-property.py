class CreateOrderRequestModel:
    def __init__(self):
        self.__item = None
        self.__quantity = None

    @property
    def item(self):
        return self.__item

    @item.setter
    def item(self, item):
        if len(item) <= 1:
            raise ValueError('length of "item" must be longer than 1')
        self.__item = item

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if not isinstance(quantity, int):
            raise ValueError('quantity must be an integer')
        if quantity <= 0 or quantity > 100:
            raise ValueError('quantity must be between 0 and 100')
        self.__quantity = quantity

    @staticmethod
    def parse(data):
        model = CreateOrderRequestModel()
        model.item = data.get('item', '')
        model.quantity = data.get('quantity', 0)
        return model


class OrderHandler:
    def post(self, data):
        model = CreateOrderRequestModel.parse(data)
        print('==> create order:', model.item, 'x', model.quantity)
        return 'OK'


print('=' * 20)
OrderHandler().post(dict(item='cup', quantity=11))
