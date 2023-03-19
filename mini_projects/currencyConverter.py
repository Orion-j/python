import requests
#from forex_python import CurrencyRates


class Currency_converter:
    # conversion_rates = {}  # store conversion rate.
    def __init__(self, source):
        self.data = requests.get(source).json()
        self.conversion_rates = self.data['rates']

    def conversion(self, currency_from, to_currency, amt):
        requested_amt = amt
        if currency_from != 'EUR':
            amt = amt / self.conversion_rates[to_currency]
            amt = round(amt * self.rates[to_currency], 2)
            print(f"{requested_amt} {currency_from} = {amt} {to_currency}")


if __name__ == "__main__":
    Access_key = 'GjLhaaioZChLaCnK8qizaMWapcXk9hTf'
    source = str.__add__('http://data.fixer.io/api/latest?access_keys=', Access_key)
    currency = Currency_converter(source)  # assign object to the class.
    country_currency = input("Currency from country? --> ")
    country_convert = input("Convert currency into? --> ")
    amt = int(input("Amount --> "))
    currency.conversion_rates(country_currency, country_convert, amt)
