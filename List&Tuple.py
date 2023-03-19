# List "[]" - a collection of items in a particular order(Read more on list).
# Can contain all kinds of data types.

# accessing an element in a list indicate by the index.
Colleagues = ["joe", "michael", "everette", "thompson"]
print(f'{Colleagues[0].title()} & {Colleagues[2].title()} welcome. \n')

Colleagues.sort()  # sorting list in alphabetical order.
print(Colleagues)

Colleagues.sort(reverse=True)  # sorting in reverse order.
print(Colleagues)

print(len(Colleagues))  # length of list.

# importance of len - to determine the amount of data -
# one have to manage in visualization.

for colleague in Colleagues:  # Looping through an entire list.
    print(f"{colleague} come for dinner")
print("Thanks for coming!")

# tuples
first_tuple = ("Trains", "Buses", "Motorcycles", "Bicycles")
print(first_tuple)

for items in first_tuple:
    print(items, sep="")
