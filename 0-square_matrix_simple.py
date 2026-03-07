#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    length = len(matrix)
    length_2 = len(matrix[0])
    new_matrix = [[0 for x in range(length_2)] for y in range(length)]
    for i in range(length):
        for j in range(length_2):
            new_matrix[i][j] = matrix[i][j]**2
    return new_matrix
