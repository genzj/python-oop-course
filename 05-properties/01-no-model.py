class OrderHandler:
    def post(self, data):
        item = str(data.get('item', ''))
        if len(item) <= 1:
            raise ValueError('length of "item" must be longer than 1')

        quantity = data.get('quantity', None)
        if not isinstance(quantity, int):
            raise ValueError('quantity must be an integer')
        if quantity <= 0 or quantity > 100:
            raise ValueError('quantity must be between 0 and 100')

        print('==> create order:', item, 'x', quantity)
        return 'OK'


print('=' * 20)
OrderHandler().post(dict(item='cup', quantity=11))
