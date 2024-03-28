from . import models
from django import forms

class ProductCreateForm (forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'description', 'price', 'gender', 'size', 'category']
        labels = {
            'name': 'Name',
            'description': 'Description',
            'price': 'Price',
            'gender': 'Gender',
            'size': 'Size',
            'category': 'Category'
        }
        help_texts = {
            'size': 'Enter the available sizes separated by commas. For example: S, M, L, XL',
            'price': 'Enter the price in EUR',
        }