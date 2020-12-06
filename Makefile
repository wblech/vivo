PROJECT = vivo

default: help

help:  ## Show this help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean: ## Remove byte-compiled, package distribution and test coverage related files
	@find . -iname '*.py[co]' -delete
	@find . -iname '__pycache__' -delete
	@find . -iname '.coverage' -delete
	@rm -rf htmlcov/
	@rm -rf dist/
	@rm -rf build/
	@rm -rf *.egg-info

ex02: ## Run server
	python vivo/ex02/app.py

test: ## Run tests
	pytest -vv tests

test-cov: ## Run tests and create coverage report in HTML
	pytest -x --cov=$(PROJECT) --cov-branch --cov-report=term-missing --cov-report=html:htmlcov

.PHONY:	default help clean ex02 test test-cov
