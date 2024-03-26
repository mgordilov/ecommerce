from . import models
from django import forms

class ProductCreateForm (forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'description', 'price', 'gender', 'size']