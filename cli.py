#!/usr/bin/env python3

import argparse

from src.currency_convert import CurrencyConverter


def main():
    converter = CurrencyConverter()

    parser = argparse.ArgumentParser(description='Currency converter')
    parser.add_argument('--amount', type=int, required=True, help="Amount which we want to convert")
    parser.add_argument('--input_currency', required=True,
                        help="Input currency in format of 3 letters symbol eg.(EUR)")
    parser.add_argument('--output_currency', default=None,
                        help="Output currency in format of 3 letters symbol eg.(USD)")
    args = parser.parse_args()

    output = converter.convert(args.amount, args.input_currency, args.output_currency)
    print(output)


if __name__ == "__main__":
    main()
