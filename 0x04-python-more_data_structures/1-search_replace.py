#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(my_list)
    for element in range(len(new_list)):
        if new_list[element] == search:
            new_list[element] = replace
    return new_list
