#!/usr/bin/python3
"""
Optimized Prime Game Solver
"""

def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.
    
    :param x: number of rounds
    :param nums: array of n for each round
    :return: name of the player that won the most rounds, or None if it's a tie
    """
    if not nums or x < 1:
        return None
    
    max_num = max(nums)
    primes = [True for _ in range(max(max_num + 1, 2))]
    primes[0] = primes[1] = False

    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    prime_counts = [0] * (max_num + 1)
    for i in range(2, max_num + 1):
        prime_counts[i] = prime_counts[i-1]
        if primes[i]:
            prime_counts[i] += 1

    maria_wins = sum(prime_counts[n] % 2 == 1 for n in nums)
    ben_wins = x - maria_wins

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
