FROM python:3.9-slim-buster

COPY . /root

WORKDIR /root

RUN pip install flask gunicorn

