class TextField:
    def __init__(self, min_length):
        self.min_length = min_length
        self.value = None
        self.name = None

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if len(value) <= self.min_length:
            raise ValueError(
                f'length of "{self.name}" must be longer than {self.min_length}'
            )
        self.value = value

    def __get__(self, instance, owner):
        return self.value


class IntegerField:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self.value = None
        self.name = None

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'{self.name} must be an integer')
        if value <= self.min_value or value > self.max_value:
            raise ValueError(
                f'{self.name} must be between {self.min_value} and {self.max_value}'
            )

        self.value = value

    def __get__(self, instance, owner):
        return self.value
