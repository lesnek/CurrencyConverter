#!/usr/bin/env python3

import json

from src.currency_rates import currency_rates


class CurrencyConverter:
    def __init__(self, custom_data=None):
        self.rates = custom_data or currency_rates()

    def convert(self, amount_input, from_currency, to_currency=None):
        """
        Converting currency by EUR rates

        :param float amount_input: Amount which we want to convert
        :param str from_currency: Input currency - 3 letters currency symbol
        :param str to_currency: Requested currency - 3 letters currency symbol
        """
        # from_currency, to_currency = self.symbol_to_currency(from_currency, to_currency)

        output = {}
        
        if from_currency != "EUR":
            amount_input = amount_input / self.rates[from_currency]

        if (to_currency is None) or (to_currency is ''):
            for key in self.rates:
                output[key] = amount_input * self.rates[key]
        else:
            if to_currency == "EUR":
                output["EUR"] = amount_input
            else:
                output[to_currency] = amount_input * self.rates[to_currency]

        return output

    @staticmethod
    def symbol_to_currency(input_currency, output_currency):
        symbol_dict = {'€': 'EUR', '$': 'USD', 'Kč': 'CZK', '¥': 'CNY', '£': 'GBP'}

        new_input_currency = symbol_dict.get(input_currency, input_currency)
        new_output_currency = symbol_dict.get(output_currency, output_currency)

        # Fixture of lowercase input
        if output_currency is None:
            return new_input_currency.upper(), new_output_currency

        return new_input_currency.upper(), new_output_currency.upper()

    @staticmethod
    def output_formatter(amount, from_currency, output):
        result = {'input': {'amount': amount, 'currency': from_currency}, 'output': output}
        return json.dumps(result)
