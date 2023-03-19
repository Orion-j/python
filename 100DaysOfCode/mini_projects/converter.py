# using the  forex-python library.
# internet connection needed to successfully run the program.
from forex_python.converter import CurrencyRates

currencies = CurrencyRates()  # assign the object currencies to the currencyRate class

amount = int(input("amount --> "))
# takes currency to be converted from user.
from_currency = input("Currency to be converted --> ").upper()
# new currency requested
to_currency = input("To what currency --> ").upper()

print(f"converting {amount} {from_currency} to {to_currency}")
output_info = currencies.convert(from_currency, to_currency, amount)
print(f"Conversion done: {output_info}")

""" assignment 1 given by GANA.
    submission date --> 28th Nov,2022.
    submitted by --> Kwadjo Boadi-Mantey(Orion)
"""
