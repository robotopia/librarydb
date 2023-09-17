# Generated by Django 4.1.3 on 2022-12-18 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("librarydb", "0003_alter_book_authors_alter_book_isbn"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="author",
            options={"ordering": ("surname", "givenname")},
        ),
        migrations.AlterModelOptions(
            name="book",
            options={"ordering": ("title", "storage", "shelf")},
        ),
    ]