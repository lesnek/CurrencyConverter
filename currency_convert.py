
import requests
import json
import sys

class CurrencyConverter:
    def __init__(self, url="https://api.exchangeratesapi.io/latest"):
        req  = requests.get(url) 
        jsonData = req.json()
        self.rates = jsonData["rates"]
        self.result_dict = dict()


    # Converting currency by EUR rates
    def convert(self, amount, from_c, to_c=None):
        if from_c != "EUR":
            amount = amount / self.rates[from_c]
        if (to_c == None):
            for key in self.rates:
                converted = amount * self.rates[key]
                self.result_dict[key] = converted
        else:
            if to_c == "EUR":
                self.result_dict["EUR"] = amount
            else:
                self.result_dict[to_c] = amount * self.rates[to_c]
        return self.printFormatter(amount, from_c, self.result_dict)

    # Finish the output format
    def printFormatter(self, amount, input_currency, result):
        output = dict()
        output["input"] = {"amount":amount, "currency":input_currency}
        output["output"] = result
        return output


converter = CurrencyConverter()

print(converter.convert(100, "CZK", "EUR"))
