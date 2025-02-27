#!/bin/sh
set -e

echo "Initializing the database..."

python -m scripts.init_db

echo "Starting gunicorn..."
exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:server
