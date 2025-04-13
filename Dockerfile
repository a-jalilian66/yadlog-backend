# Dockerfile

FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/src

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements/ /app/requirements/
RUN pip install --upgrade pip \
    && pip install -r /app/requirements/base.txt

RUN apt-get update && apt-get install -y gettext

# Copy project
COPY src/ /app/src/
COPY scripts/ /app/scripts/

# Collect static files (only used in prod)
RUN mkdir -p /app/staticfiles /app/media

# Default command
CMD ["bash", "/app/scripts/entrypoint.sh"]