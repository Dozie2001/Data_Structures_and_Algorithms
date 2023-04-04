#!/usr/bin/python3
"""A recursive problem Tower of hanoi"""


def hanoi(n, source, spare, target):
    """To solve problem of Hanoi using n disc and 3 poles
    args:
      n, source, spare, target: int values
    """

    if n == 1:
        print('Move a disk from {} to {}'.format(source, target))
    elif n == 0:
        return
    else:
        hanoi(n-1, source, target, spare)
        print('Move a disk from {} to {}'.format(source, target))
        hanoi(n-1, spare, source, target)

