from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.forms import forms
from rest_framework.fields import ListField


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=400)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=400, null=True)
    first_name = models.CharField(max_length=400)
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=400)
    role = models.CharField(max_length=400)
    age = models.IntegerField()
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='+'
    )

    class Meta:
        verbose_name = "Продавец"
        verbose_name_plural = "Продавцы"

    def __str__(self):
        return self.last_name


class Ads(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=400)
    author = models.ForeignKey(
        User,
        related_name='author_name',
        on_delete=models.CASCADE,
        null=True
    )
    price = models.FloatField()
    description = models.CharField(max_length=2000, null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', null=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        verbose_name = "Инфо"
        verbose_name_plural = "Инфо всех"

    def __str__(self):
        return self.name


class Compilation(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(Ads)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return str(self.name)
