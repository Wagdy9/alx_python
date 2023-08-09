#!/usr/bin/python3

"""Defines class Rectangle.

This module defines the Rectangle class, which represents a rectangle.

The Rectangle class has the following attributes:

* width: The width of the rectangle.
* height: The height of the rectangle.
* x: The x coordinate of the rectangle.
* y: The y coordinate of the rectangle.

The Rectangle class has the following methods:

* area(): Calculates the area of the rectangle.
* display(): Displays the rectangle using #.
* __str__(): Returns a string representation of the rectangle.
* update(): Updates the attributes of the rectangle.
"""

from models.base import Base


class Rectangle(Base):
    """Represent a Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate of the rectangle.
            y (int): The y coordinate of the rectangle.
            id (int): The identity of the rectangle.
        Raises:
            TypeError: If the input is not an integer.
            ValueError: If width/height is <= 0.
        """
        super().__init__(id)
        self._width = width
        self._height = height
        self._x = x
        self._y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self._width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self._height = value

    @property
    def x(self):
        """Get the x coordinate of the rectangle."""
        return self._x

    @x.setter
    def x(self, value):
        """Set the x coordinate of the rectangle."""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self._x = value

    @property
    def y(self):
        """Get the y coordinate of the rectangle."""
        return self._y

    @y.setter
    def y(self, value):
        """Set the y coordinate of the rectangle."""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self._y = value

    def area(self):
        """Calculates the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Display the rectangle using #."""
        if self.width == 0 or self.height == 0:
            print('')
            return

        [print('') for y in range(self.y)]
        for h in range(self.height):
            [print(' ', end='') for x in range(self.x)]
            [print('#', end='') for w in range(self.width)]
            print('')

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f'[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}'

    def update(self, *args, **kwargs
