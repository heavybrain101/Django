#!/bin/bash
python manage.py migrate
gunicorn help_prav_server.wsgi:application --workers=4 --threads=4 --bind=0.0.0.0:8000 --max-requests=1000 --log-level=info
