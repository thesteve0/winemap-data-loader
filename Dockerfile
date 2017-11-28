FROM python:latest

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD app.py /

ADD wineData.csv /

ARG server

ARG password

ARG user

ARG dbname

ENV server=$server

ENV password=$password

ENV user=$user

ENV dbname=$dbname