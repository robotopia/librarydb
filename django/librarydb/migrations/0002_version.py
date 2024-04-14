# Generated by Django 4.1.3 on 2022-12-04 08:17

from django.db import migrations, models
import versionfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("librarydb", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", versionfield.fields.VersionField()),
                (
                    "min_version",
                    versionfield.fields.VersionField(blank=True, null=True),
                ),
                (
                    "max_version",
                    versionfield.fields.VersionField(blank=True, null=True),
                ),
            ],
        ),
    ]