#!/usr/bin/env python3

import requests
import argparse
import json


# from .currency_rates import CurrencyRates


class CurrencyConverter:
    def __init__(self, custom_dict=None, url="https://api.exchangeratesapi.io/latest"):
        response = requests.get(url)
        json_data = response.json()

        if custom_dict is None:
            # self.rates = CurrencyRates.currency_rates(
            self.rates = json_data["rates"]
        else:
            self.rates = custom_dict

    def convert(self, amount_input, from_currency, to_currency=None):
        """
        Converting currency by EUR rates

        :param float amount_input: Amount which we want to convert
        :param str from_currency: Input currency - 3 letters currency symbol
        :param str to_currency: Requested currency - 3 letters currency symbol
        """
        result_dict = {}
        amount = amount_input
        if from_currency != "EUR":
            amount_input = amount_input / self.rates[from_currency]
        if to_currency is None:
            for key in self.rates:
                converted = amount_input * self.rates[key]
                result_dict[key] = converted
        else:
            if to_currency == "EUR":
                result_dict["EUR"] = amount_input
            else:
                result_dict[to_currency] = amount_input * self.rates[to_currency]
        return result_dict

    @staticmethod
    def print_formatter(amount_input, from_currency, result_dict):
        """
        Create needed output format

        :param float amount_input: Amount which we want to convert
        :param str from_currency: Input currency - 3 letters currency symbol
        :param dict result_dict: Dictionary of finished convertitions {"Symbol": "Amount"}
        """
        output = {"input": {"amount": amount_input, "currency": from_currency}, "output": result_dict}
        return json.dumps(output)

    def cli_input(self):
        parser = argparse.ArgumentParser(description='Currency converter')
        parser.add_argument('--amount', type=int, required=True, help="Amount which we want to convert")
        parser.add_argument('--input_currency', required=True,
                            help="Input currency in format of 3 letters symbol eg.(EUR)")
        parser.add_argument('--output_currency', default=None,
                            help="Output currency in format of 3 letters symbol eg.(USD)")
        args = parser.parse_args()
        symbol_array = self.symbol_to_currency(args.input_currency, args.output_currency)
        result = self.convert(args.amount, symbol_array[0], symbol_array[1])
        return result

    def symbol_to_currency(self, input_currency, output_currency):
        symbol_dict = {'€': 'EUR', '$': 'USD', 'Kč': 'CZK', '¥': 'CNY', '£': 'GBP'}
        if input_currency in symbol_dict:
            input_currency = symbol_dict[input_currency]
        if output_currency in symbol_dict:
            output_currency = symbol_dict[output_currency]

        return [input_currency, output_currency]