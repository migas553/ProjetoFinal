from django.urls import path
from .views import *
    
    
    
urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),   
    path('cart/', cart, name='cart'),   
    path('checkout/', checkout, name='checkout'),
    path('hx_menu_cart/', hx_menu_cart, name= 'hx-menu-cart'),
    path('update_cart/<int:product_id>/<str:action>/',update_cart, name='update_cart'),
    path('hx_menu_cart/', hx_menu_cart, name='hx_menu_cart'),
]

    
