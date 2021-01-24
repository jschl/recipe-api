from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=60)
    ingredients = models.CharField(max_length=300)

    def __str__(self):
        return self.name
