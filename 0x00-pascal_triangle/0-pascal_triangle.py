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
    if n <= 1:
        return []
    while i < n:
        array = []
        for index in range(i + 1):
            prev = triangle[i - 1][index - 1] if index > 0 else 0
            current = triangle[i - 1][index] if index != len(triangle[i - 1]) else 0
            array.append(prev + current)
        i += 1
        triangle.append(array)
    return triangle
