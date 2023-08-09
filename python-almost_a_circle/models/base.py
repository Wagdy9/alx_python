# models/base.py

"""
This module contains the Base class.

The Base class is the base class of all other classes in this project.
It provides a way to manage the id attribute of all objects.
"""


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Init method"""
        if id is not None:
            self.id = id
        else:
            self.id = self.__class__.__nb_objects + 1
            self.__class__.__nb_objects += 1

    def __repr__(self):
        """Representation"""
        return f"<Base id={self.id}>"
