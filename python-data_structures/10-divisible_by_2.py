#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_value = []
    for element in my_list:
        if element % 2 == 0:
            list_value.append(True)
        else:
            list_value.append(False)
    return list_value
