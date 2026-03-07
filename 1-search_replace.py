#!/usr/bin/python3
def search_replace(my_list, search, replace):
    length = len(my_list)
    new_matrix = list(my_list)
    for i in range(length):
        if my_list[i] == search:
            new_matrix[i] = replace
    return new_matrix
