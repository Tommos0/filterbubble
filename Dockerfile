# Dockerfile
FROM python:3

ADD ./requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

WORKDIR /app/

CMD python manage.py runserver

ENV PORT 3000
EXPOSE 3000

