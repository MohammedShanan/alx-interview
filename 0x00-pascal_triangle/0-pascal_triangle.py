#!/usr/bin/python3
"""A module for Pascal's triangle"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to a given number of rows.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        list of list of int: A list of lists where each inner list
        represents a row in Pascal's Triangle.
        If the input is not a positive integer, an empty list is returned.
    """
    triangle = [[1]]
    i = 1
    if n < 1:
        return []
    while i < n:
        cur_row = []
        prev_row = triangle[i - 1]
        for j in range(i + 1):
            prev = prev_row[j - 1] if j > 0 else 0
            cur = prev_row[j] if j != len(prev_row) else 0
            cur_row.append(prev + cur)
        i += 1
        triangle.append(cur_row)
    return triangle
