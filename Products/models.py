from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(null=False)
    name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    slug = models.SlugField(null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.CharField(max_length=1000, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0)])
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    photo = models.ImageField(upload_to='product_photos/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 