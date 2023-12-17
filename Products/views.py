from django.shortcuts import render, get_object_or_404
from Products.models import Product, Category

# Create your views here.
def frontpage(request):
    products = Product.objects.all()[:6]
    
    return render(request, 'Products/frontpage.html', {'products': products})

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    active_category = request.GET.get('category', '')
    if active_category:
        products = products.filter(category__slug=active_category)
    
    
    if query := request.GET.get('query', ''):
        products = products.filter(name__icontains=query)
    context = {
        'products': products,
        'categories': categories,
        'active_category': active_category
    }
    
    return render(request, 'Products/shop.html', context)

def product(request, slug):
    product = get_object_or_404(Product,slug=slug)
    return render(request, 'Products/product.html', {'product': product})
