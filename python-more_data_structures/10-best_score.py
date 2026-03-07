#!/usr/bin/python3
def best_score(a_dictionary):
    maximum = 0
    element_storage = ''
    if not a_dictionary:
        return None
    for key in a_dictionary:
        if a_dictionary[key] > maximum:
            maximum = a_dictionary[key]
            element_storage = key
    return element_storage
