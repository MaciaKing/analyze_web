#!/bin/bash

python manage.py makemigrations
python manage.py migrate

# Backgrounds jobs
#celery -A web_analyzer worker -l info &
#celery -A web_analyzer beat -l info &

# Runserver
python manage.py runserver 