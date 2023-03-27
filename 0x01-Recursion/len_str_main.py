def main():
    """Objective: To determine length of the input string
    Input Parameter: str - string
    Return Value: numeric
    """

    str1 = input('Enyer the string: ')
    length = __import__('length').length
    result = length(str1)
    print('Length of string {} is {}'.format(str1, result))

if __name__ == '__main__':
    main()