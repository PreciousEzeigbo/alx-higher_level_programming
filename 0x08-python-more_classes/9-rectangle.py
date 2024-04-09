#!/usr/bin/python3
"""class rectangle that defines a rectangle"""


class Rectangle:
    """Class rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the rectangle
        Attributes:
            width: integer value of the rectangle
            height: integer value of the recatngle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """

        Draw the Rectangle with their size

        Returns:
            str: `Empty` If width or height is `0`,
            otherwise returns a string with the Rectangle.

        """

        rectangle = ""

        if self.__width > 0 and self.__height > 0:
            for y in range(self.__height):
                rectangle += str(self.print_symbol) * self.__width + '\n'

        return rectangle[:-1]

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        to be able to recreate a new instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Sets a behaviour  when an instance of Rectangle is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the
        one with the larger or equal area.

        Args:
        rect_1: The first rectangle object to compare.
        rect_2: The second rectangle object to compare.

        Returns:
        The rectangle object with the larger or equal area
        (rect_1 if equal).

        Raises:
            TypeError:
            if either rect_1 or rect_2 is not a Rectangle instance.
        """

        # Check if both arguments are instances of Rectangle
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        # Calculate the areas of both rectangles
        area_1 = rect_1.area()
        area_2 = rect_2.area()

        # Determine the larger or equal rectangle based on area
        if area_1 > area_2:
            return rect_1
        elif area_2 > area_1:
            return rect_2
        else:  # Areas are equal
            return rect_1

        @classmethod
        def square(cls, size=0):
        """
        Creates a new Rectangle instance (a square).
        Args:
        size: An integer representing the
        side length of the square (default 0).

        Returns:
        A new Rectangle instance with width and height equal to size.
        Raises a TypeError if size is not an integer.
        Raises a ValueError if size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        return cls(size, size)
