FROM python:3.9.7-slim-buster

ADD requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

ADD . .

RUN ["python", "app.py"]