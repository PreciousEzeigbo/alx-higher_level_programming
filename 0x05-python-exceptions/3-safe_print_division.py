#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides two integers and prints the result.
    Args:
    a: The first integer.
    b: The second integer.

    Returns:
    The result of the division.
    """
    try:
        c = (a / b)
    except ZeroDivisionError:
        return None
    except TypeError:
        return None
    finally:
        print("Inside result: ""{}".format(c))
    return c
