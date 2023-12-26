from django.urls import path
from .views import *

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('add_to_cart/<slug:product_slug>/', add_to_cart, name='add_to_cart'),
    path('increase_quantity/<int:cart_product_id>/', increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:cart_product_id>/', decrease_quantity, name='decrease_quantity'),
]

