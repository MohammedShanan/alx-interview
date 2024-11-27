#!/usr/bin/python3
"""
Change making module.
"""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Determines the fewest number of coins needed to meet a given total.

    Args:
        coins (List[int]): A list of the values of coins available.
        total (int): The target amount to achieve using the coins.

    Returns:
        int: The minimum number of coins needed to meet the total,
             or -1 if it is not possible.
    """
    if total <= 0:
        return 0
    if not coins:
        return -1

    coins.sort(reverse=True)

    remaining = total
    coin_count = 0

    for coin in coins:
        if remaining == 0:
            break
        count = remaining // coin
        coin_count += count
        remaining -= count * coin

    return coin_count if remaining == 0 else -1
