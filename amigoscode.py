# working with sets.

letters = {'a', 'b', 'c', 'd', 'e'}
letters1 = {'f', 'g', 'h', 'i'}
union = letters | letters1
intersection = letters & letters

# in sets values are stored in no particular order
print(f'Union: {union}\nIntersection: {intersection}\n')

# dictionary
person = {
    'name': 'Joe boadi',
    'age': 23,
    'location': 'Ghana',
    'profession': 'software engineer',
    'company': {'position':'Snr. Software Eng.',
                'role':'project manager',
                'start': '01/06/24',
                'location': 'USA/Rmote'
                }
}

print(person['name'], person['age'], person['profession'])
print(person.keys())
print(person.values(), '\n')

# for loop
names = ['adwoa', 'kojo', 'kwabena', 'akua', 'yaw']
for name in names:
    print(name)

# using for loop sum the values in a list.
numbers = [1, 3, 5, 6, 7, 9]
total = 0
for number in numbers:
    total = total + number
print(total)
