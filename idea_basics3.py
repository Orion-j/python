total = 0
count = 0
some_list = []  # initialize an empty list.

while True:
    user_input = input("enter number: ")  # take input from user.
    if user_input == 'done':
        break

    value = int(user_input)
    some_list.append(value)  # add value to list
    total = total + value
    count = count + 1
    avg = total / count

print('\nyour list', some_list)
print('total of your input', total)
print('Avg of numbers entered', avg)
