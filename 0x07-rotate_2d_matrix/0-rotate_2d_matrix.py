#!/usr/bin/python3
"""A module to rotate a 2D array 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D array 90 degrees clockwise"""
    l, r = 0, len(matrix) - 1

    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            # Save the top left value
            top_left = matrix[top][l + i]

            # Move bottom left into top left
            matrix[top][l + i] = matrix[bottom - i][l]

            # Move bottom right into bottom left
            matrix[bottom - i][l] = matrix[bottom][r - i]

            # Move top right into bottom right
            matrix[bottom][r - i] = matrix[top + i][r]

            # Move top left into top right
            matrix[top + i][r] = top_left

        r -= 1
        l += 1
