def main():
    """
    Objective: To determine nth term in Fibonacci sequence
    based on user input
    """
    n = int(input('Enter the value of n: '))
    fibo = __import__('fibo').fib
    result = fibo(n)

    print("{}th Fibonacci term is {}".format(n, result))


if __name__ == '__main__':
    main()
