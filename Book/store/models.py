from django.db import models
from tinymce.models import HTMLField

class Science (models.Model):
    Title=models.CharField(max_length=100)
    Content=HTMLField()
    Author=models.CharField(max_length=100)
# Create your models here.
