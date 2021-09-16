PYTHON ?= python
PIP ?= $(PYTHON) -m pip
COVERAGE ?= coverage
PYCODESTYLE ?= pycodestyle
FLAKE8 ?= flake8
NPM          ?= npm
NPX          ?= npx
GUNICORN     ?= gunicorn


help: Makefile
	@echo
	@echo " Choose a command run in Cookie:"
	@echo
	@sed -n 's/^##//p' $< | column -t -s ':' |  sed -e 's/^/ /'
	@echo


## config: Install dependencies.
.PHONY: config
config:
	$(PIP) install -r requirements.test.txt
	$(PIP) install -r requirements.txt


## lint-pycodestyle: PyCode Style Lint
.PHONY: lint-pycodestyle
lint-pycodestyle:
	@echo "\n>> ============= Pycodestyle Linting ============= <<"
	@find app -type f -name \*.py | while read file; do echo "$$file" && $(PYCODESTYLE) --config=./pycodestyle --first "$$file" || exit 1; done


## lint-flake8: Flake8 Lint.
.PHONY: lint-flake8
lint-flake8:
	@echo "\n>> ============= Flake8 Linting ============= <<"
	@find app -type f -name \*.py | while read file; do echo "$$file" && $(FLAKE8) --config=flake8.ini "$$file" || exit 1; done


## lint: Lint The Code.
.PHONY: lint
lint: lint-pycodestyle lint-flake8
	@echo "\n>> ============= All linting cases passed! ============= <<"


## test: Run Test Cases.
.PHONY: test
test:
	@echo "\n>> ============= Run Test Cases ============= <<"
	export CALVIN_TEST_RUN=true
	$(PYTHON) manage.py test


## migration: Create DB Migration Files.
.PHONY: migration
migration:
	@echo "\n>> ============= Make Migrations ============= <<"
	$(PYTHON) manage.py makemigrations


## migrate: Migrate Database.
.PHONY: migrate
migrate:
	@echo "\n>> ============= Migrate ============= <<"
	$(PYTHON) manage.py migrate


## run: Run Server.
.PHONY: run
run:
	@echo "\n>> ============= Run Server ============= <<"
	$(GUNICORN) --bind 0.0.0.0:8000 app.wsgi


## coverage: Get test coverage.
.PHONY: coverage
coverage:
	@echo "\n>> ============= Get test coverage ============= <<"
	$(COVERAGE) run --source='app' manage.py test app
	$(COVERAGE) report -m
	$(COVERAGE) html


## create-env: Create .env file.
.PHONY: create-env
create-env:
	@echo "\n>> ============= Create .env file ============= <<"
	cp .env.example .env


## makemessages: Make translation files.
.PHONY: makemessages
makemessages:
	@echo "\n>> ============= Make translation files ============= <<"
	$(PYTHON) manage.py makemessages


## rqstats: Get the worker stats
.PHONY: rqstats
rqstats:
	@echo "\n>> ============= Get Worker Stats ============= <<"
	$(PYTHON) manage.py rqstats --interval=1


## worker: Run the worker
.PHONY: worker
worker:
	@echo "\n>> ============= Run Worker ============= <<"
	$(PYTHON) manage.py rqworker default


## outdated-pkg: Show outdated python packages
.PHONY: outdated-pkg
outdated-pkg:
	@echo "\n>> ============= List Outdated Packages ============= <<"
	$(PIP) list --outdated


## serve_ui: Serve admin dashboard
.PHONY: serve_ui
serve_ui:
	@echo ">> ============= Run Vuejs App ============= <<"
	cd web;$(NPM) run serve


## build_ui: Builds admin dashboard for production
.PHONY: build_ui
build_ui:
	@echo ">> ============= Build Vuejs App ============= <<"
	cd web;$(NPM) run build


## check_ui_format: Check dashboard code format
.PHONY: check_ui_format
check_ui_format:
	@echo ">> ============= Validate js format ============= <<"
	cd web;$(NPX) prettier  --check .


## format_ui: Format dashboard code
.PHONY: format_ui
format_ui:
	@echo ">> ============= Format js Code ============= <<"
	-rm -rf web/dist
	cd web;$(NPX) prettier  --write .


## package: Package assets
.PHONY: package
package:
	@echo ">> ============= Package Assets ============= <<"
	-rm $(shell pwd)/web/.env
	echo "VUE_API_SERVER_URL=" > $(shell pwd)/web/.env.dist
	cd web;$(NPM) run build
	-rm -rf static/*
	cp -R web/dist/* static/
	echo "{% load static %}" > themes/default/templates/index.html
	echo "{% load i18n %}\n\n" >> themes/default/templates/index.html
	cat static/index.html >> themes/default/templates/index.html
	$(PYTHON) manage.py build_ui


## ci: Run all CI tests.
.PHONY: ci
ci: coverage lint outdated-pkg
	@echo "\n>> ============= All quality checks passed ============= <<"


.PHONY: help