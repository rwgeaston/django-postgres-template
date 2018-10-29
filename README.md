Django project for storing entities! with names!

    docker-compose up

First time you run it you need to also do

    docker-compose exec web python app/manage.py makemigrations
    docker-compose exec web python app/manage.py createsuperuser

You need a local_settings.py file in main folder with settings like

    SECRET_KEY = 'testing'
    DEBUG = True
    ALLOWED_HOSTS = ['0.0.0.0']

But these are not appropriate for production. You can also make the google login button work somehow, idk.

API with GET/POST/PUT/DELETE is here

    http://0.0.0.0:8000/api/v1/things/

Django admin is, as usual, found at

    http://0.0.0.0:8000/admin/
