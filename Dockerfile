# base image
FROM python:latest
# create app directory
RUN mkdir /usr/src/app
# set a directory for the app
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt
# copy project
COPY . .