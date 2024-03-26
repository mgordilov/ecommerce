from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . import models
from . import forms
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.contrib import messages

import os
import json

import stripe

stripe.api_key = os.getenv('STRIPE_API')

endpoint_secret = os.getenv('STRIPE_WEBHOOK_SECRET')

# Create your views here.


# Stripe related functions
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
            metadata = {'user_id': request.user.id, 'product_id': pk},
            success_url = 'http://localhost:8000/',
            cancel_url = 'http://localhost:8000/cart/',
        )
        return redirect(checkout_session.url, code=303)

    else:
        return render(request, 'ecommerce_app/home.html')

def createCartCheckoutSession(request):
    if request.method == 'POST':
        line_items = []
        metadata = {'user_id': request.user.id}
        n = 1
        for product in request.user.userprofile.cart.all():
            line_items.append({
                'price_data': {
                    'currency': 'eur',
                    'product_data': {
                        'name': product.name,
                    },
                    'unit_amount': int(product.price * 100),
                },
                'quantity': 1,
            }),
            metadata.update({f'product_id{n}': product.id})
            n += 1
            
        checkout_session = stripe.checkout.Session.create(
            line_items = line_items,
            mode = 'payment',
            metadata = metadata,
            success_url = 'http://localhost:8000/profile/',
            cancel_url = 'http://localhost:8000/cart/',
        )
        return redirect(checkout_session.url, code=303)
    
    else:
        return render(request, 'ecommerce_app/cart.html')

@csrf_exempt
def webhook(request):
    event = None
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event.type == 'checkout.session.completed':
        print("Payment was successful.")
        metadata = event['data']['object']['metadata']
        user_id = metadata['user_id']

        if user_id:
            user_profile = models.UserProfile.objects.get(user_id=user_id)
            cart = user_profile.cart.all()
            if cart:
                order = models.Order.objects.create(
                    user=user_profile.user,
                    seller=user_profile.business
                )
                order.product.add(*cart)
                order.save()

                user_profile.order.add(order)
                user_profile.cart.clear()
            else:
                pass
    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)

#  Product related functions
def AddToWishlist(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    if product in request.user.userprofile.wishlist.all():
        request.user.userprofile.wishlist.remove(product)
        messages.info(request, f'Product removed from your wishlist. {request.user.is_authenticated}')
    else:
        request.user.userprofile.wishlist.add(product)
        messages.info(request, 'Product added to your wishlist')
    return redirect('home')

def AddToCart(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    if product in request.user.userprofile.cart.all():
        request.user.userprofile.cart.remove(product)
        messages.info(request, 'Product removed from your cart')
    else:
        request.user.userprofile.cart.add(product)
        messages.info(request, 'Product added to your cart')
    return redirect('home')

def productCreate(request):
    if request.method == 'POST':
        form = forms.ProductCreateForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.business = request.user.userprofile.business
            product.save()
            return redirect('home')
    else:
        form = forms.ProductCreateForm()
    return render(request, 'ecommerce_app/create_product.html', {'form': form})

def productDetail(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    return render(request, 'ecommerce_app/item_page.html', {'product': product})

def products(request):
    products = models.Product.objects.all()
    gender_filter = request.GET.get('gender')
    if gender_filter:
        products = products.filter(gender=gender_filter)
    else:
        products = products
    return render(request, 'ecommerce_app/products.html', {'products': products})

def home(request):
    return render(request, 'ecommerce_app/home.html')

def cart(request):
    return render(request, 'ecommerce_app/cart.html')