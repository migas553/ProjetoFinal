from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, OrderProducts, Cart, CartProduct
from Products.models import Product
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_products = CartProduct.objects.filter(cart=cart)
    cart_total = sum([cart_product.product.price * cart_product.quantity for cart_product in cart_products])
    context = {'cart_products': cart_products, 'cart_total': cart_total}
    return render(request, 'Orders/cart.html', context)

def checkout(request):
    return render(request, 'Orders/checkout.html')

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