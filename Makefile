all: run

clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log*

format:
	black -l 80 daylight

type-check: format
	mypy daylight

deps-dev: venv
	pip install --user -r requirements_dev.txt

deps: venv
	pip install --user -r requirements.txt

venv:
	virtualenv --python=python3 venv && venv/bin/python setup.py develop

run: venv deps
	FLASK_APP=daylight DAYLIGHT_SETTINGS=../settings.cfg venv/bin/flask run

test: venv
	DAYLIGHT_SETTINGS=../settings.cfg venv/bin/python -m unittest discover -s tests

sdist: venv test
	venv/bin/python setup.py sdist
