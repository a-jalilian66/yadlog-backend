#!/bin/bash

echo "Applying staging DB migrations..."
python manage.py migrate --noinput

echo "Collecting static files for staging..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn for staging..."
exec gunicorn core.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --threads 2 \
    --timeout 60