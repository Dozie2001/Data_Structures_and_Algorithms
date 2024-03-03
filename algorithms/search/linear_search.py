#!/usr/bin/python3
def linear_search(list, target):
    """Return the position of the target if found, else returns None
    """

    for i in range(0, len(list)):
        if list[i]  == target:
            return i
    return None

def verify(index):
    if index is not None:
        print(f"Target is at index {index}")
    else:
        print("Target Not found")


def main():
    number = [1, 2, 3, 4, 5, 6, 8, 9, 10]

    index = int(input(" Enter index: "))
    result = linear_search(number, index)

    final_index = verify(result)

if __name__ == "__main__":
    main()
