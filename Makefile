lint:
	poetry run isort src tests
	poetry run flakeheaven lint src tests
	poetry run mypy src
