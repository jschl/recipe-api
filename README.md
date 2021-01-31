# recipe-api

Api for storing and requesting recipes.

## Prerequirements

- install `requirements.txt`

## Usage (example)

```
python3 manage.py runserver
curl http://127.0.0.1:8000/recipes/ # get request for all recipes
curl http://127.0.0.1:8000/recipes/<id> # get request for specific recipe
curl http://127.0.0.1:8000/recipes/filter/<ingredient> # get request for filtering recipes by ingredient
curl -data "name=recipe&ingredients=ingredient1, ingredient2" http://127.0.0.1:8000/recipes/ # post request
