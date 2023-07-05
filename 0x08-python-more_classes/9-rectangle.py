#!/usr/bin/python3
""" empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """ class rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """width
        """
        return self.__width

    @property
    def height(self):
        """height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """width setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        width = size
        height = size
        return cls(width, height)

    def area(self):
        """ returns rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """ returns rectangle perimiter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        """ return the rectangle with the character #
        """
        rectangle = ""

        if self.__width > 0 and self.__height > 0:
            for y in range(self.__height):
                rectangle += str(self.print_symbol) * self.__width + '\n'

        return rectangle[:-1]


    def __repr__(self):
        """ return a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print the message when an instance of rectangle is deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

