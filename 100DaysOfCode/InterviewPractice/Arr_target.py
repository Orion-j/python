def arr_target(arr, target):
    """
    Returns the indices of two values in the input list that
    adds up to the target value.
    :param arr: input list
    :param target: sum value
    :return:'s a list of two indices of value that add up
    to the target value.
    """
    result = {}  # store the index and value of the elements
    for i in range(len(arr)):
        remainder = target - arr[i]
        # result.extend([i, j] for j in arr if arr[j] == remainder)
        if remainder in result:
            return [result[remainder], i]
        result[arr[i]] = i
    return []


# TODO - debug to return only two indexes for elements that sums up to the target -> Done!
final_result1 = arr_target([1, 2, 3, 4, 7], 6)
print(final_result1)
final_result2 = arr_target([1, 2, 3, 4, 7], 9)
print(final_result2)