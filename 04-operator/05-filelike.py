# -*- encoding: utf-8 -*-
import json
from io import StringIO

number_table = '甲乙丙丁戊己庚辛壬癸'


class NumberTranslator:
    def __init__(self):
        self.buffer = StringIO()

    def write(self, b):
        for x in b:
            try:
                int_x = int(x)
                self.buffer.write(number_table[int_x])
            except:
                self.buffer.write(x)

    def read(self, size):
        return self.buffer.read(size)

    def seek(self, pos, whence=0):
        return self.buffer.seek(pos, whence)


data = {
    'x': 31,
    'y': 49
}

translator = NumberTranslator()
json.dump(data, translator)
translator.seek(0)
print(translator.read(-1))
