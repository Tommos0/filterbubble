# Dockerfile
FROM python:3

RUN apt-get update && apt-get install -y python-pdal

ADD ./requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

WORKDIR /app/

EXPOSE 8000

