#!/bin/bash

echo "Waiting for postgres (staging)..."
python << END
import time
import socket
while True:
    try:
        sock = socket.create_connection(("db", 5432), timeout=1)
        sock.close()
        break
    except OSError:
        time.sleep(1)
END
echo "PostgreSQL is available (staging)!"

echo "Applying staging DB migrations..."
python src/manage.py migrate --noinput

echo "Collecting static files for staging..."
python src/manage.py collectstatic --noinput

echo "Starting Gunicorn for staging..."
exec gunicorn yadlog.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --threads 2 \
    --timeout 60
