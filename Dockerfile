# syntax=docker/dockerfile:1
# FROM python:3.8.10-alpine
FROM python:3.8.10-alpine


# # install app dependencies
# RUN apk update

# install app
WORKDIR /my-app/
COPY app/ requirements.txt .
RUN apk update && apk add gcc g++ zlib-dev make python3-dev && pip3 install wheel && pip3 install matplotlibpip install -r requirements.txt
    
# final configuration
ENV FLASK_APP=main3.py
EXPOSE 8001
# CMD flask run --host 0.0.0.0 --port 8001
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8001"]
