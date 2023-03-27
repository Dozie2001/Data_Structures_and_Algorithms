def length(str1):
    """To determine the length of the input string
    Input arameter: str1 - string
    Return Value: Int
    """

    if str1 == '':
        return 0
    else:
        return 1 + length(str1[1:])
