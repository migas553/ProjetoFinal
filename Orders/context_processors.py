# context_processors.py
from .models import Cart, CartProduct

def cart_count(request):
    cart_count = 0
    total_price = 0
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart = Cart.objects.get(user=request.user)
        cart_products = CartProduct.objects.filter(cart=cart)
        cart_count = sum(product.quantity for product in cart_products)
    else:
        cart_count = None
    return {'cart_count': cart_count}