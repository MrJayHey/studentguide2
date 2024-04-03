#!/bin/bash

apt-get update

sleep 30

python manage.py migrate

python manage.py collectstatic --noinput

# playwright install

# playwright install-deps

# python manage.py parse

exec gunicorn --bind 0.0.0.0:8000 guide.wsgi
