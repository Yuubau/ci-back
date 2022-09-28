#!/bin/sh
until python manage.py migrate; do
    echo "Migrations failed, retrying in 3 seconds..."
    sleep 3
done
python -m gunicorn --bind=0.0.0.0:8000 core.wsgi
