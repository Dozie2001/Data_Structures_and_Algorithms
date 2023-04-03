#!/usr/bin/python3
"""To create a deep copy of a list lst1"""
def deepCopy:
    if lst1 == []:
        pass
    else:
        if type(lst1[0]) != list:
            lst2.append(lst1[0])
            else:
                lst2.append([])
                deepcopy(lst1[1:], lst2[-1])
                deepCopy(lst[1:], lst2)
                return lst2
    return lst2
