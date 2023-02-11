from django.contrib import admin

# Register your models here.
from . import models

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "loaned_to", "loan_date",]
    list_filter = [
        ("authors", admin.RelatedOnlyFieldListFilter),
    ]
    search_fields = [
        "title",
    ]

admin.site.register(models.Author)
admin.site.register(models.Room)
admin.site.register(models.Storage)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Version)
