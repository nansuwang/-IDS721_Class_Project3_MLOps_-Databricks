install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test.py

format:
	black preprocessing.py

lint:
	pylint --disable=R,C test.py

all: install lint test
