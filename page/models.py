from unicodedata import name
from django.db import models

# Create your models here.

class User(models.Model):
    
    name = models.CharField(verbose_name="name", max_length=100)

    def __str__(self):
        return self.name