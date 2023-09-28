#!/usr/bin/python3
from sys import exc_info
def main():
    """
    Objective:To open a file for reading
    Input Parameter: None
    Return Value: None
    """
    f = "Temporary_file"
    try:
        with open(f, 'r') as m:
            f.readline()
    except IOError as err:
        print('Problem with Input Output...\n {}'.format(err)) 
        print(exc_info())
    print("Program continues smoothly beyond try...except block")
  
if __name__ == "__main__":
    main()
