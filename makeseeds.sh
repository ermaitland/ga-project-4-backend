#!/bin/bash

echo "creating brand/seeds.json"
python manage.py dumpdata brand --output brand/seeds.json --indent=2;

echo "creating category/seeds.json"
python manage.py dumpdata category --output category/seeds.json --indent=2;

echo "creating products/seeds.json"
python manage.py dumpdata products --output products/seeds.json --indent=2;

echo "creating requests/seeds.json"
python manage.py dumpdata requests --output requests/seeds.json --indent=2;

echo "creating FAQs/seeds.json"
python manage.py dumpdata FAQs --output FAQs/seeds.json --indent=2;

echo "creating jwt_auth/seeds.json"
python manage.py dumpdata jwt_auth --output jwt_auth/seeds.json --indent=2;