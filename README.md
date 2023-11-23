# Oxit API
Backend API's

## Clone the project
Clone the project from Github:


## Virtual Environment Setup For Local
Create Virtualenv Folder

    virtualenv --python=python3.8 Project_dir/.venv


## Activate Environment:

    source project_venv/bin/activate


## Install dependencies:

    pipenv install

## Project Run On Local:

    chalice local

## Deploy On API Gateway :

    chalice deploy

## Run Test Cases
    
    pytest tests/test_app/machine_tests.py 
    pytest tests/test_app/nozzle_tests.py 