WORKDIR := $(shell pwd)

PORT?=8000


help: ## Display help message
	@echo "Please use \`make <target>' where <target> is one of"
	@perl -nle'print $& if m{^[\.a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

run_dev_web: ## Run project in dev mode with autoreload
	uvicorn app:app --port $(PORT) --reload

run_nbu_fetch: ## Fetch data from the NBU and store it to the project DB
	python3 $(WORKDIR)/script_nbu_stat_servise.py