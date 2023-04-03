#!/usr/bin/python3
""" To flatten the list entered by user """
from flatten import flatten


def main():
    """To flatten the list entered by user"""
    lst1 = eval(input('Enter the list: '))
    result = flatten(lst1)
    print("Flattened List:", (result))

if __name__ == "__main__":
    main()
