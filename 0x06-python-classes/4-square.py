#!/usr/bin/python3


"""Class square that defines a square"""


class Square:
    """Class square that defines a square"""
    def __init__(self, size=0):
        """Initializes a square with optional size.
        Attributes:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Returns the size"""
        return self._size

    @property.setter
    def size(self, value):
        """Sets the size of the square,
        ensuring it's an integer and non-negative.
        Attributes:
            value (int, optional): The value of the square size.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Finds the area of the square
        Returns:
            int: The area of the square.
        """
        return self._size * self._size
