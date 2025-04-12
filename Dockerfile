# Dockerfile

FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements/ requirements/
RUN pip install --upgrade pip \
    && pip install -r requirements/base.txt

# Copy project
COPY . .

# Collect static files (only used in prod)
RUN mkdir -p /app/staticfiles /app/media

# Default command
CMD ["bash", "scripts/entrypoint.sh"]