from django.db import models

from authentification.models import User
from material.models import Material


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)


class ProductLine(models.Model):
    material = models.ForeignKey(
            Material,
            null=True,
            on_delete=models.SET_NULL
        )
    quantity = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
