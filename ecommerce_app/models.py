from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import UserProfile, Business

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    product = models.ManyToManyField(Product)

class WishList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    product = models.ManyToManyField(Product)
