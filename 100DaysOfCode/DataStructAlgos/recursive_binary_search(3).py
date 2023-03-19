def recursive_binary_search(lists, target):
    if len(lists) == 0:
        return False
    else:
        midpoint = len(lists) // 2

        if lists[midpoint] == target:
            return True
        else:
            if lists[midpoint] < target:
                return recursive_binary_search(lists[midpoint + 1:], target)
            else:
                return recursive_binary_search(lists[:midpoint], target)


def verify(final_result):
    print(f"Target found: {final_result}")


lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# final_results = recursive_binary_search(lists, 1)
verify(recursive_binary_search(lists, 6))

# final_results = recursive_binary_search(lists, 11)
verify(recursive_binary_search(lists, 11))
