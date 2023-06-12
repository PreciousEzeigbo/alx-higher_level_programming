#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for elen in matrix:
            i = 1
            length = len(elen)
            for elens in elen:
                if i == length:
                    print('{:d}'.format(elens), end='')
                else:
                    print('{:d}'.format(elens), end= ' ')
                    i += 1
            print()
