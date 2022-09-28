# Backend

## Setup local environment

### Setup venv and install dependencies

```sh
python -m venv venv
(venv) pip install -r requirements.txt
```

### Setup database

```sh
docker-compose up -d
```

### Run migrations

```
python manage.py migrate
```
### Run local server

```sh
python manage.py runserver
```

## Override database configuration

The database can be configured by these 5 variables
 - `DATABASE_HOST`
 - `DATABASE_NAME`
 - `DATABASE_PORT`
 - `DATABASE_USER`
 - `DATABASE_PASSWORD`


