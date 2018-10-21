import requests


def currency_rates():
    url = "https://api.exchangeratesapi.io/latest"
    response = requests.get(url)
    json_data = response.json()
    return json_data["rates"]