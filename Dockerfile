# syntax=docker/dockerfile:1
FROM nvidia/cuda:12.1.0-base-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive
ARG BUILD_TIME=undefined
ARG BUILD_VERSION=undefined

ENV RR_BUILD_TIME=$BUILD_TIME
ENV RR_BUILD_VERSION=$BUILD_VERSION
ENV PYTHONPATH=/app

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-pip && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
