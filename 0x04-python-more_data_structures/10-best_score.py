#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    value = max(a_dictionary, key=lambda i: a_dictionary[i])
    return value
