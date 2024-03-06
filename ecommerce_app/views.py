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

import os

import stripe

stripe.api_key = ''

# Create your views here.
def home(request):
    products = models.Product.objects.all()
    return render(request, 'ecommerce_app/home.html', {'products': products})

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