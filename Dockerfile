# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# install app
COPY requirements.txt /my-app/
COPY app/ /my-app
RUN pip install -r /my-app/requirements.txt

# final configuration
ENV FLASK_APP=main3.py
EXPOSE 8001
CMD flask run --host 0.0.0.0 --port 8001
