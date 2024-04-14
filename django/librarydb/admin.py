from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from . import models

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "authors_html", "storage", "shelf", "loaned_to", "loan_date",]
    list_filter = [
        ("storage", admin.RelatedOnlyFieldListFilter),
        "shelf",
    ]
    search_fields = [
        "title",
        "authors__surname",
        "authors__givenname",
    ]
    filter_horizontal = ["authors"]

    def authors_html(self, obj):
        authors = "<br>".join([f"{author}" for author in obj.authors.all()])
        return format_html(authors)

@admin.register(models.Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ["title", "composers_html",]
    list_filter = [
        ("composers", admin.RelatedOnlyFieldListFilter),
        ("arrangers", admin.RelatedOnlyFieldListFilter),
    ]
    search_fields = [
        "title",
        "composers__surname",
        "composers__givenname",
        "arrangers__surname",
        "arrangers__givenname",
    ]

    def composers_html(self, obj):
        composers = "<br>".join([f"{author}" for author in obj.composers.all()])
        return format_html(composers)

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ["surname", "givenname", "books"]
    search_fields = ["surname", "givenname"]
    filter_horizontal = ["books"]

admin.site.register(models.Room)
admin.site.register(models.Storage)
admin.site.register(models.Version)