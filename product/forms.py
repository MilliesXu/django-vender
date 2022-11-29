from django.forms import ModelForm

from .models import Product, ProductLine


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description']


class ProductLineForm(ModelForm):
    class Meta:
        model = ProductLine
        fields = ['material', 'quantity', 'product']
