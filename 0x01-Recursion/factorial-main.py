def main():
    """To compute factorial of a number provided by user
    Input Parameter: None
    Reurn Value: None
    """

    factorial = __import__("factorial").factorial

    n = int(input(" Enter a value: "))
    result = factorial(n)
    print('fatorial of {} is {}'.format(n, result))


if __name__ == '__main__':
    main()
