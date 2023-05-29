# Python Docker Template
A template for creating dockerised python applications. The project deploys your docker image to AWS ECR via CICD.

## Repository Setup
1. Create a new repository
2. Clone this repository and copy the contents to the newly created repository (make sure the hidden 
files are copied)
3. Go to `.circleci/config.yml` and change the team name to your team name
4. Commit and push to master (just this once)
5. Login to [circleci](https://circleci.com/dashboard) using your domain git credentials
6. Go to add project and add your project, click start building
7. Ask `roman.kovalik` for the service account credentials (this service account can only write to ECR)
8. Got to `project settings -> environment variables` and add the following
    1. AWS_ACCESS_KEY_ID: a value received from Roman
    2. AWS_SECRET_ACCESS_KEY: a value received from Roman
9. Congratulations the CI/CD is setup!

## Getting started
The repository uses `Pyenv` to manage the virtual env and `pip-compile` for dependency pinning.

The following steps assume you have setup your AWS CLI with the guide found [here](https://domain.atlassian.net/wiki/spaces/DO/pages/481230937/How+to+use+Okta+to+login+to+AWS+console+and+AWS+CLI+on+Windows+and+MacOSx)

1. In the Makefile change the `profile` parameter to the AWS CLI profile you want to use
2. `make env.setup` to install pyenv, Python, Python dependencies and create a virtual env
4. `make test.lint` to lint test your code
5. `make test.unit` to run your tests
5. `make app.run` to run the program, locally
5. `make docker.build` to build the docker image
5. `make docker.run` to run the docker iamge, locally

To update the dependencies:
1. Add the dependencies you need to `requirements.in`, add any development dependencies to `requirements-dev.in`
2. `make env.update` will produce a new pinned requirements.txt

## Git Workflow

#### Development
1. Create a feature branch, commit and push
2. Each time you push CircleCI will build the docker image and publish it to 
[ECR](https://ap-southeast-2.console.aws.amazon.com/ecr/repositories?region=ap-southeast-2) with the name `<repository_name>-<your_name>-dev`

#### Staging
1. Create a pull request from your feature branch into master
2. Once the request is merged CircleCi will build the docker image and publish it to [ECR](https://ap-southeast-2.console.aws.amazon.com/ecr/repositories?region=ap-southeast-2) with the name `<repository_name>-stg`

#### Production
1. Create a git tag and push
2. Once you push the tag CircleCi will build the docker image and publish it to [ECR](https://ap-southeast-2.console.aws.amazon.com/ecr/repositories?region=ap-southeast-2) with the name `<repository_name>-prd`

## Scheduling with Airflow
There are two options for scheduling this job on Airflow:
1. Sagemaker Operator
    There is an example dag that uses the Sagemaker processing operator found [here](https://github.com/domain-group/mlp-airflow-aws/blob/master/dags/machine_learning_platform/mlp_sagemaker_example/dag.py)
2. EC2-Docker Operator
    Compared to Sagemaker, this operator uses EC2 spot instance and reduces the cost by up to 90%. However it requires your application to be fault-tolerant/stateless
    Example found [here](https://github.com/domain-group/mlp-airflow-aws/tree/master/dags/machine_learning_platform/mlp_ec2_docker_example)
# newdev-classification-docker
