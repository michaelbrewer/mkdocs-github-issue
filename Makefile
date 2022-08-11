dev:
	pip install -U pip pipenv
	pipenv install

serve:
	pipenv run mkdocs serve

pygments:
	pipenv run python src/pygments_example.py

superfences:
	pipenv run python src/superfences_example.py

clean:
	pipenv --rm