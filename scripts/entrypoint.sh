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

echo "Applying database migrations..."
python manage.py migrate

if [ "$CREATE_SUPERUSER" = "true" ]; then
  echo "Creating superuser..."
  python manage.py shell << END
from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print("Superuser created.")
else:
    print("Superuser already exists.")
END
fi

echo "Starting Django development server..."
python manage.py runserver 0.0.0.0:8000
