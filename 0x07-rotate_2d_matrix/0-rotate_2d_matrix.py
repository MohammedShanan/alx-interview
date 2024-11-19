#!/usr/bin/python3
"""
2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place"""
    n = len(matrix[0])
    if type(matrix) is list:
        return
    if n <= 0:
        return
    i, j = 0, n - 1
    while i < j:
        tmp = matrix[i]
        matrix[i] = matrix[j]
        matrix[j] = tmp
        i += 1
        j -= 1
    i, j = 0, 0

    while i < n:
        j = i + 1
        while j < n:
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp
            j += 1
        i += 1
