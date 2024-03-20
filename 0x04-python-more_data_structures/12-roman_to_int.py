#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not instance(roman_string, str):
        return 0
    roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    total = 0
    prev_value = 0

    for symbol in roman_string:
        value = roman_numerals.get(symbol, 0)
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value

    return total

