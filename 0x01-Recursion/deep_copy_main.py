#!/usr/bin/python3
"""To create deep copy of list entered by user"""

from deep_copy import deepCopy
def main():
    lst1 = eval(input('Enter the list: '))
    lst2 = deepCopy(lst1)
    print('Deep copy of list is ', lst2)

if __name__ == '__main__':
    main()
