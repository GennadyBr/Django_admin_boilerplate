# Django PostgresSQL admin boilerplate

* This is boilerplate for Django Admin & PostgresSQL

## Installation && Run
### Git clone
https://github.com/GennadyBr/Django_admin_boilerplate.git


### Create config/.env file from config/.env.example
```
cd config
cp .env.example .env
```


### Run app
```
docker compose up -d
python manage.py runserver
```


## Features
- Django admin with translation;
- Django Debug Tool Bar;
- PostgresSQL in docker