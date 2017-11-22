FROM centos:latest

USER root

ENV server postgresql
ENV user username
ENV password password
ENV dbname wineDb

ADD loader.py /opt