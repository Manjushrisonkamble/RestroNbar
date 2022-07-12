from django.db import models

# Create your models here.

class RestronBar(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    price = models.IntegerField()
    add = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    
