FROM python:3.10-alpine
LABEL com.iam.app.vendor="IAm Ltd"
LABEL version="1.0"
LABEL com.iam.app.authors="santhosh.r.subramani@outlook.com"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D admin
USER admin