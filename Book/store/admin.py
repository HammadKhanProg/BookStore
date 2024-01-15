from django.contrib import admin
from store.models import Science

class AdminScience (admin.ModelAdmin):
    list_display=["Title","Content","Author"]

admin.site.register(Science,AdminScience)
# Register your models here.
