# Django implementation of LibraryDB

## Install dependencies:

- [`django`](https://pypi.org/project/django/)
- [`django-versionfield`](https://pypi.org/project/django-versionfield/)

The above can be installed with
```
pip install -r requirements.txt
```

## Create the (SQLite3) database:

```
python manage.py makemigrations librarydb
python manage.py migrate
```
**OR**

Download a pre-existing SQLITE database that is compatible with the specification version, and place it in this directory with the name `librarydb.sqlite3`.

## Create an admin user

```
python manage.py createsuperuser
```
Follow the prompts for entering a username, email address, and password.

## Run the server locally

```
python manage.py runserver
```

The admin site can then be accessed at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
