from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Address

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=100,required=True)
    
    class Meta:
        model = User
        fields=[ 
            'username',
            'first_name', 
            'last_name', 
            'email',
            'password1',
            'password2',
            ]
class AddressForm(forms.ModelForm):
    addressLine1 = forms.CharField(max_length=100, required=True)
    addressLine2 = forms.CharField(max_length=100, required=False)
    postal_code = forms.CharField(max_length=8, required=True)
    city = forms.CharField(max_length=100, required=True)
    nif = forms.CharField(max_length=9, required=False)
    phone = forms.CharField(max_length=9, required=True)
    
    class Meta:
        model = Address
        fields = [
            'addressLine1',
            'addressLine2',
            'postal_code',
            'city',
            'nif',
            'phone',
            ]