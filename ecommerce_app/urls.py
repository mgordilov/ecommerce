from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('cart/', views.cart, name='cart'),

    path('about/', views.about, name='about'),

    # Product URLs
    path('products/', views.products, name='products'),
    path('product/<int:pk>/', views.productDetail, name='product_detail'),
    path('product/<int:pk>/delete/', views.productDeleteView.as_view(), name='product_delete'),
    path('cart-checkout/', views.createCartCheckoutSession, name='cart-checkout'),
    path('create-product/', views.productCreate, name='create-product'),
    path('add-to-wishlist/<int:pk>/', views.AddToWishlist, name='add-to-wishlist'),
    path('add-to-cart/<int:pk>/', views.AddToCart, name='add-to-cart'),

    path('webhook', views.webhook, name='webhook'),
]