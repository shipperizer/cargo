PYTHON=/usr/bin/env python
PIP=/usr/bin/pip
PACKAGES=python python-pip
DEPENDENCIES=requirements.txt
MOD_NAME=cargo
VERSION_NUMBER?="0.0.99"
WSGI=gunicorn
MSG?="change-me-plz"

.PHONY: info install test

clean-build:
		rm -rf build/ dist/
		rm -rf $(MOD_NAME)-$(VERSION_NUMBER)_* $(MOD_NAME).egg-info
		rm -rf docs/_build

info:
		@echo "****************************************************************"
		@echo "To build this project you need these dependencies: $(PACKAGES)"
		@echo "Check requirements.txt/setup.py file to see python dependencies."
		@echo "****************************************************************"
		@echo "USAGE:"
		@echo "- To install dependencies: make install"
		@echo "- To launch: make [start|stop|debug]"
		@echo "- To test: make test   **unit(integration)test"

start: db-upgrade
		$(WSGI) -w 4 "$(MOD_NAME).bootstrap:app"

debug: db-upgrade
		DEBUG=1 $(PYTHON) "$(MOD_NAME)/bootstrap" runserver

debug-gun: db-upgrade
		DEBUG=1 $(WSGI) -w 4 "$(MOD_NAME).bootstrap:app"

install: build-reqs info
		@echo "Python dependencies"
		$(PIP) install -r $(DEPENDENCIES)

build-reqs:
		$(PIP) install --upgrade pip
		$(PIP) install --upgrade setuptools
		# pip you are so stupid http://stackoverflow.com/a/25288078
		$(PIP) install --upgrade setuptools

test: build-reqs
		touch conftest.py
		$(PYTHON) setup.py test -a '--cov $(MOD_NAME) --cov-config .coveragerc --cov-report xml --junit-xml=results.xml'
		rm conftest.py

db-init:
		$(PYTHON) "$(MOD_NAME)/bootstrap.py" db init
		$(PYTHON) "$(MOD_NAME)/bootstrap.py" db migrate

db-migrate:
		$(PYTHON) "$(MOD_NAME)/bootstrap.py" db migrate -m"$(MSG)"

db-upgrade:
		$(PYTHON) "$(MOD_NAME)/bootstrap.py" db upgrade
