#!/usr/bin/python3
"""Class rectangle that inherits from Basegeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherots from BaseGeometry"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, 'height', height)
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width
        self.__height = height
