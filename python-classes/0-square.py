class Square:
    """
    This class represents a Square.

    Attributes:
        __size (int): The size of the Square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the Square.
        """
        self.__size = size

    @property
    def dict_(self):
        """
        Retrieves the Square attributes as a dictionary.

        Returns:
            dict: A dictionary containing the Square attributes.
        """
        return self.__dict__
