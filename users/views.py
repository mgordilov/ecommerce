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

stripe.api_key = os.getenv('STRIPE_API')

# Create your views here.
@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user, 'orders': request.user.userprofile.order.all()})

def signin(request):
    if request.method == 'POST':
        form = forms.UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next')
                return redirect(next_url or 'profile')
    else:
        form = forms.UserLoginForm()
    return render(request, 'users/login.html', {'form': form})    

def signup(request):
    if request.method == 'POST':
        form = forms.UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = forms.UserCreateForm()
    return render(request, 'users/signup.html', {'form': form})

@login_required
def signout(request):
    logout(request)
    return redirect('home')

@login_required
def business_create(request):
    if request.method == 'POST':
        form = forms.BusinessCreate(request.POST)
        if form.is_valid():
            stripeBusiness = stripe.Account.create(
              type='express',
              business_type=form.cleaned_data.get('type'),
              country="IE",
              email=request.user.email,
              capabilities={
                "card_payments": {"requested": True},
                "transfers": {"requested": True},
              },
            )
            business = form.save(commit=False)
            business.owner = request.user
            business.stripe_id = stripeBusiness['id']
            business.save()

            stripeLink = stripe.AccountLink.create(
              account=stripeBusiness['id'],
              refresh_url="https://stripe.com/",
              return_url="http://localhost:8000/profile",
              type="account_onboarding",
            )
            return redirect(stripeLink['url'])
    else:
        form = forms.BusinessCreate()
    return render(request, 'users/business_create.html', {'form': form})

@login_required
def business_delete(request):
    business = get_object_or_404(models.Business, owner=request.user)
    if request.method == 'POST':
        stripe.Account.delete(business.stripe_id)
        business.delete()
        return redirect('profile')
    return render(request, 'users/business_delete.html', {'business': business})