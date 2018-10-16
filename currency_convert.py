
import requests
import json
import sys

class CurrencyConverter:
    def __init__(self, url="https://api.exchangeratesapi.io/latest"):
        req  = requests.get(url) 
        jsonData = req.json()
        self.rates = jsonData["rates"]


    # Converting currency by EUR rates
    def convert(self, amount, from_c, to_c=None):
        result_arr = dict()
        if from_c != "EUR":
            amount = amount / self.rates[from_c]
        if (to_c == None):
            for key in self.rates:
                converted = amount * self.rates[key]
                result_arr[key] = converted
            return result_arr
        else:
            if to_c == "EUR":
                return amount
            else:
                return amount * self.rates[to_c]

converter = CurrencyConverter()

print(converter.convert(100000, "CZK"))
