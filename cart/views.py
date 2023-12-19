from django.shortcuts import render
from.cart import Cart
from django.contrib.auth.decorators import login_required
from Products.models import Product
# Create your views here.


def add_to_cart(request,product_id):
    cart =Cart(request)
    cart.add(product_id)    
    cart.save()
    return render(request, 'cart/cart_menu.html')
def update_cart(request,product_id, action):
    cart = Cart(request)
    
    if action =='plus':
        cart.add(product_id,1,True)
    else:
        cart.add(product_id,-1,True)
        
    product= Product.objects.get(pk=product_id)
    quantity= cart.get_item(product_id)['quantity']
    
    item = {
        'product': {
            'id': product.id,
            'slug': product.slug,
            'name': product.name,
            'photo': product.photo,
            'price': product.price,       
             },
        'total_price': (quantity * product.price),
        'quantity': quantity,
    }
    response = render(request, 'cart/partials/cart_items.html', {'item': item})
    response['HX-Trigger'] = 'update-menu-cart'
    return response
def hx_menu_cart(request):
    return render(request, 'cart/cart_menu.html')

def cart(request):
    return render(request, 'cart/cart.html')

@login_required
def checkout(request):
    return render(request, 'cart/checkout.html')