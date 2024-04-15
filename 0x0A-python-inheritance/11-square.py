#!/usr/bin/python3
"""module sub class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Square(BaseGeometry):
    """
    A Square class shape, inheirts from BaseGeometry
    """
    def __init__(self, size):
    """"
    Init function for Square
    Attributes:
        size (int): The size of the square
    """
    self.integer_validator("size", size)
    self.__size = size

    def __str__(self):
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        return self.__size ** 2
