3

class IngegerField:
    def __init__(self, number):
        self.number = number  # (4)

    def __get__(self, instance, owner):
        return instance.__dict__[self.number]  # (5)

    def __set__(self, instance, value):
        instance.__dict__[self.number] = value


class Data:
    number = IngegerField('number')


data_row = Data()
new_data_row = Data()

data_row.number = 5
new_data_row.number = 10

assert data_row.number != new_data_row.number