from .models import *
from django.forms import ModelForm


class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        
class AddCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        
