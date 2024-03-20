from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),

    # Product URLs
    path('create-checkout-session/<int:pk>/', views.createCheckoutSession, name='create-checkout-session'),
    path('cart-checkout/', views.createCartCheckoutSession, name='cart-checkout'),
    path('create-product/', views.CreateProductView.as_view(), name='create-product'),
    path('add-to-wishlist/<int:pk>/', views.AddToWishlist, name='add-to-wishlist'),
    path('add-to-cart/<int:pk>/', views.AddToCart, name='add-to-cart'),
]