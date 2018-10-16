FROM python:3
ADD currency_convert.py /
CMD ["python", "./currency_convert.py"]
