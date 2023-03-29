def main():
    """Objective: To compute reverse of a string entered by user
    Input Parameter: None
    Return Value: None
    """

    from reverse_string import reverse
    str1 = input('Enter the string: ')
    result = reverse(str1)
    print('Reverse of string {} is {}'.format(str1, result))

if __name__ == '__main__':
    main()