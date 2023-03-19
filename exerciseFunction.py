def whileLoop():  # encapsulate exercise.py into a function.

    # list types of sandwiches:
    sandwich_orders = ['chicken sandwich', 'grilled cheese', 'ham sandwich', 'sea food sandwich', 'grilled chicken']
    finished_sandwich = []  # an empty list to store new values.
    print('I made: ')
    [print(f"{sandwich_made}.") for sandwich_made in sandwich_orders]
    print("\n")

    print("Completed order: ")
    while sandwich_orders:
        sandwich_order = sandwich_orders.pop()
        print(f"{sandwich_order}")
        finished_sandwich.append(sandwich_order)
    print("\n")

    # contains some repeated values which will be trimmed.
    sandwich_orders1 = ['chicken', 'grilled cheese', 'ham', 'sea food', 'chicken', 'chicken']
    print(f"sandwich: {sandwich_orders1}")
    while 'chicken' in sandwich_orders1:
        sandwich_orders1.remove('chicken')
    print(f"Ran out of chicken sandwich: {sandwich_orders1}")


whileLoop()
#  100 Days of coding: Day 20.
