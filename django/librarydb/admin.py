from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from . import models

class MusicInline(admin.TabularInline):
    model = models.Music
    extra = 1
    filter_horizontal = ["composers", "arrangers"]

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "authors_html", "storage", "shelf", "loaned_to", "loan_date",]
    list_filter = [
        ("storage", admin.RelatedOnlyFieldListFilter),
        "shelf",
        "owner",
    ]
    search_fields = [
        "title",
        "authors__surname",
        "authors__givenname",
    ]
    filter_horizontal = ["authors", "languages"]
    inlines = [MusicInline]

    def authors_html(self, obj):
        authors = "<br>".join([f"{author}" for author in obj.authors.all()])
        return format_html(authors)

@admin.register(models.Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ["title", "composers_html",]
    list_filter = [
        ("composers", admin.RelatedOnlyFieldListFilter),
        ("arrangers", admin.RelatedOnlyFieldListFilter),
        ("book_or_folder", admin.RelatedOnlyFieldListFilter),
    ]
    search_fields = [
        "title",
        "composers__surname",
        "composers__givenname",
        "arrangers__surname",
        "arrangers__givenname",
    ]
    filter_horizontal = ["composers", "arrangers"]
    autocomplete_fields = ["book_or_folder"]

    def composers_html(self, obj):
        composers = "<br>".join([f"{author}" for author in obj.composers.all()])
        return format_html(composers)

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ["surname", "givenname"]
    filter_horizontal = ["books", "composed_music"]
    #fields = ["givenname", "surname", "books"]

@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    filter_horizontal = ["books"]

admin.site.register(models.Room)
admin.site.register(models.Storage)
admin.site.register(models.Version)
