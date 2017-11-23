FROM centos:latest

ENV server postgresql
ENV user username
ENV password password
ENV dbname wineDb

ADD loader.py /app/loader.py
