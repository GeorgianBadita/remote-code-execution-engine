FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /app

COPY requirements.txt /app/


RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install -r /app/requirements.txt

COPY ./remote_coding_compilation_engine /app/remote_coding_compilation_engine
