from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=200)
    INDIVIDUAL = 'individual'
    COMPANY = 'company'
    NON_PROFIT = 'non_profit'
    BUSINESS_TYPE_CHOICES = [
        (INDIVIDUAL, 'Individual'),
        (COMPANY, 'Company'),
        (NON_PROFIT, 'Non-Profit'),
    ]
    type = models.CharField(max_length=200, choices=BUSINESS_TYPE_CHOICES, default=INDIVIDUAL)
    description = models.TextField()
    image = models.ImageField(upload_to='businesses/', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, blank=True, null=True)
    stripe_id = models.CharField(max_length=50, blank=True, null=True)