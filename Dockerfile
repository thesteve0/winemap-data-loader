FROM centos:latest

USER root

RUN mkdir -p /app
WORKDIR /app

ENV server postgresql
ENV user username
ENV password password
ENV dbname wineDb

ADD loader.py /app