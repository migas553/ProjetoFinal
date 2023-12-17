from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path
from .views import *
urlpatterns = [
    path('signup/', SignUp, name='signup' ),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout' ),
    path('login/', LoginView.as_view(template_name='UsersManagement/login.html', next_page = '/my_account/'),name='login'),
    path('my_account/', my_account, name='my_account'),
    path('edit_my_account/', edit_my_account, name='edit_my_account')
    
]
