#!/usr/bin/python3
def flatten(lst1, lst2=[]):
    """To flatten a list list1
    args:
      lst1, lst2 - list
    Return Value lst2 - a list
    """

    for element in lst1:
        if type(element) != list:
            lst2.append(element)
        else:
            flatten(element, lst2)
    return lst2
