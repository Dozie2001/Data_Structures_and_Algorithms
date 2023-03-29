#!/usr/bin/python3
def reverse(str1):
    """A function that printts the reverse of a string recursively
    args: str1 - str
    Return Value: str
    """

    if str1 == '':
        return str1
    else:
        return str1[-1] + reverse(str1[:-1])
