#!/bin/bash

echo "dropping database django-medications"
dropdb django-medications

echo "creating database django-medications"
createdb django-medications

python manage.py makemigrations

python manage.py migrate

echo "inserting users"
python manage.py loaddata jwt_auth/seeds.json

echo "inserting category"
python manage.py loaddata category/seeds.json

echo "inserting brand"
python manage.py loaddata brand/seeds.json

echo "inserting products"
python manage.py loaddata products/seeds.json

echo "inserting requests"
python manage.py loaddata requests/seeds.json