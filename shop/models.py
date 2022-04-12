from statistics import mode
from django.db import models
from django.forms import CharField
from matplotlib.pyplot import cla
from sympy import true

# Create your models here.

class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Product(models.Model):

    def __str__(self):
        return self.title

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE) 
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image = models.CharField(max_length=300)


class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=100)
 