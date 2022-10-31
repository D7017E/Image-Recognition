# Run lint in both cmd and app and warn about 
# lint issues that are not up to standard.
pipenv install --dev
pipenv run pylint ./cmd/
pipenv run pylint ./app/
