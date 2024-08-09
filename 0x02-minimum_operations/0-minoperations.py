#!/usr/bin/python3
"""
Module that contains the minOperations function.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H characters.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The minimum number of operations. Returns 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    return operations
