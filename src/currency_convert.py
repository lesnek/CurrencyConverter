
import json
import sys

import requests

class CurrencyConverter:
    def __init__(self, url="https://api.exchangeratesapi.io/latest"):
        response  = requests.get(url) 
        json_data = response.json()
        self.rates = json_data["rates"]
        
    def convert(self, amount_input, from_currency, to_currency=None):
        '''
        Converting currency by EUR rates

        :param float amount: Amount which we want to convert
        :param str from_currency: Input currency - 3 letters currency symbol
        :param str to_currency: Requested currency - 3 letters currency symbol
        '''
        result_dict = {}
        if from_currency != "EUR":
            amount = amount_input / self.rates[from_currency]
        if (to_currency == None):
            for key in self.rates:
                converted = amount * self.rates[key]
                result_dict[key] = converted
        else:
            if to_currency == "EUR":
                result_dict["EUR"] = amount
            else:
                result_dict[to_currency] = amount * self.rates[to_currency]
        return self.printFormatter(amount_input, from_currency, result_dict)

    # Finish the output format
    def printFormatter(self, amount_input, from_currency, result):
        output = dict()
        output["input"] = {"amount": amount_input, "currency": from_currency}
        output["output"] = result
        return output

converter = CurrencyConverter()

print(converter.convert(100, "CZK", "EUR"))
print(converter.convert(100, "CZK", "CZK"))
