class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    def area(self):
        return self.__size**2


mysquare = Square(3)
print("{}".format(mysquare.area()))

mysquare = Square(89)
print("{}".format(mysquare.area()))

mysquare = Square()
print("{}".format(mysquare.area()))
