from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, OrderProducts, Cart, CartProduct
from Products.models import Product
from UsersManagement.models import Address
from django.contrib.auth.decorators import login_required


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
    address = request.user.address.first()
    cart = Cart.objects.get(user=request.user)
    if cart:
        cart_products = CartProduct.objects.filter(cart=cart)
        cart_total = sum([cart_product.product.price * cart_product.quantity for cart_product in cart_products])
        context = {'cart_products': cart_products, 'cart_total': cart_total, 'address': address}
        return render(request, 'Orders/checkout.html', context)
    
    if request.method == 'POST':
        address = Address.objects.get(id=request.POST['address'])
        order = Order.objects.create(user=request.user, address=address)
        cart_products = CartProduct.objects.filter(cart=cart)
        for cart_product in cart_products:
            OrderProducts.objects.create(order=order, product=cart_product.product, quantity=cart_product.quantity)
        cart.delete()
        return redirect('orders')

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