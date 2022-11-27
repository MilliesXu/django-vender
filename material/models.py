from django.db import models
from authentification.models import User


# Create your models here.
class Material(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    uom = models.CharField(max_length=50)
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0
    )
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
