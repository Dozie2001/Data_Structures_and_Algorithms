"""
Creates  a Binary search algorithm
n = 50
O(n)  = 50 steps
O(log50) = 25 steps. (efficient)
"""




def binary_search(arr, target):
    first = 0
    last = len(arr) -1

    
    # 0 - 8
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            first = mid + 1 # mid value is less than target arr[mid+1:]
        else:
            last = mid -1 # mid value is greater than target arr[:mid-1]
    return None

arr = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11]  # Index for mid will be 2  [8, 8, 10, 11]  [1, 2, 3, 4, 5, 6]

if __name__ == "__main__":
    binary_search(arr, 6)