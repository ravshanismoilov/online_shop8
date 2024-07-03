from django.forms import ModelForm
from .models import Products


class CreateProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['category', 'name', 'year', 'price', 'description', 'image']
