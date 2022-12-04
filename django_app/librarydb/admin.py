from django.contrib import admin

# Register your models here.
from .models import Author, Room, Storage, Book, Version

admin.site.register(Author)
admin.site.register(Room)
admin.site.register(Storage)
admin.site.register(Book)
admin.site.register(Version)
