main_path = src/run_ids_pipeline.py
image_name = ds-nlp-ids-classification-docker
profile = data-scientist

.PHONY: help
.DEFAULT_GOAL := help

venv_path = .venv
venv_bin = $(venv_path)/bin/

#help: @ Lists all available commands
help:
	@grep -E '[a-zA-Z\.\-]+:.*?@ .*$$' $(MAKEFILE_LIST) --no-filename | tr -d '#' | awk 'BEGIN {FS = ":.*?@ "}; \
	{printf "\033[36m%-35s\033[0m %s\n", $$1, $$2}'

#env.setup: @ Installs environment dependencies, creates virtual environment and installs dev python packages
env.setup: e.install-environment-dependencies e.create-virtualenv env.install-python-dependencies
env.setup-ci: e.create-virtualenv-ci env.install-python-dependencies

#env.delete: @ Removes the current evnironment
env.delete:
	rm -rf $(venv_path)

e.install-environment-dependencies:
	-brew install pyenv
	-pyenv install 3.7.9
	-pip3 install virtualenv

e.create-virtualenv:
	python3 -m virtualenv -p ~/.pyenv/versions/3.7.9/bin/python $(venv_path)

e.create-virtualenv-ci:
	python3 -V
	python3 -m virtualenv $(venv_path)

#env.install-python-dependencies: @ Installs development python dependencies
env.install-python-dependencies:
	$(venv_bin)pip install pip-tools
	$(venv_bin)pip install -r requirements-dev.txt

#env.update: @ Updates all python dependencies
env.update: e.update env.install-python-dependencies

e.update:
	$(venv_bin)python -m pip install -U pip-tools
	$(venv_bin)pip install pip --upgrade
	$(venv_bin)pip-compile --verbose -r requirements.in --max-rounds=30
	$(venv_bin)pip-compile --verbose -r requirements-dev.in --max-rounds=30

#test.unit: @ Run all unit tests under src/tests. Example usage: 'make test.unit'
test.unit:
	$(venv_bin)python -m unittest discover ./tests/

#test.lint: @ Test your Python code with Pylint before you merge changes to master/release and deploy your dag. Example usage: 'make test.lint'
test.lint:
	PYTHONPATH=${PYTHONPATH}:src \
	$(venv_bin)pylint src; \
	$(venv_bin)mypy --show-error-codes src; \
	$(venv_bin)flake8 src

#app.run: @ Runs the application
app.run:
	AWS_PROFILE=$(profile) \
	$(venv_bin)python $(main_path) sagemaker_code_path_we_ignore --s3-bucket-name data-science-nlp-dev --run-date-str 20220101_010101

#docker.build: @ Builds a docker image for the application
docker.build:
	docker build -t $(image_name) .

#docker.run: @ To run with docker locally: PROXY_USERNAME=blah PROXY_PASSWORD=blah make run-image
docker.run:
	docker run \
	--env AWS_ACCESS_KEY_ID=`aws configure get $(profile).aws_access_key_id` \
	--env AWS_SECRET_ACCESS_KEY=`aws configure get $(profile).aws_secret_access_key` \
	--env AWS_SESSION_TOKEN=`aws configure get $(profile).aws_session_token` \
	$(image_name) \
	python $(main_path) sagemaker_code_path_we_ignore --s3-bucket-name decision-science-emr
