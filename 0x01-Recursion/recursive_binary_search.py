#!/usr/bin/python3
def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2
    
    if list[midpoint] == target:
        return True
    else:
        if list[midpoint] < target:
            return recursive_binary_search(list[midpoint+1: ], target)
        else:
            return recursive_binary_search(list[:midpoint-1], target)


def verify(result):
    print("Target found ", result)


def main():
    number = [1, 2, 3, 4, 5, 6, 8, 9, 10]

    index = int(input(" Enter index: "))
    result = recursive_binary_search(number, index)

    final_index = verify(result)

if __name__ == "__main__":
    main()

