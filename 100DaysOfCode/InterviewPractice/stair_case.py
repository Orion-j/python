# unique way s to climb stairs.
def count_way(N):
    if N <= 1:
        return 1

    countN1 = 1
    countN2 = 1

    for _ in range(2, N + 1):
        current_count = countN1 + countN2
        countN2 = countN1
        countN1 = current_count
    return countN1


print(count_way(4))
