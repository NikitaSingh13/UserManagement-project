#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python UserManagement/manage.py collectstatic --no-input
python UserManagement/manage.py migrate
