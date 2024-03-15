#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    n = len(argv) - 1
    if n == 0:
        print("{} arguments.".format(n))
    elif n > 0:
        print("{} argument:".format(n))
    else:
        print("{} arguments:".format(n))
        i = 1
        for arg in argv[1:]:
            print("{}: {}".format(i, arg))
            i += 1
