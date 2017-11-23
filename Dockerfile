FROM centos:latest

ENV server postgresql
ENV user username
ENV password password
ENV dbname wineDb

USER root

ADD loader.py /app/loader.py

RUN yum -y install epel-release && yum clean all

RUN yum -y install python-pip && yum clean all

RUN pip install -r requirements.txt

CMD ["python", "/app/loader.py"]