#!/bin/sh

echo "Waiting database start"
python3 backend_pre_start.py
sleep 10
echo "Database started"

alembic upgrade head

exec "$@"