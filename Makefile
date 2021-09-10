.PHONY: test pytest

init:
	virtualenv .env && source .env/bin/activate && pip install -r requirements.txt

# Used to run a subset of the tests, e.g. `make pytest PATH=tests/subfolder`
pytest:
	python3 -m pytest $(ARGS)

test:
	python3 -m pytest ./test

lint:
	python3 -m pylint ./**/*.py