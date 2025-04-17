# --------------------------------------
# Stage 1: Frontend build with Node
# --------------------------------------
FROM node:20 AS frontend-build

# Set working directory for frontend build
WORKDIR /app

# Copy only package files first for layer caching
COPY ./frontend/package*.json ./frontend/
RUN cd frontend && npm install

# Copy full frontend and Django templates for Tailwind scanning
COPY ./frontend ./frontend
COPY ./src ./src

# Run Tailwind and JS build (now it can see src/templates and Python)
WORKDIR /app/frontend
RUN npm run build


# --------------------------------------
# Stage 2: Main Python + Django image
# --------------------------------------
FROM python:3.11-slim

# Set environment variables for clean Python output and correct path
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/src

# Set working directory for Django app
WORKDIR /app

# Install system dependencies for Django (gettext needed for translations)
RUN apt-get update && apt-get install -y gettext

# Install Python dependencies from production requirements
COPY requirements/ /app/requirements/
RUN pip install --upgrade pip \
    && pip install -r /app/requirements/production.txt

# Create folders for static and media files
RUN mkdir -p /app/staticfiles /app/media

# Copy Django source and app scripts
COPY ./src /app/src
COPY ./scripts /app/scripts

# Copy the built frontend output (dist) from previous stage
COPY --from=frontend-build /app/frontend/dist /app/frontend/dist
