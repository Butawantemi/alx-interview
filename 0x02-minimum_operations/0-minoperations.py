#!/usr/bin/python3
"""Minimum number of operatios"""


def minOperations(n):
    """function returns the minimum number of operations 'n'"""
    # Check if the number n is impossible
    if n <= 1:
        return 0

    # Recursively compute the number of operations
    for op in range(2, n + 1):
        if n % op == 0:
            return minOperations(int(n / op)) + op
