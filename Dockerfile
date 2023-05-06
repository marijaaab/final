# syntax=docker/dockerfile:1
FROM python:3.8.10-alpine

# install app dependencies
RUN apk update

# install app
COPY requirements.txt /my-app/
COPY app/ /my-app
RUN pip install -r /my-app/requirements.txt
WORKDIR /my-app/

# final configuration
# ENV FLASK_APP=main3.py
EXPOSE 8001
CMD flask run --host 0.0.0.0 --port 8001
