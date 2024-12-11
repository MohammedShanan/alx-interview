#!/usr/bin/python3
"""
Prime game module.
"""


def isWinner(x, nums):
    """
    Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None

    n = max(nums)
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    prime_counts = [0] * (n + 1)
    for i in range(1, n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    marias_wins, bens_wins = 0, 0
    for num in nums:
        if prime_counts[num] % 2 == 1:
            marias_wins += 1
        else:
            bens_wins += 1

    if marias_wins > bens_wins:
        return "Maria"
    elif bens_wins > marias_wins:
        return "Ben"
    return None
