.PHONY: start build dev test setup install db-clean make-n-migrate makemigrations migrate \
		shell lint test-coverage test-report

MANAGE := poetry run python manage.py


PORT ?= 8000

start:
	poetry run gunicorn task_manager.wsgi

build:
	./build.sh

dev:
	poetry run python manage.py runserver

test:
	@poetry run python manage.py test

setup: db-clean install migrate

install:
	@poetry install

db-clean:
	@rm db.sqlite3 || true

 make-n-migrate:
	@$(MANAGE) makemigrations
	@$(MANAGE) migrate

 makemigrations:
	@$(MANAGE) makemigrations

migrate:
	@$(MANAGE) migrate

shell:
	@$(MANAGE) shell_plus --ipython

lint:
	@poetry run flake8 task_manager

test-coverage:
	poetry run coverage run manage.py test task_manager
	poetry run coverage xml

test-report:
	poetry run coverage report