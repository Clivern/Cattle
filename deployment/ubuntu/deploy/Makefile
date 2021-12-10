PYTHON ?= python


help: Makefile
	@echo
	@echo " Choose a command run in Cattle:"
	@echo
	@sed -n 's/^##//p' $< | column -t -s ':' |  sed -e 's/^/ /'
	@echo


## config: Install dependencies.
config:
	$(PYTHON) -m pip install ansible
	$(PYTHON) -m pip install ansible-lint


## lint: Lint ansible files.
lint:
	ansible-lint -v


## configure: Configure the server.
configure:
	@echo "\n>> ============= Ship Mgt Server ============= <<"
	ansible-playbook playbook.yml


.PHONY: help configure lint config
