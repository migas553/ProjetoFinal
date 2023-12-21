from django.db import models
from UsersManagement.models import User
from Products.models import Product
# Create your models here.


# def Order(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product)
#     total = models.FloatField()
#     date = models.DateField(auto_now_add=True)
#     status = models.CharField(max_length=50)
#     address = models.CharField(max_length=100)
#     phone = models.CharField(max_length=20)
#     email = models.EmailField()
#     def __str__(self):
#         return self.id
#     class Meta:
#         db_table = 'Order'
#         verbose_name = 'Order'
#         verbose_name_plural = 'Orders'
#         ordering = ['id']
        