#!/usr/bin/python3
"""class rectangle that defines a rectangle"""


class Rectangle:
    """Class rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle
        Attributes:
            width: integer value of the rectangle
            height: integer value of the recatngle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of the width
        Attributes:
            value: width of the rectangle
        Raises:
            TypeError: if it is not an integer
            ValueError: if the value is negative
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of the height
        Attributes:
            value: height of the rectangle
        Raises:
            TypeError: if it is not an integer
            ValueError: if the value is negative
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else
        return 2 * (self.width + self.height)
