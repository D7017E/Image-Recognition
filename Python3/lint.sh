# Run lint on src and check that style is up to standard.
pipenv install --dev
pipenv run pylint ./src
