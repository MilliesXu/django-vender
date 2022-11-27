from django.forms import ModelForm

from .models import Material


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'description', 'uom', 'unit_price']
