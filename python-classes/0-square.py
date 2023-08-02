class Square:
    def __init__(self, size):
        self.__size = size

    @property
    def dict_(self):
        return self.__dict__


my_square = Square(3)
print(type(my_square))
print(my_square.dict_)

my_square = Square(89)
print(type(my_square))
print(my_square.dict_)

try:
    print(my_square.size)
except AttributeError as e:
    print(e)

my_square = Square(3)
print(type(my_square))
print(my_square.dict_)

try:
    print(my_square._Square__size)
except AttributeError as e:
    print(e)
