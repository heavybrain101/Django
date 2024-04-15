#!/bin/bash
gunicorn project.wsgi:application --workers=4 --threads=4 --bind=0.0.0.0:8000 --max-requests=1000 --log-level=info
