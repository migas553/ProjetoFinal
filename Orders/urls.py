from django.urls import path
from .views import *

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    
    path('add_to_cart/<slug:product_slug>/', add_to_cart, name='add_to_cart'),
    path('increase_quantity/<int:cart_product_id>/', increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:cart_product_id>/', decrease_quantity, name='decrease_quantity'),
    
    path('show_orders', show_orders, name='show_orders'),
    path('order_details/<int:order_id>/', order_details, name='order_details'),
    path('edit_order/<int:order_id>/', edit_order, name='edit_order'),
    path('edit_shipping_address/<int:order_id>/', edit_shipping_address, name='edit_shipping_address'),
]

