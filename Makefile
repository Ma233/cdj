env:
	virtualenv venv

dev:
	./venv/bin/python setup.py develop

test:
	./venv/bin/python setup.py test
