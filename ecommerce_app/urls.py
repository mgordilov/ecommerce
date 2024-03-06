from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-checkout-session/<int:pk>/', views.createCheckoutSession, name='create-checkout-session'),
    path('create-product/', views.CreateProductView.as_view(), name='create-product'),
]