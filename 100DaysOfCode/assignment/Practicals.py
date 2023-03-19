# store values in variables & perform addition.
firstNumber = 30
secondNumber = 20
print(f"{firstNumber} + {secondNumber} is {firstNumber+secondNumber} \n")

# program to display your details.
name = "Joe Orion"
age = 23
address = "Accra"
print(f"Hi {name}\nyour age: {age}\nFrom {address}")

# program to compute future of a specified amount.
initialAmount = 100_000
ints = 3.5
years = 7
futureValue = initialAmount*((1+0.01*ints) ** years)
print(f"expected outcome: {round(futureValue)}")
