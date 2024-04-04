#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Args:
    my_list : The list of elements to print
    x : The number of elements of my_list to print

    Returns:
    The number of elemts printed.
    """
    printed = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            printed += 1
        except IndexError:
            break
    print("")
    return (printed)
