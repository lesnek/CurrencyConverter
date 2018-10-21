from flask import Flask, request

from src.currency_converter import CurrencyConverter


app = Flask(__name__)
converter = CurrencyConverter()


@app.route("/currency_converter")
def on_get():
    amount = int(request.args.get("amount", 1))
    input_currency = request.args.get("input_currency", "EUR")
    output_currency = request.args.get("output_currency", None)

    from_currency, to_currency = converter.symbol_to_currency(input_currency, output_currency)
    converted_dict = converter.convert(amount, from_currency, to_currency)
    output = converter.output_formatter(amount, from_currency, converted_dict)
    
    return output, 200
