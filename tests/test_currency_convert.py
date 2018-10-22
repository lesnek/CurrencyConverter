import pytest


@pytest.mark.parametrize("amount,from_currency,to_currency,result", [
    (100, "B", "D", {'D': 400.0}),
    (100, "A", "D", {'D': 2000.0}),
    (100, "B", "A", {'A': 20.0}),
    (100, "C", "A", {'A': 10.0}),
    (100, "C", None, {'A': 10.0, "B": 50, "D": 200, "C": 100}),
])
def test_convert(amount, from_currency, to_currency, result):
    from src.currency_converter import CurrencyConverter

    test_dict = {"A": 0.1, "B": 0.5, "C": 1, "D": 2}
    converter = CurrencyConverter(test_dict)

    assert converter.convert(amount, from_currency, to_currency) == result


@pytest.mark.parametrize("input_currency, output_currency, result_arr", [
    ("eur", "usd", ("EUR", "USD")),
    ("eur", "$", ("EUR", "USD")),
    ("€", "usd", ("EUR", "USD")),
    ("€", "$", ("EUR", "USD")),
])
def test_convert_symbol(input_currency, output_currency, result_arr):
    from src.currency_converter import CurrencyConverter

    converter = CurrencyConverter()

    assert converter.symbol_to_currency(input_currency, output_currency) == result_arr
