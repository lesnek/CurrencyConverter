FROM python:3
ADD currency_convert.py /
RUN pip install pystrich
CMD ["python", "./currency_convert.py"]
