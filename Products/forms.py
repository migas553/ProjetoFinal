from .models import *
from django.forms import ModelForm


class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','slug','category','description','price','stock','photo']

        
class AddCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name','slug']

        
