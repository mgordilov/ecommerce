from . import models
from django import forms

class ProductCreateForm (forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'shortened_description', 'description', 'price', 'gender', 'size', 'category', 'image']
        labels = {
            'name': 'Name',
            'shortened_description': 'Shortened Description',
            'description': 'Description',
            'price': 'Price',
            'gender': 'Gender',
            'size': 'Size',
            'category': 'Category',
            'image': 'Image hosted link',
        }
        help_texts = {
            'size': 'Enter the available sizes separated by commas. For example: S, M, L, XL',
            'price': 'Enter the price in EUR',
            'shortened_description': 'It will be used on the product card',
            'image': 'Enter the link to the hosted image',
        }

class ProductUpdateForm (forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['name', 'shortened_description', 'description', 'price', 'gender', 'size', 'category', 'image']
        labels = {
            'name': 'Name',
            'shortened_description': 'Shortened Description',
            'description': 'Description',
            'price': 'Price',
            'gender': 'Gender',
            'size': 'Size',
            'category': 'Category',
            'image': 'Image hosted link',
        }
        help_texts = {
            'size': 'Enter the available sizes separated by commas. For example: S, M, L, XL',
            'price': 'Enter the price in EUR',
            'shortened_description': 'It will be used on the product card',
            'image': 'Enter the link to the hosted image',
        }