# Currency converter 
[![Build Status](https://travis-ci.org/lesnek/CurrencyConverter.svg?branch=master)](https://travis-ci.org/lesnek/CurrencyConverter)<br />
<br />
Intro test for kiwi.com: Currency converter made into server API and CLI application

## Currency CLI application
### Installation
install python requirements
```
pip install -r requirements.txt
```
### Usage
For simple convert
```
./currency_convert.py --amount [amount] --input_currency [currency symbol] --output_currency [currency symbol]
```
For example convert Euros to US dollars
```
./currency_convert.py --amount 100 --input_currency EUR --output_currency USD
```
If you didn't specify --output_currency, you'll get convertition into all currencies from European Bank API

## Currency server application
### Installation
```
docker build -t currencyconverter .
docker run -p 5000:5000 currencyconverter
```
### Usage
Server is on address localhost:5000, you can try:
```
localhost:5000/currency_converter?amount=200&input_currency=USD&output_currency=EUR
```

## Testing
Testing of application is provided by pytests
```
python -m pytest tests/
```