from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartProduct, ShippingAddress, Payment, Order, OrderProducts
from Products.models import Product
from UsersManagement.models import Address
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import OrderForm, ShippingAddressForm, PaymentForm
from django.db.models import Count
# Create your views here.
@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_products = CartProduct.objects.filter(cart=cart)
    cart_total = sum([cart_product.product.price * cart_product.quantity for cart_product in cart_products])
    context = {'cart_products': cart_products, 'cart_total': cart_total}
    return render(request, 'Orders/cart.html', context)
@login_required
def checkout(request):
    address_form = ShippingAddressForm(request.POST or None)
    payment_form = PaymentForm(request.POST or None)
    cart = Cart.objects.get(user=request.user)
    cart_products = CartProduct.objects.filter(cart=cart)
    cart_total = sum(
                [cart_product.product.price * cart_product.quantity for cart_product in cart_products]
                )
    address = request.user.address.first() 
    if request.method == 'POST':
      
        if address_form.is_valid() and payment_form.is_valid():
            address = ShippingAddress.objects.create(**address_form.cleaned_data)
            payment = Payment.objects.create(**payment_form.cleaned_data)
            
            cart_products = CartProduct.objects.filter(cart=cart)

            order = Order.objects.create(user=request.user, address=address, payment=payment, total=cart_total)
            for cart_product in cart_products:
                OrderProducts.objects.create(order=order, product=cart_product.product, quantity=cart_product.quantity)
            cart.delete()
            return redirect('my_account')
        else:
            print(address_form.errors)
            print(payment_form.errors)
            context = {
                'cart_products': cart_products, 
                'cart_total': cart_total, 
                'address': address,
                'address_form': address_form,
                'payment_form': payment_form
            }
            return render(request, 'Orders/checkout.html', context) 




    if cart:
               
        context = {
            'cart_products': cart_products, 
            'cart_total': cart_total, 
            'address': address,
        }
        return render(request, 'Orders/checkout.html', context)   
        
@login_required
def add_to_cart(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if the product is already in the cart
    cart_product, created = CartProduct.objects.get_or_create(cart=cart, product=product)
    if not created:
        # If the product is already in the cart, increment the quantity
        cart_product.quantity += 1
        cart_product.save()

    return redirect('cart')

@login_required
def increase_quantity(request, cart_product_id):
    cart_product = get_object_or_404(CartProduct, id=cart_product_id)
    cart_product.quantity += 1
    cart_product.save()
    return redirect('cart')

@login_required
def decrease_quantity(request, cart_product_id):
    cart_product = get_object_or_404(CartProduct, id=cart_product_id)
    if cart_product.quantity > 1:
        cart_product.quantity -= 1
        cart_product.save()
    elif cart_product.quantity == 1:
        cart_product.delete()
    return redirect('cart')

@staff_member_required
def show_orders(request):
    orders = Order.objects.all()
    status = request.GET.get('status', '')
    if status:
        orders = orders.filter(status=status)
    query = request.GET.get('query', '')
    if query:
        orders = orders.filter(name__icontains=query)    
 

    active_status = request.GET.get('status', '')
    

    statuses = Order.objects.values('status').annotate(total=Count('status'))
    
    context = {'orders': orders, 'statuses': statuses, 'status': status, 'active_status': active_status}
    
    return render(request, 'Orders/show_orders.html', context)

@login_required
def order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_products = OrderProducts.objects.filter(order=order)
    context = {'order': order, 'order_products': order_products}
    return render(request, 'Orders/order_details.html', context)

@staff_member_required
def edit_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_products = OrderProducts.objects.filter(order=order)
    order_form = OrderForm(request.POST or None, instance=order)
    if request.method == 'POST':
        if order_form.is_valid():
            order_form.save()
            return redirect('show_orders')
        else:
            print(order_form.errors)
            context = {'order': order, 'order_products': order_products, 'order_form': order_form}
            return render(request, 'Orders/edit_order.html', context)
    context = {'order': order, 'order_products': order_products, 'order_form': order_form}
    return render(request, 'Orders/edit_order.html', context)

@staff_member_required
def edit_shipping_address(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    address = get_object_or_404(ShippingAddress, id=order.address.id)
    address_form = ShippingAddressForm(request.POST or None, instance=address)
    if request.method == 'POST':
        if address_form.is_valid():
            address_form.save()
            return redirect('show_orders')
        else:
            print(address_form.errors)
            context = {'order': order, 'address_form': address_form}
            return render(request, 'Orders/edit_shipping_address.html', context)
    context = {'order': order, 'address_form': address_form}
    return render(request, 'Orders/edit_shipping_address.html', context)