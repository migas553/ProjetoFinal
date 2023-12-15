from django.shortcuts import render
from Products.models import Product
# Create your views here.
def frontpage(request):
    products = Product.objects.all()[0:6]
    
    return render(request, 'Products/frontpage.html', {'products': products})

def shop(request):
    products = Product.objects.all()
    return render(request, 'Products/shop.html', {'products': products})

def productpage(request):
    return render(request, 'Product/product.html')