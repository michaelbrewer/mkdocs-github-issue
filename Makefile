dev:
	pip install -U pip pipenv
	pipenv install

serve:
	pipenv run mkdocs serve

clean:
	pipenv --rm