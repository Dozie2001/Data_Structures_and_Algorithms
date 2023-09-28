#!/usr/bin/python3
from sys import exc_info
def main():
    """
    Computes price per unit weight of an item
    Input ParaMETER: None
    Return: None
    """


    price = input('Enter price of item purchased: ')
    weight = input('Enter weight of item purchased: ')
    try:
        if (price == ''): price = None
        price = float(price)
        if weight == '': weight = None
        weight = float(weight)
        assert price >=0 and weight >=0
        result = price / weight
    except ValueError:
        print('Invalid inputs: ValueError')
    except TypeError:
        print('Invalid inpugs: TypeError')
    except ZeroDivisionError:
        print('Invalid inputs: ZeroDivisionError')
    except:
        print(str(exc_info()))
    else:
        print('Print per unit weight:', result)

if __name__ == '__main__':
    main()
