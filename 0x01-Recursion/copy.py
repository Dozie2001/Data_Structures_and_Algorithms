#!/usr/bin/python3
""" A program that copies a string using recursive method"""


def copy_1(lst1, lst2=[]):
    """To create a copy pf list list1
    args:
      lst1, lst2 = list
    """

    if lst1 == []:
        return lst2
    else:
        lst2.append(lst1[0])
        copy_1(lst1[1:], lst2)

    return lst2
