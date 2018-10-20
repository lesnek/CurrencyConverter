#!/usr/bin/env python3

import argparse
import json

import requests


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
        from_currency, to_currency = self.symbol_to_currency(from_currency, to_currency)

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


    def symbol_to_currency(self, input_currency, output_currency):
        symbol_dict = {'€': 'EUR', '$': 'USD', 'Kč': 'CZK', '¥': 'CNY', '£': 'GBP'}

        new_input_currency = symbol_dict.get(input_currency, input_currency)
        new_output_currency = symbol_dict.get(output_currency, output_currency)

        return new_input_currency, new_output_currency
