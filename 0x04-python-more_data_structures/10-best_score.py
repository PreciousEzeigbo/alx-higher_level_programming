#!/usr/bin/python3
def best_score(a_dictionary):
    #initialize variable to track maximum score
    i = 0
    keys = None

    #iterate through the dictionary
    for key,value in a_dictionary.items():
        if value > i:
            i = value

    #returns the key with the highest value
    return keys
