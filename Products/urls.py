from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    path('',frontpage, name='frontpage'),
    path('shop/',shop, name='shop'),
    path('shop/<slug:slug>', product, name='product'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
