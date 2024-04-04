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
        result = (a / b)
    except ZeroDivisionError:
        result = None
    except TypeError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
