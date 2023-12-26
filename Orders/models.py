from django.db import models
from django.contrib.auth.models import User
from Products.models import Product
from UsersManagement.models import Address
from django.core.validators import RegexValidator

class ShippingAddress(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    postal_code = models.CharField(validators=[RegexValidator(r'^\d{4}-\d{3}$')], max_length=8, null=False)
    city = models.CharField(max_length=100, null=False)
    nif = models.CharField(validators=[RegexValidator(r'^\d{9}$')], max_length=9, null=True)
    phone = models.CharField(validators=[RegexValidator(r'^\d{9}$')], max_length=9, null=False)
      
    
    
    def __str__(self):
        return self.address
    class Meta:
        db_table = 'ShippingAdress'
        verbose_name = 'ShippingAdress'
        verbose_name_plural = 'ShippingAdresses'
        ordering = ['id']
        
class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    card_number = models.CharField(validators=[RegexValidator(r'^\d{16}$')], max_length=16, null=False)
    card_holder = models.CharField(max_length=100, null=False)
    expiration_month = models.CharField(validators=[RegexValidator(r'^\d{2}$')], max_length=2, null=False)
    expiration_year = models.CharField(validators=[RegexValidator(r'^\d{2}$')], max_length=2, null=False)
    cvv = models.CharField(validators=[RegexValidator(r'^\d{3}$')], max_length=3, null=False)
    
    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        
    def __str__(self):
        return str(self.id)
class Order(models.Model):
    STATUS_CHOICES = (
        ('Pendente', 'Pendente'),
        ('Enviado', 'Enviado'),
        ('Recebido', 'Recebido'),
        ('Cancelado', 'Cancelado'),
    )
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pendente')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tracking_number = models.CharField(max_length=100, null=True)
    
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
