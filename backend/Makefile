lint:
	black --check .
	flake8
	isort --check-only .

test:
	coverage run -m pytest
	coverage report
	coveralls

check: lint test

format_code:
	isort .
	black .
