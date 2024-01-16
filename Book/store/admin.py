from django.contrib import admin
from store.models import Book
from store.models import Category


class AdminScience (admin.ModelAdmin):
    list_display=["Title","Content","Author"]

class AdminCategory (admin.ModelAdmin):
    list_display=["name"]


admin.site.register(Book,AdminScience)
admin.site.register(Category,AdminCategory)
# Register your models here.
