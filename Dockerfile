FROM centos:latest

ENV server postgresql
ENV user username
ENV password password
ENV dbname wineDb

USER root

ADD loader.py /app/loader.py

ADD wineData.csv /opt/app-root/src/wineData.py

RUN yum -y install epel-release && yum clean all

RUN yum -y install python-pip && yum clean all

RUN pip install psycopg2

CMD ["python", "/app/loader.py"]