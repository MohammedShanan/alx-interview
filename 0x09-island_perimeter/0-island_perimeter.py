#!/usr/bin/python3
"""
Island perimeter computing module.
"""


def island_perimeter(grid):
    """
    Computes the perimeter of an island with no lakes.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    if type(grid) != list:
        return 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
