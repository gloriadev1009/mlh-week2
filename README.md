# mlh-holiday-planner

## Installation

Make sure you have python3 and pip installed
Create and activate virtual environment using virtualenv

```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file with the following line included:

```bash
URL=localhost:5000
```

Start psql container using `$ docker-compose up -d`

Start flask development server

```bash
$ export FLASK_ENV=development
$ flask run
```

## To use the '/flightsAPI' endpoint:
- make sure the api key is added in .env 
- call the endpoint with a POST request containing the following data (as key-value/ form data): 
  - origin = origin airport code
  - destination = destination airport code
  - departDate = date of departure
  - returnDate = date of arrival 

EXAMPLE: 
```bash
origin:YYZ
destination:YVR
departDate:2021-09-01
returnDate:2021-12-01
```
*Note: for testing purposes, just use the exact form data above*
