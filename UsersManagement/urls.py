from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path
from .views import *
urlpatterns = [
    path('',frontpage, name='frontpage'),
    path('signup/', SignUp, name='signup' ),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout' ),
    path('login/', LoginView.as_view(template_name='UsersManagement/login.html',next_page='/'), name='login' ),
    
]
