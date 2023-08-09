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

from models.base import Base


class Rectangle(Base):

    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if value <= 0:
            raise ValueError("width must be positive")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if value <= 0:
            raise ValueError("height must be positive")
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate of the rectangle"""
        if value < 0:
            raise ValueError("x must be non-negative")
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate of the rectangle"""
        if value < 0:
            raise ValueError("y must be non-negative")
        self.__y = value
