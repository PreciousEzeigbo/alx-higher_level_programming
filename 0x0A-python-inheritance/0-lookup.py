#!/usr/bin/python3
"""  returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """Returns the list of available attributes and methods.
    """
    return dir(obj)
