#!/usr/bin/python3
"""To check if a string is a palindrome"""
from ispalindrome import ispalindrome

def main():
    """
    Input Parameter: None
    Return Value: None
    """


    str1 = input('Enter the string: ')
    if (ispalindrome(str1)):
        print('String is a palindrome')
    else:
        print('String is not a palindrome')

if __name__ == '__main__':
    main()