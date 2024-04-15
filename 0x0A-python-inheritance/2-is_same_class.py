#!/usr/bin/python3
"""A function that returns True if the object is
exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """returns true if the object is the same with the class
        otherwise
    """
    return True if type(obj) == a_class else False
