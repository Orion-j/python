new_list = [1, 2, 3, ]
# access and read data from list.
print(new_list[1])  # fetches the second value in list.
# print(new_list[5])  # returns error;  invalid index

if 1 in new_list:
    print(True)

for n in new_list:
    if new_list == 1:
        print(True)
    break

for n in new_list:
    if n == 1:
        print(True)
    break
# inserting and deleting values in an array.
new_list.append(4)
print(new_list)
new_list.remove(3)
print(new_list)

# inserting a list into a list.
new_list.extend([5, 6, 7])
print(new_list)