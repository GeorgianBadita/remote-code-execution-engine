FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

RUN mkdir /worker
WORKDIR /worker

COPY requirements.txt /worker/

# Install g++
RUN apk add --no-cache g++ 

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /worker/requirements.txt


COPY . /worker/
