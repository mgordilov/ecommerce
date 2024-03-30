from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import UserProfile, Business

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    shortened_description = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    WOMEN = 'women'
    MEN = 'men'
    KIDS = 'kids'
    GENDER_TYPE_CHOICES = [
        (WOMEN, 'Women'),
        (MEN, 'Men'),
        (KIDS, 'Kids'),
    ]
    gender = models.CharField(max_length=200, choices=GENDER_TYPE_CHOICES, default=WOMEN)
    size = models.CharField(max_length=30, blank=True)
    SHOES = 'shoes'
    TSHIRTS = 'tshirts'
    PANTS = 'pants'
    ACCESSORIES = 'accessories'
    CATEGORY_CHOICES = [
        (SHOES, 'Shoes'),
        (TSHIRTS, 'T-Shirts'),
        (PANTS, 'Pants'),
        (ACCESSORIES, 'Accessories'),
    ]
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default=TSHIRTS)
    image = models.CharField(max_length=500, blank=True, null=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    quantity = models.PositiveIntegerField(default=1)
    seller = models.ForeignKey(Business, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=200, null=True)
    is_cancelled = models.BooleanField(default=False)