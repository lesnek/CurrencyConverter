import json

from flask import Flask, request

from src.currency_convert import CurrencyConverter


app = Flask(__name__)
converter = CurrencyConverter()


@app.route("/currency_converter")
def on_get():
    amount = request.args.get("amount", 1)
    input_currency = request.args.get("input_currency", "EUR")
    output_currency = request.args.get("output_currency")
    
    output = converter.convert(amount, input_currency, output_currency)
    
    return json.dumps({"input": {}, "output": output}), 200
	


