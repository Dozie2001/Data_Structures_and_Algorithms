def fib(n):
    """
    A program that returns the value of nth term in
    a fibonacci sequence
    args:
    n(int): nth term
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
