# build.sh
#!/bin/bash
set -e  # Exit on error

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running migrations..."
python manage.py migrate

echo "Creating superuser..."
python manage.py createsuperuser --noinput || true