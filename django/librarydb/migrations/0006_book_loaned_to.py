# Generated by Django 4.1.3 on 2023-02-11 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("librarydb", "0005_alter_room_options_alter_storage_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="loaned_to",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
