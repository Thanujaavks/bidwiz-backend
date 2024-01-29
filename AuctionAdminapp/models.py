from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 255)
    category = models.CharField(max_length = 255)
    startprice = models.FloatField()
    currentprice = models.FloatField()
    end_date = models.DateField(max_length = 10)
    description = models.TextField()

class User(models.Model):
     name = models.CharField(max_length=256, null = True)
     birth_date = models.DateField(max_length=30, null=True)
     username = models.CharField(max_length=256)
     email = models.EmailField(max_length=200, unique = True)

