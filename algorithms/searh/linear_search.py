#!/usr/bin/python3
def linear_search(list, target):
    """Return the position of the target if found, else returns None
    """

    for i in range(0, len(list)):
        if list[i]  == target:
            return i
    return None

