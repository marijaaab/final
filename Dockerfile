# syntax=docker/dockerfile:1
# FROM python:3.8.10-alpine
FROM ubuntu:20.04


# # install app dependencies
# RUN apk update

# install app
WORKDIR /my-app/
COPY app/ requirements.txt .
RUN RUN apt-get update && apt-get install -y python3 python3-pip && pip install -r requirements.txt
    
# final configuration
ENV FLASK_APP=main3.py
EXPOSE 8001
# CMD flask run --host 0.0.0.0 --port 8001
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8001"]
