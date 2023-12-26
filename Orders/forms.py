from django.forms import ModelForm
from .models import Order, ShippingAddress, Payment

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'payment']
class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['first_name', 'last_name', 'address', 'postal_code', 'city', 'nif', 'phone']

class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = ['card_number', 'card_holder', 'expiration_month', 'expiration_year', 'cvv']