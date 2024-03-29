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
    address = forms.CharField(max_length=100, required=True, initial='')
    postal_code = forms.CharField(max_length=8, required=True, initial='')
    city = forms.CharField(max_length=100, required=True, initial='')
    nif = forms.CharField(max_length=9, required=False, initial='')
    phone = forms.CharField(max_length=9, required=True, initial='')
    
    class Meta:
        model = Address
        fields = [
            'address',
            'postal_code',
            'city',
            'nif',
            'phone',
            ]