# syntax=docker/dockerfile:1
FROM python:3.8.10-alpine

# # install app dependencies
# RUN apk update

# install app
WORKDIR /my-app/
COPY app/ requirements.txt .
RUN apk add --no-cache build-base && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del build-base

# final configuration
ENV FLASK_APP=main3.py
EXPOSE 8001
# CMD flask run --host 0.0.0.0 --port 8001
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8001"]
