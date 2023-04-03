#!/usr/bin/python3
"""To create a copy of the list entered by user"""
from copy import copy_1

def main():
    """Return Value: None"""

    lst1 = eval(input('Enter the list: '))
    lst2 = copy_1(lst1)
    print('Copy of list lst1 is ', lst2)

if __name__ == '__main__':
    main()
