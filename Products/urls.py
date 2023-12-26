from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('',frontpage, name='frontpage'),
    
    path('shop/',shop, name='shop'),
    path('shop/<slug:slug>', product, name='product'),
    
    path('add_product/', add_product, name='add_product'),
    path('edit_product/<slug:slug>/', edit_product, name='edit_product'),
    path('delete_product/<slug:slug>/', delete_product, name='delete_product'),
    
    path('add_category/', add_category, name='add_category'),
    path('edit_category/<slug:slug>/', edit_category, name='edit_category'),
    path('delete_category/<slug:slug>/', delete_category, name='delete_category'),
    
    path('show_products/', show_products, name='show_products'),
    path('show_products/<slug:slug>', show_products, name='show_products'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
