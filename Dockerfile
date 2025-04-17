# --------------------------------------
# Stage 1: Frontend build with Node
# --------------------------------------
FROM node:20 AS frontend-build

WORKDIR /app/frontend

COPY ./frontend/package*.json ./
RUN npm install

COPY ./frontend/ ./
RUN npm run build

# --------------------------------------
# Stage 2: Main Python + Django image
# --------------------------------------
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src

WORKDIR /app

RUN apt-get update && apt-get install -y gettext

COPY requirements/ /app/requirements/
RUN pip install --upgrade pip \
    && pip install -r /app/requirements/production.txt

RUN mkdir -p /app/staticfiles /app/media

COPY ./src /app/src
COPY ./scripts /app/scripts
COPY --from=frontend-build /app/frontend/dist /app/frontend/dist
