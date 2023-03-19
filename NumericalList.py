for number in range(1, 10):
    print(number)

# even numbers.
print(list(range(2, 11, 2)))

# playing with list.
numberSquare = []
for digit in range(2, 11, 2):
    digitSquared = digit ** 2
    numberSquare.append(digitSquared)
print(numberSquare)

# list of numbers.
numbers = list(range(1, 10))
print(f"{numbers}")

# list comprehension.
numberSquare = [digit ** 2 for digit in range(1, 11, )]
print(numberSquare)

# multiples of 3.
print(list(range(3, 31, 3)))

# cube comprehension.
cubeNumbers = [cubes ** 3 for cubes in range(1, 11)]
print(cubeNumbers)
