from django.db import models
from versionfield import VersionField

class Version(models.Model):
    created = VersionField()
    min_version = VersionField(null=True, blank=True)
    max_version = VersionField(null=True, blank=True)

    class Meta:
        ordering = ("created",)

class Author(models.Model):
    surname = models.CharField(max_length=200)
    givenname = models.CharField(verbose_name="Given names", max_length=200, null=True, blank=True)

    def __str__(self):
        if self.givenname is not None:
            return f"{self.surname}, {self.givenname}"
        else:
            return self.surname

    class Meta:
        ordering = ("surname", "givenname",)

class Room(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)

class Storage(models.Model):
    name = models.CharField(max_length=200)
    room = models.ForeignKey(Room, null=True, blank=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)

class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField("ISBN", max_length=64, null=True, blank=True)
    storage = models.ForeignKey(Storage, null=True, blank=True, on_delete=models.SET_NULL)
    shelf = models.IntegerField(null=True, blank=True)
    authors = models.ManyToManyField(Author, blank=True)
    loaned_to = models.CharField(max_length=200, blank=True, null=True)
    loan_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("title", "storage", "shelf",)

class Music(models.Model):
    title = models.CharField(max_length=200)
    book_or_folder = models.ForeignKey(Book, on_delete=models.CASCADE)
    composers = models.ManyToManyField(Author, blank=True, related_name="composed_music")
    arrangers = models.ManyToManyField(Author, blank=True, related_name="arranged_music")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Music"
        ordering = ("title",)
