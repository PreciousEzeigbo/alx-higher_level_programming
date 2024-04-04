#!/usr/bin/python3
def safe_print_integer(value):
    """
    Args:
    Value : integer to print.

    Returns : True if value is printed well.
    False if otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
