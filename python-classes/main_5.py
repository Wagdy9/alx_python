#!/usr/bin/python3
Square = __import__("1-square").Square

try:
    my_square = Square(-89)
    print(type(my_square))
    print(my_square.__dict__)
except Exception as e:
    print(e)
