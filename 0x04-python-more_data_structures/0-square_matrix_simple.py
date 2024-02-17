#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_cpy = []
    if len(matrix) == 0:
        return matrix_cpy
    matrix_cpy = [[col*col for col in row] for row in matrix]
    return matrix_cpy
