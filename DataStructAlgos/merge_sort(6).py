def merge_sort(lists):
    """
    Sort a list in ascending order.
    Returns a new sorted list.

    Divide: Find a midpoint of the list and divide into sublist.
    Conquer: Recursively sort the sublist created in previous step.
    Combine: Merge the sorted sublist created in previous step.
    Takes 0( n log n) time
    :param lists:
    :return:
    """
    if len(lists) <= 1:
        return lists

    left_half, right_half = split(lists)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)


def split(lists):
    """
    Divide the unsorted list at midpoint into sublist.
    Return two sublist left and right
    Takes overall 0(k log n) time.
    :param lists:
    :return:
    """
    mid = len(lists) // 2
    left = lists[:mid]
    right = lists[mid:]
    return left, right


def merge(left, right):
    """
    Merges tow list/array sorting i the process.
    Returns a new merged list.
    Runs in 0(n) time.
    :param left, right:
    :return:
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1
    return l


# Robust function
def verify_sorted(lists):
    n = len(lists)

    # if n == 0 or n == 1.
    if n in {0, 1}:
        return True
    return lists[0] < lists[1] and verify_sorted(lists[1:])


# test them out.
a_list = [54, 62, 93, 17, 77, 31, 44, 55, 20]
print(f"{a_list}: unsorted list")
l = merge_sort(a_list)
print(f"{l}: sorted list")
