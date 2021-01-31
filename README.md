# annotator

Api for storing and requesting recipes.

## Prerequirements

- install `requirements.txt`

## Usage (example)

```
python3 manage.py runserver
curl http://127.0.0.1:8000/recipes/ # get request
curl -data "name=recipe&ingredients=ingredient1, ingredient2" # post request
