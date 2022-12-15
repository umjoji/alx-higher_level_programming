#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_strings = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    num = 0
    for i in range(len(roman_string)):
        if i > 0 and roman_strings[roman_string[i]] > roman_strings[roman_string[i-1]]:
            num += roman_strings[roman_string[i]] - 2 * roman_strings[roman_string[i-1]]
        else:
            num += roman_strings[roman_string[i]]
    return num
