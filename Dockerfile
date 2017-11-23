FROM centos:latest

ENV server postgresql
ENV user username
ENV password password
ENV dbname wineDb

USER root

ADD loader.py /app/loader.py

CMD ["/bin/bash", "sleep infinity"]