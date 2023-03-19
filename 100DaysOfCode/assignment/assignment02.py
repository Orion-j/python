# 100DaysOfCode Assignment 02.
# Author: Joe Boadi.
# TODO: rewrite the program to handle for "Fahrenheit{for both kelvin and celsius}"- Done 100%.
# re-programmed to handle temperatures in fahrenheit.

message = """Welcome, check your temperature.
We convert between kelvin, celsius & fahrenheit.
At the prompt, input data.
"""
print(message)
prompt = "Input C,K or F for Celsius(C), Kelvin(K) or Fahrenheit respectively!"
userData = int(input("Enter temperature: "))
userData_2 = input(f"{prompt}: ").upper()

if userData_2 == "C":  # handle temperature in Celsius.
    kelvin_Data = userData + 273.15
    fahrenheit_Data = int(userData * 1.8 + 32)
    print(f"Temperature in Kelvin(K) is {int(kelvin_Data)}K")
    print(f"Temperature in Fahrenheit(F) is {fahrenheit_Data}K")

elif userData_2 == "K":
    celsius_Data = userData - 273.15
    fahrenheit_Data = int(1.8 * int(userData - 273) + 32)
    print(f"Temperature in Celsius(C) is {int(celsius_Data)}\N{DEGREE SIGN}C")
    print(f"Temperature in Fahrenheit(F) is {fahrenheit_Data}K")

elif userData_2 == "F":
    celsius_Data = (userData - 32 * 5 / 9)
    kelvin_Data = (5 / 9 * (userData + 459.67))
    print(f"Temperature in Celsius(C) is {int(celsius_Data)}\N{DEGREE SIGN}C")
    print(f"Temperature in Kelvin(K) is {int(kelvin_Data)}K")

else:  # handle wrong input.
    print("Invalid input, try again.")
