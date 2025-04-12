
#!/bin/bash

echo "Waiting for postgres to be ready..."
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
echo "PostgreSQL is available!"

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec gunicorn core.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 4 \
    --threads 2 \
    --timeout 120
