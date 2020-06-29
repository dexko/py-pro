#1
import re
EMAIL_REGEX = re.compile( r"[A-Za-z0-9-_]+(.[A-Za-z0-9-_]+)*@""[A-Za-z0-9-]+(.[A-Za-z0-9]+)*(.[A-Za-z]{2,})")


def ValidateEmail(email_address):
    if not EMAIL_REGEX.match(email_address):
        raise ValueError


class EmailDescriptor:
    """Descriptor class used to validate an email address."""

    def __init__(self):
        self.email = {}

    def __get__(self, instance, owner):
        return self.email.get(instance, 0)

    def __set__(self, instance, email_address):
        if not EMAIL_REGEX.match(email_address):
            raise ValueError
        self.email[instance] = email_address


class MyClass:
    email = EmailDescriptor()


my_class = MyClass()
my_class.email = "validemail@gmail.com"

my_class.email = "novalidemail"
#2

class Singleton(type):
    _instances={}

    def __call__(cls, *args, **kwargs):
        if cls not in Singleton._instances:
            Singleton._instances[cls] = super().__call__(*args, **kwargs)
        return Singleton._instances[cls]


class MyClass(metaclass=Singleton):
    pass


c = MyClass()
b = MyClass()
assert id(c) == id(b)


#3

class IngegerField:
    """Descriptor class that hold unicue states ."""

    def __init__(self, number):
        self.number = number  

    def __get__(self, instance, owner):
        return instance.__dict__[self.number]  

    def __set__(self, instance, value):
        instance.__dict__[self.number] = value


class Data:
    number = IngegerField('number')


data_row = Data()
new_data_row = Data()

data_row.number = 5
new_data_row.number = 10

assert data_row.number != new_data_row.number
