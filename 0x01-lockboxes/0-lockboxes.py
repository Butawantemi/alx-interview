#!/usr/bin/python3
"""an algorithm to determine if n number of boxes can be unlocked

given n number of locked boxes, each numbered sequentially from 0 to n - 1.
If each box may contain keys to other boxes, determine if all the boxes
can be opened.

"""


def canUnlockAll(boxes):
    """checks if all boxes can be unlocked"""
    # Check if boxes are provided
    if not boxes:
        return False

    # Check if boxes are not a list of list
    if not isinstance(boxes, list):
        return False

    # Initial position to check the unlocked boxes
    unlocked = [0]

    # Check if boxes can be unlocked
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)

    # check if all boxes are unlocked
    # And return True, otherwise return False
    if len(unlocked) == len(boxes):
        return True
    return False
