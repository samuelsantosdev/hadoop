FROM python:3.7-alpine
MAINTAINER Samuel Santos <samuelsantosdev@gmail.com>

RUN apk update && apk add gcc python3-dev musl-dev
COPY app /app
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh && pip install -r /app/requirements.txt && rm /app/requirements.txt
WORKDIR /app