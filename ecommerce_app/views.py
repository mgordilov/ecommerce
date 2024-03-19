from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import models
from . import forms
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

import os

import stripe

stripe.api_key = 'sk_test_51MlaPJBH5qedVa5Iv3CRtZ6WCDvNSQqq6F2Qh4iD6lcHOWTzZEZktq8sRjlf24qg0LPM9kUbWq1qEceUIUg4Oxu500aPbmkO2Y'

# Create your views here.


def createCheckoutSession(request, pk):
    name = get_object_or_404(models.Product, pk=pk).name
    price = get_object_or_404(models.Product, pk=pk).price * 100
    if request.method == 'POST':
        checkout_session = stripe.checkout.Session.create(
            line_items = [
                {
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {
                            'name': name,
                        },
                        'unit_amount': int(price),
                    },
                    'quantity': 1,
                },
            ],
            mode = 'payment',
            success_url = 'http://example.com',
            cancel_url = 'http://localhost:8000/',
        )
        return redirect(checkout_session.url, code=303)

    else:
        return render(request, 'ecommerce_app/home.html')

class CreateProductView(LoginRequiredMixin, CreateView):
    model = models.Product
    form_class = forms.ProductCreateForm
    template_name = 'ecommerce_app/create_product.html'

def AddToWishlist(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    if product in request.user.userprofile.wishlist.all():
        request.user.userprofile.wishlist.remove(product)
        messages.info(request, 'Product removed from your wishlist')
    else:
        request.user.userprofile.wishlist.add(product)
        messages.info(request, 'Product added to your wishlist')
    return redirect('home')

def home(request):
    products = models.Product.objects.all()
    return render(request, 'ecommerce_app/home.html', {'products': products})