#!/usr/bin/python3
"""Class square that defines a square"""


class Square:
    """Class square that defines a square"""
    def __init__(self, size=0):
        """__init__

        The __init__ Initializes a square with optional size.

       Attributes:
           size (int, optional): The size of the square. Defaults to 0.

       Raises:
           TypeError: If size is not an integer.
           ValueError: If size is less than 0.
       """

       if not isinstance(size, int):
           raise TypeError("size must be an integer")
       if size < 0:
           raise ValueError("size must be >= 0")

       self.__size = size
