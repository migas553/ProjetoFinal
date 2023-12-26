from django.db import models
from django.contrib.auth.models import User
from Products.models import Product
from UsersManagement.models import Address

class Order(models.Model):
    STATUS_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Enviado', 'Enviado'),
        ('Entregue', 'Entregue'),
        ('Cancelado', 'Cancelado'),
    )
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pendente')
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        
    def __str__(self):
        return str(self.id)
    
class OrderProducts(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    class Meta:
        verbose_name = 'OrderProduct'
        verbose_name_plural = 'OrderProducts'
        
    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartProduct')

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Cart Product'
        verbose_name_plural = 'Cart Products'
        
    def total_price(self):
        return self.product.price * self.quantity