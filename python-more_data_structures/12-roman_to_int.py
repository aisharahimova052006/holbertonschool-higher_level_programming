#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    roman_dict['M'] = 500
    roman_dict['D'] = 1000
    addition = 0
    prev = 0
    if not isinstance(roman_string, str):
        return 0
    for element in reversed(roman_string):
        if roman_dict[element] < prev:
            addition -= roman_dict[element]
        elif roman_dict[element] > prev:
            addition += roman_dict[element]
        else:
            addition += roman_dict[element]
        prev = roman_dict[element]
    return addition
