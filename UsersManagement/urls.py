
from django.urls import path
from .views import *
urlpatterns = [
    path('',frontpage, name='frontpage'),
    path('signup/', SignUp, name='signup' ),
    
]
