#!/bin/sh

# Wait for the database
python manage.py wait_for_db

# Migrate Database
python manage.py migrate

exec "$@"
