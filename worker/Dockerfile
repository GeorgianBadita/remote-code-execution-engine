FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ENV PYTHONDONTWRITEBYTECODE=1

RUN mkdir /worker
WORKDIR /worker

COPY requirements.txt /worker/


RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install -r /worker/requirements.txt

COPY . /worker/
