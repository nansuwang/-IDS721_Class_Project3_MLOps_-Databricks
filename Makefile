install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test.py

format:
	black app.py

lint:
	pylint --disable=R,C preprocessing.py

all: install lint test
