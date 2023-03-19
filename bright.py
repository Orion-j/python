# 5.8 list of usernames and a "welcoming message".
import collections

HelloAdmin = ['Admin', 'Bright', 'Orion', 'Ella']
for name in HelloAdmin:
    if name == 'Admin':
        print(f"Hello {name} check the reports\n")
    else:
        print(f"Hello {name},logged successfully")

HelloAdmin.clear()  # 5.9 remove values from list.
if not HelloAdmin:  # check if list is empty.
    print("\nAdd more users, admin.\n")

# 5.10 checking username.
current_usernames = ['Eli', 'Coco', 'York', 'Ko-vs', 'nami']
current_usernames.sort()
new_users = ['York', 'Coco', 'Eli', 'Nams', 'Lad']
new_users.sort()

print(' '.join(current_usernames))
print(' '.join(new_users))

if current_usernames == new_users:
    print("Choose another username")
else:
    print("name available.")



