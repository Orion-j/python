"""
  --> implementation of Data Struct. & Algos.
  --> Returns the index position of the target if found,
  else returns None."""


def linear_search(lists, target):
    return next((i for i in range(len(lists)) if lists[i] == target), None)


"""
 --> a function that accepts index value
 --> if value is not none it prints its index position."""


def verify(index):
    if index is not None:
        print(f"Target found at index: {index}")
    print("Target not found")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = linear_search(numbers, 10)
verify(result)
