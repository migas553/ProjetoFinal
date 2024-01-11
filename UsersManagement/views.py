from django.shortcuts import render, redirect
from .forms import *
from Orders.models import *
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form=SignUpForm()
    return render(request, 'UsersManagement/signup.html', {'form' : form})

# Frontpage temporaria
def frontpage(request):    
    return render(request, 'UsersManagement/frontpage.html')


@login_required
def my_account(request):
    address = request.user.address.first()
    orders = Order.objects.filter(user=request.user)
    order_products = OrderProducts.objects.filter(order__in=orders)
    
    context = {'address' : address, 'orders' : orders, 'order_products' : order_products}
    return render(request, 'UsersManagement/my_account.html', context)





@login_required
def edit_my_account(request):
    error_message = None
    if request.method =='POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        if User.objects.filter(username=username).exclude(pk=user.pk).exists():
            error_message = "Utilizador já existe."
        else:
            user.username = username
            user.email = request.POST.get('email')
            user.save()
            return redirect('my_account')
        
    return render(request, 'UsersManagement/edit_my_account.html', {'error_message': error_message})



@login_required
def edit_my_address(request):
    if request.method =='POST':
        form = AddressForm(request.POST, instance=request.user.address.first())
            
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('my_account')
        else:
            print(form.errors)
    else:
        form = AddressForm(instance=request.user.address.first())
    return render(request, 'UsersManagement/edit_my_address.html', {'form' : form})