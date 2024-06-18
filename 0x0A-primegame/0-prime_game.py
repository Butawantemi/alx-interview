#!/usr/bin/python3
""" Module for solving prime game question """

def isWinner(x, nums):
    """Prime Game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    