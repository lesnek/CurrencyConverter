
import json
import sys

import requests
import argparse

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

    def printFormatter(self, amount_input, from_currency, result_dict):
        '''
        Create needed output format

        :param float: Amount which we want to convert
        :param str from_currency: Input currency - 3 letters currency symbol
        :param dict result_dict: Dictionary of finished convertitions {"Symbol": "Amount"}
        '''
        output = {}
        output["input"] = {"amount": amount_input, "currency": from_currency}
        output["output"] = result_dict
        return output

    def cli_input(self):
        parser = argparse.ArgumentParser(description='Currency converter')
        parser.add_argument('--amount', type=int, help="Amount which we want to convert")
        parser.add_argument('--input_currency', help="Input currency in format of 3 letters symbol eg.(EUR)")
        parser.add_argument('--output_currency', default=None, help="Output currency in format of 3 letters symbol eg.(USD)")
        args = parser.parse_args()
        result = self.convert(args.amount, args.input_currency, args.output_currency)
        return result

print(CurrencyConverter().cli_input())