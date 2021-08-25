# syntax=docker/dockerfile:1

FROM python:3.7

WORKDIR /application

COPY application/requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY application .

CMD [ "python3", "app.py"]
