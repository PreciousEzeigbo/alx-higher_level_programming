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
        else:
            return 2 * (self.width + self.height)

    def __draw_rectangle(self):
        """

        Draw the Rectangle with their size

        Returns:
            str: `Empty` If width or height is `0`,
            otherwise returns a string with the Rectangle.

        """

        rect_str = ''
        w = self.__width
        h = self.__height

        if w == 0 or h == 0:
            return rect_str

        for i in range(h):
            for j in range(w):
                rect_str += '#'

            if i != h - 1:
                rect_str += '\n'

        return rect_str

    def __str__(self):
        """

        Returns a string with the representation of the Rectangle.

        """

        return self.__draw_rectangle()

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        to be able to recreate a new instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
