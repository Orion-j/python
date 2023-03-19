""" --> Binary-Search works by breaking the array/list into smaller sets
    till the value we are looking for is found
"""


def binary_search(lists, target):
    first = 0
    last = len(lists) - 1  # last index of the array/list
    while first <= last:
        midpoint = (first + last) // 2  # //floor division operand.
        if lists[midpoint] == target:
            return midpoint
        elif lists[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    else:
        print("Target not found in list")


# first operation.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = binary_search(numbers, 9)
verify(results)
# second operation.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = binary_search(numbers, 11)
verify(results)
