#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    max = -10
    if my_list == []:
        return None
    for element in my_list:
        if element > max:
            max = element
        else:
            pass
    return max
