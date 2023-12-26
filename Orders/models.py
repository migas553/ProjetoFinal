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
    products = models.ManyToManyField(Product, through='OrderProduct')
    quantity = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pendente')
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    