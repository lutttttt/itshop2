from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    def __str__(self):
        return self.name
class Form(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey('Category',on_delete=models.PROTECT)
    seller=models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Seller(models.Model):
    rate=models.FloatField()
# Create your models here.
