from django.urls import path
from .views import *

urlpatterns = [
    path('about/', about, name='about'),
    path('shipping/', shipping, name='shipping'),
    path('payment/', payment, name='payment'),
    path('contact/', contact, name='contact'),
    
]
