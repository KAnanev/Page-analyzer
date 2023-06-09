install:
	poetry install

test:
	poetry run pytest

lint:
	poetry run flake8 page_analyzer

test-coverage:
	poetry run pytest --cov=page_analyzer --cov-report xml

self_check:
	poetry check

check: self_check test lint

build: check
	poetry build

dev:
	poetry run flask --app page_analyzer:app --debug run

PORT ?= 8000
start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

start-testdb:
	docker-compose -f docker-compose.test.yml up -d

stop-testdb:
	docker-compose -f docker-compose.test.yml down

init_db:
	poetry run flask --app page_analyzer:app init-db

.PHONY: install test lint selfcheck check build dev start start-testdb stop-testdb init_db
