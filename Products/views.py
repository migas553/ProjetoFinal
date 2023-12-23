from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import *
from .forms import *    
from django.contrib.admin.views.decorators import staff_member_required  
# Create your views here.
def frontpage(request):
    products = Product.objects.all()[0:6]
    categories = Category.objects.all()
    return render(request, 'Products/frontpage.html', {'products': products,'categories': categories})

def shop(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    active_category = request.GET.get('category', '')
    if active_category:
        products = products.filter(category__slug=active_category)
    
    query = request.GET.get('query', '')
    if query:
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

@staff_member_required
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('frontpage')
    else:
        form = AddProductForm()
    return render(request, 'Products/add_product.html', {'form': form})

@staff_member_required
def edit_product(request, slug):
    product = get_object_or_404(Product,slug=slug)
    categories = Category.objects.all()
    if request.method == 'POST':
        form = AddProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('show_products')
        else:
            print(form.errors)
    else:
        form = AddProductForm(instance=product)
        
    context = {
        'form': form,
        'product': product,
        'categories': categories,
    }
    return render(request, 'Products/edit_product.html', context)

@staff_member_required
def delete_product(request, slug):
    product = get_object_or_404(Product,slug=slug)
    if request.method == 'POST':
        product.delete()
        return redirect('frontpage')
    return render(request, 'Products/delete_product.html', {'product': product})


@staff_member_required
def add_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_products')
        else:
            print(form.errors)  # print form errors to the console
    else:
        form = AddCategoryForm()
    return render(request, 'Products/add_category.html', {'form': form})

@staff_member_required
def edit_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    if request.method == 'POST':
        form = AddCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('show_products')
    else:
        form = AddCategoryForm(instance=category)
    return render(request, 'Products/edit_category.html', {'form': form,'category': category})

@staff_member_required
def delete_category(request, slug):
    category = get_object_or_404(Category,slug=slug)
    if request.method == 'POST':
        category.delete()
        return redirect('show_products')
    return render(request, 'Products/delete_category.html', {'category': category})

@staff_member_required
def show_products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    category = request.GET.get('category', '')
    if category:
        products = products.filter(category__slug=category)
    query = request.GET.get('query', '')
    if query:
        products = products.filter(name__icontains=query)
    
    active_category = request.GET.get('category', '')
    context = {
        'products': products,
        'categories': categories,
        'active_category': active_category
    }
    
    return render(request, 'Products/show_products.html', context)
