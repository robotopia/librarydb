# Generated by Django 4.1.3 on 2022-12-18 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("librarydb", "0004_alter_author_options_alter_book_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="room",
            options={"ordering": ("name",)},
        ),
        migrations.AlterModelOptions(
            name="storage",
            options={"ordering": ("name",)},
        ),
        migrations.AlterModelOptions(
            name="version",
            options={"ordering": ("created",)},
        ),
    ]
