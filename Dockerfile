FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /documents

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY documents .
