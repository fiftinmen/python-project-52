### Hexlet tests and linter status:
[![Actions Status](https://github.com/fiftinmen/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/fiftinmen/python-project-52/actions)
### CodeClimate Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/6d65ccfdd61107c53525/maintainability)](https://codeclimate.com/github/fiftinmen/python-project-52/maintainability)
### Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/6d65ccfdd61107c53525/test_coverage)](https://codeclimate.com/github/fiftinmen/python-project-52/test_coverage)

# Apllication description

Simple Task Manager web-application on Django framework. Provide elementary elements of task management site: user registration, task creation, statuses, labels.

Users can update and delete their accounts (if they are not associated with any tasks), create, update statuses, labels and tasks, assign statuses, labels and executors to tasks. Only task author can delete it. Labels and statuses can't be deleted if they are associated with tasks.

Application is based on Bootstrap.

# Prerequisites

To install and use this application you will need Python3.11 and poetry package manager. For Windows and MacOS you will need to setup Make. As database engine you can use PostgreSQL or integrated into Django SQLlite.

Also you will need to provide SECRET_KEY in you environment like this:
```
export SECRET_KEY = 123456
```
If you want to use PostgreSQL as database backend set DATABASE_URL like this:
```
export DATABASE_URL = postgresql://localhost/mydb?user=other&password=secret
```
Either application will use default SQLLite database stored in `task_manager.sqlite3` file.

Also you can provide Rollbar_Token for error and warning logging with Rollbar:
```
export ROLLBAR_TOKEN = some_token
```
Or you can set this variables in your `.env` file in application root directory (nearly `Makefile`).

# Installation

For quick installation use this command in command line:
```
make build
```

This will run `build.sh`. Here what it does:
```
make install
make make-n-migrate
poetry run python manage.py collectstatic --noinput
```