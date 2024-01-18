from django.db import models
from tinymce.models import HTMLField
from .category import Category

class Book (models.Model):
    Title=models.CharField(max_length=100)
    Content=models.TextField()
    image=models.ImageField(upload_to="uploads/books",default=1)
    Author=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)