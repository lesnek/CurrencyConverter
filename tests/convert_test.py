import pytest


@pytest.mark.parametrize("amount,from_currency,to_currency,result", [
    (100, "B", "D", {'D': 400.0}),
    (100, "B", "D", {'D': 400.0}),
    (100, "B", "D", {'D': 400.0}),
    (100, "B", "D", {'D': 400.0}),
    (100, "B", "D", {'D': 400.0}),
    (100, "B", "D", {'D': 400.0}),
])
def test_convert(amount, from_currency, to_currency, result):
    from src.currency_convert import CurrencyConverter

    test_dict = {"A": 0, "B": 0.5, "C": 1, "D": 2}
    converter = CurrencyConverter(test_dict)

    assert converter.convert(amount, from_currency, to_currency) == result
