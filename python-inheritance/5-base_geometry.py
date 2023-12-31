""" An empty class representing the base geometry."""


class BaseMetaClass(type):
    """
    overrides.
    """

    def __dir__(cls):
        return [
            attribute
            for attribute in super().__dir__()
            if attribute != "__init_subclass__"
        ]


class BaseGeometry(metaclass=BaseMetaClass):
    """
    Do nothing: By passing pass.
    """

    def __dir__(cls):
        return [
            attribute
            for attribute in super().__dir__()
            if attribute != "__init_subclass__"
        ]

    def area(self):
        """
        Public instance method that raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method that validate a value
        Attr:
            name(string): the name string.
            value(int): must be an integer greater than 0.
        """
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
