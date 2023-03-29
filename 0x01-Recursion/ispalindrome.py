#!/usr/bin/python3
def ispalindrome(str1):
    """To check whether a string is a palindrome
    args:
       str1: string
    """

    if str1 == '':
        return True
    else:
        return (str1[0] == str1[-1] and ispalindrome(str1[1:-1]))
