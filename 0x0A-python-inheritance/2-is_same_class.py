#!/usr/bin/python3
"""A function that returns True if the object is
exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """Checlks if obj is exactly an instance of the specified class
    args:
        obj: the object
        a_class: the class to compare with the object

    Returns:
        true if the object is the same with the class
        otherwise false
    """
    if type(obj) == a_class:
        return True

    return False
