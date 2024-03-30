from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profileEdit, name='profileEdit'),
    path('profile/wishlist/', views.profileWishlist, name='profileWishlist'),
    path('profile/orders/', views.profileOrders, name='profileOrders'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),

    path('customer-portal/', views.customerPortal, name='customerPortal'),

    path('business-create/', views.business_create, name='business-create'),
    path('business-delete/', views.business_delete, name='business-delete'),
    path('business/', views.businessProfile, name='businessProfile'),
]