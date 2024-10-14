#!/usr/bin/python3
"""
Minimum Operations Module
"""


def minOperations(n: int) -> int:
    """
    Calculate the minimum number of operations needed to achieve
    exactly n 'H' characters in the file starting from a single 'H'
    using only two operations: Copy All and Paste.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The fewest number of operations needed,
    or 0 if n is impossible to achieve.
    """

    if n <= 1:
        return 0

    operations = 0
    current = n

    for i in range(2, n + 1):
        while current % i == 0:
            operations += i
            current //= i

    return operations


print(minOperations(12))
