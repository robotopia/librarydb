from django.db import models
from versionfield import VersionField

class Version(models.Model):
    created = VersionField()
    min_version = VersionField(null=True, blank=True)
    max_version = VersionField(null=True, blank=True)

class Author(models.Model):
    surname = models.CharField(max_length=200)
    givenname = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.givenname is not None:
            return f"{self.surname}, {self.givenname}"
        else:
            return self.surname

class Room(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return name

class Storage(models.Model):
    name = models.CharField(max_length=200)
    room = models.ForeignKey(Room, null=True, blank=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.BigIntegerField(null=True, blank=True)
    storage = models.ForeignKey(Storage, null=True, blank=True, on_delete=models.SET_NULL)
    shelf = models.IntegerField(null=True, blank=True)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

