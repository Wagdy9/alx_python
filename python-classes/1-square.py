class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def dict_(self):
        return {"_Square__size": self.__size}


my_square = Square(3)
print(type(my_square))
print(my_square.dict_)

my_square = Square(89)
print(type(my_square))
print(my_square.dict_)

my_square = Square()
print(type(my_square))
print(my_square.dict_)
