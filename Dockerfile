FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
  apt-get install -y --no-install-recommends git curl && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .