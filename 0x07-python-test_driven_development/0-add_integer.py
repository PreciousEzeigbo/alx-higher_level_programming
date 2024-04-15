#!/usr/bin/python3
"""Function that adds two integers"""


def add_integer(a, b=98):
    """Adds two integers
    Attributes:
        a: an integer or float
        b: an integer or float

    Raises:
        TypeError: if not an integer or float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return (a + b)
