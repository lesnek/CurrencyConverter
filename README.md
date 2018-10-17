# Currency converter 
Intro test for kiwi.com: Currency converter is made into server API and CLI

## Currency CLI application
### Instalation
install docker volume
```
docker-compose currency_convert.py
```
### Usage
For simple convert
```
./currency_convert.py --amount [amount] --input_currency [currency symbol] --output_currency [currency symbol]
```
For example
```
./currency_convert.py --amount 100 --input_currency EUR --output_currency USD
```
If you didn't specify --output_currency, you'll get convertition into all currencies from European Bank API
