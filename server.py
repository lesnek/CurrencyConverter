from flask import Flask, request

from src.currency_convert import CurrencyConverter


app = Flask(__name__)
converter = CurrencyConverter()


@app.route("/currency_converter")
def on_get():
    amount = int(request.args.get("amount", 1))
    input_currency = request.args.get("input_currency", "EUR")
    output_currency = request.args.get("output_currency", None)
    
    converted_dict = converter.convert(amount, input_currency, output_currency)
    output = converter.output_formatter(amount, input_currency, converted_dict)
    
    return output, 200
