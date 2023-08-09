"""
Rectangle class

This class represents a rectangle.

Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
    x (int): The x coordinate of the rectangle.
    y (int): The y coordinate of the rectangle.

Methods:
    __init__(width, height, x=0, y=0, id=None):
        Initialize a new rectangle.
    width(self):
        Get the width of the rectangle.
    width(self, value):
        Set the width of the rectangle.
    height(self):
        Get the height of the rectangle.
    height(self, value):
        Set the height of the rectangle.
    x(self):
        Get the x coordinate of the rectangle.
    x(self, value):
        Set the x coordinate of the rectangle.
    y(self):
        Get the y coordinate of the rectangle.
    y(self, value):
        Set the y coordinate of the rectangle.
"""

#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__":
    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
