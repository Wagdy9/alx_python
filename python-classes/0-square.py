class Square:
    def __init__(self, size):
        self.__size = size

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

my_square = Square(89)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.__size)  # Change 'size' to '__size'
except AttributeError as e:
    print(e)

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)
