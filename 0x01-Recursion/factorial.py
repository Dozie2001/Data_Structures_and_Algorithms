def factorial(n):
    """To compute factorial of a positive value
    args:
    n(int value): numeric value
    Return: Factorial value of n
    """

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
