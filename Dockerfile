FROM centos/python-35-centos7

ENV server postgresql
ENV user username
ENV password password
ENV dbname wineDb

ADD loader.py /app/loader.py
