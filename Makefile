install:
	poetry install


test:
	poetry run pytest

lint:
	poetry run flake8 fizz_buzz tests