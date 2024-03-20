#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not  str or roman_string is None:
        return 0

    roman_numerals = {
        ['M', 1000], ['D', 500], ['C', 100], ['L', 50],
        ['X', 10], ['V', 5], ['I', 1]
    }
    total = 0
    prev_value = 0

    for symbol in roman_string:
        for element in roman_numerals:
            if symbol == element[0]:
                if prev_value == 0 or prev_value >= element[1]:
                    total += element[1]
                elif prev_value < element[1]:
                    total += element[1] - (prev_value * 2)

                prev_value = element[1]

    return total

