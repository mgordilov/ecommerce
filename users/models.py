from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    stripe_id = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.SET_NULL, blank=True, null=True)
    wishlist = models.ManyToManyField('ecommerce_app.Product', blank=True, related_name='wishlist')
    cart = models.ManyToManyField('ecommerce_app.Product', blank=True, related_name='cart')
    order = models.ManyToManyField('ecommerce_app.Order', blank=True, related_name='orders')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=Business)
def create_business(sender, instance, created, **kwargs):
    if created:
        user = instance.owner
        if UserProfile.objects.filter(user=user).exists():
            user_profile = UserProfile.objects.get(user=user)
            user_profile.business = instance
            user_profile.save()