FROM python:3.11
RUN mkdir /usr/backend

WORKDIR /usr/backend
COPY ./backend/req.txt /usr/backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install -r ./req.txt

COPY ./ /usr/backend

