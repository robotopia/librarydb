# Django implementation of LibraryDB

1. Install dependencies:

- [`django-versionfield`](https://pypi.org/project/django-versionfield/)

The above can be installed with
```
pip install -r requirements.txt
```

2. Create the (SQLite) database:

```
python manage.py makemigrations librarydb
python manage.py migrate
```
or download a pre-existing one that is compatible with the specification version.

3. Create an admin user

```
python manage.py createsuperuser
```
and then follow the prompts for entering a username, email address, and password.
