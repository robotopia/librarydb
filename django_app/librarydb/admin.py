from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from . import models

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "authors_html", "loaned_to", "loan_date",]
    list_filter = [
        ("storage", admin.RelatedOnlyFieldListFilter),
        "shelf",
    ]
    search_fields = [
        "title",
        "authors__surname",
        "authors__givenname",
    ]

    def authors_html(self, obj):
        authors = "<br>".join([f"{author}" for author in obj.authors.all()])
        return format_html(authors)

class MusicAdmin(admin.ModelAdmin):
    list_display = ["title", "composers_html",]
    list_filter = ["composers", "arrangers",]
    search_fields = ["title", "composers", "arrangers",]

    def composers_html(self, obj):
        composers = "<br>".join([f"{author}" for author in obj.composers.all()])
        return format_html(composers)

admin.site.register(models.Author)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Music, MusicAdmin)
admin.site.register(models.Room)
admin.site.register(models.Storage)
admin.site.register(models.Version)
