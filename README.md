# flask-rest-simple

Simple REST App with Flask and Mysql

## Installation

### Create your virtual environment

```
python -m venv venv
```

### Enter your virtual environment

```
source venv/bin/activate
```

### How to Deactivate the Virtual Environment:

```
deactivate
```

### Check Virtual Environment: 

```
pip list
```

### Freeze Library

```
pip freeze > requirements.txt
```

### Install Library

```
pip install -r requirements.txt
```

## Run

## Run with uwsgi

```
uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:application

uwsgi --http 0.0.0.0:8000 --master -p 4 -w wsgi:application
```