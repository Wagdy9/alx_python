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

    __validate_width(self, width):
        Validator for the width attribute.
    __validate_height(self, height):
        Validator for the height attribute.
    __validate_x(self, x):
        Validator for the x attribute.
    __validate_y(self, y):
        Validator for the y attribute.
"""

from models.base import Base


class Rectangle(Base):

    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle"""
        super().__init__(id)
        self.__validate_width(width)
        self.__validate_height(height)
        self.__validate_x(x)
        self.__validate_y(y)
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
        self.__validate_width(value)
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        self.__validate_height(value)
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate of the rectangle"""
        self.__validate_x(value)
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate of the rectangle"""
        self.__validate_y(value)
        self.__y = value

    def __validate_width(self, width):
        """Validator for the width attribute."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

    def __validate_height(self, height):
        """Validator for the height attribute."""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

    def __validate_x(self, x):
        """Validator for the x attribute."""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

    def __validate_y(self, y):
        """Validator for the y attribute."""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
