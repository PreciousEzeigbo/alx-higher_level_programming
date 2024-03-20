#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy_dict = a_dictionary.copy()
    for key in copy_dict:
        copy_dict *= 2
    return copy_dict
