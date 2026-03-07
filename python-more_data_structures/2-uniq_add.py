#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = [0 for i in range(len(my_list))]
    addition = 0
    for element in my_list:
        if element not in new_list:
            new_list.append(element)
            addition = addition+element
    return addition
