#!/bin/bash
set -e
echo "--- Installing Dependencies ---"
python3.12 -m pip install -r requirements.txt
echo "--- Collecting Static Files ---"
python3.12 manage.py collectstatic --noinput --clear
echo "--- Running Database Migrations ---"
python3.12 manage.py migrate