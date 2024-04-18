#!/usr/bin/python3
"""An algorithm to determine if n number of boxes can be unlocked

Given n number of locked boxes, each numbered sequentially from 0 to n - 1.
If each box may contain keys to other boxes, determine if all the boxes
can be opened.

"""


def canUnlockAll(boxes):
    """Checks if all boxes can be unlocked

    Args:
        boxes (list of list): all the boxes to check

    Returns:
        boolean: True if can be unlocked, False otherwise

    """
    # check if boxes are provided
    if not boxes:
        return False

    # check if boxes are not a list of list
    if not isinstance(boxes, list):
        return False

    # Initial position to check the unlocked boxes
    unlocked = [0]

    # check if boxes can be unlocked
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)

    # check if all boxes are unlocked
    # and return True, otherwise return False
    if len(unlocked) == len(boxes):
        return True
    return False
