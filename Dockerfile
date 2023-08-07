FROM python:3.8.10-alpine

# install app & dependencies, run the update
WORKDIR /my-app/
COPY app/ requirements.txt .
RUN apk update && \
    pip install --no-cache-dir -r requirements.txt

# final configuration
ENV FLASK_APP=main3.py
EXPOSE 8001
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8001"]
