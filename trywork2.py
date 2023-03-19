def try_code():
    total = []
    for i in range(2,101):
        if not i % 5 or not i % 7:
            total.append(i)
    print(sum(total))


try_code()