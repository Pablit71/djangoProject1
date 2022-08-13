from django.db import models


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)


class Ads(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=400)
    author = models.CharField(max_length=400)
    price = models.FloatField()
    description = models.CharField(max_length=2000)
    address = models.CharField(max_length=400)
    is_published = models.CharField(max_length=100)

