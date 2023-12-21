from django.shortcuts import render
from.cart import Cart
from django.contrib.auth.decorators import login_required
from Products.models import Product
from django.http import HttpResponse


def add_to_cart(request,product_id):
    cart =Cart(request)
    cart.add(product_id)    
    cart.save()
    return render(request, 'cart/cart_menu.html')


def cart(request):
    return render(request, 'cart/cart.html')

@login_required
def checkout(request):
    return render(request, 'cart/checkout.html')

def cart(request):
    return render(request, 'cart/cart.html')

def update_cart(request, product_id, action):
    cart = Cart(request)
    
    if action == 'increment':
        cart.add(product_id, 1, True)
    else:
        cart.add(product_id, -1, True)
    
    product = Product.objects.get(pk=product_id)
    item = cart.get_item(product_id)
    if item is None:
        # handle the case when the item is not in the cart
        return HttpResponse('Item not found in cart', status=404)

    quantity = item['quantity']

    item = {
        'product': {
            'id': product.id,
            'name': product.name,
            'image': product.image,
            'get_thumbnail': product.get_thumbnail(),
            'price': product.price,
        },
        'total_price': (quantity * product.price),
        'quantity': quantity,
    }

    response = render(request, 'cart/partials/cart_item.html', {'item': item})
    response['HX-Trigger'] = 'update-menu-cart'

    return response


def hx_cart_total(request):
    return render(request, 'cart/partials/cart_total.html')
def hx_menu_cart(request):
    return render(request, 'cart/cart_menu.html')
