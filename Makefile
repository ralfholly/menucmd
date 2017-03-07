

all: pylint test

pylint:
	pylint3 *.py

test:
	python3 -m unittest test_menucmd.py
