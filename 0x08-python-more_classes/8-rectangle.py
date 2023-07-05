#!/usr/bin/python3

"""Create a class Rectangle that defines a rectangle"""


class Rectangle:
    """rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Retrieve attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """To set attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """To retrieve attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """To set the attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value > 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def area(self):
        """Area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Get perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """ return the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(["".join([str(self.print_symbol)
                for i in range(self.__width)]) for j in range(self.__height)]))

    def __repr__(self):
        """Return a string representation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Sets the del behavior of the Rectangle object."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
