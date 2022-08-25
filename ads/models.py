from django.db import models


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=400)
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=400, null=True)
    first_name = models.CharField(max_length=400)
    password = models.CharField(max_length=400)
    role = models.CharField(max_length=400)
    age = models.IntegerField()
    location_id = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Продавец"
        verbose_name_plural = "Продавцы"

    def __str__(self):
        return self.last_name


class Ads(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=400)
    author_id = models.ManyToManyField(User)
    price = models.FloatField()
    description = models.CharField(max_length=2000, null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', null=True)
    category_id = models.ManyToManyField(Category)

    class Meta:
        verbose_name = "Инфо"
        verbose_name_plural = "Инфо всех"

    def __str__(self):
        return self.name
