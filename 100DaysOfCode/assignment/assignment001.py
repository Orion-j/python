# In accessing an element in a list indicate by the index.
Colleagues = ["joe", "michael", "everette", "thompson"]
print(f'{Colleagues[0].title()} & {Colleagues[2].title()} welcome. \n')

print(len(Colleagues))  # length of list.

# tuples
first_tuple = ("Trains", "Buses", "Motorcycles", "Bicycles")
print(first_tuple)
for items in first_tuple:
    print(items, sep="")

floatNumber = 4.5  # working with numbers.
print(f"joe you got {floatNumber}")
# basic operations.
print(2 + 5)  # print integer.
print(4.5 - 2)  # print float.
print(5 * 2)  # multiplication.
print(4 / 2)  # division.

# strings manipulation.
Guest_name = "orion codes"
welcomeMessage = "Enjoy coding"

Guest_name1 = Guest_name.title()
Guest_name2 = Guest_name1.upper()

print(Guest_name1 + " \n" + Guest_name2)
# string concatenation.
print(f"{Guest_name1} {welcomeMessage}")

# program to display your details.
name = "Joe Orion"
age = 23
address = "Accra"
print(f"Hi {name}\nyour age: {age}\nFrom {address}")
