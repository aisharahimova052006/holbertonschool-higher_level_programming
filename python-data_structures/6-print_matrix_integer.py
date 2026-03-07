#!/usr/bin/python3
def print_matrix_integer(a=[[]]):
    row = len(a)
    column = len(a[0])
    j = 0
    i = 0
    string = ''
    if a == [[]]:
        print()
    while i < row:
        while j < column:
            string = "{:d}".format(a[i][j])
            if j == column-1:
                print(string)
            else:
                print(string, end=' ')
            j += 1
        i += 1
        j = 0
