#!/usr/bin/python3
"""
Module for making change using the fewest number of coins (optimized version)
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
    coins (list of int): List of coin values available
    total (int): The target amount

    Returns:
    int: Fewest number of coins needed to meet total, or -1 if not possible
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for greedy approach
    coins.sort(reverse=True)

    # Initialize an array to store the minimum coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
