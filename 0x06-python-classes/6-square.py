#!/usr/bin/python3


"""Class square that defines a square"""


class Square:
    """Class square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with optional size.
        Attributes:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns the size"""
        return self.__size

    @size.setter
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
        self.__size = value

    @property
    def position(self):
        """Returns the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square,
        ensuring it's an integer.
        Attributes:
            value (int, optional): The value of the square position.

        Raises:
            TypeError: If position is not an integer.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(not isinstance(x, int) or x < 1 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with
        the caharacter #.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
