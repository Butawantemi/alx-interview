#!/usr/bin/python3
"""
Program to display Pascal's Triangle.

For details about what a Pascal's Triangle is visit
ref: https://en.wikipedia.org/wiki/Pascal%27s_triangle

"""


def pascal_triangle(n: int):
    """Prints a Pascal's Triangle

    Args:
        n (int); The number of rows of a Pascal's triangle

    Returns:
        list vector: A list of lists representing a Pascal's Triangle
        list: An empty list if n is negative integer or zero

    """
    # Check if n is a negative integer or zero
    if n <= 0:
        return []

    # Initialize Pascal's Triangle with the first row
    triangle = [[1]]

    # Generate subsequent rows
    for i in range(1, n):
        row = [1]
        # Compute values for the current row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        # Append the current row to the triangle
        triangle.append(row)

    return triangle
