FROM python:3-alpine

WORKDIR /app
ADD . .

RUN pip install -r requirements.txt

ENV FLASK_APP=server.py
CMD ["flask", "run", "--host", "0.0.0.0"]
