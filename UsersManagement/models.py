from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.
class Address(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address')
    
    addressLine1 = models.CharField(max_length=100, null=False)
    addressLine2 = models.CharField(max_length=100, null=True)
    postal_code = models.CharField(validators=[RegexValidator(r'^\d{4}-\d{3}$')], max_length=8, null=False)
    city = models.CharField(max_length=100, null=False)
    nif = models.CharField(validators=[RegexValidator(r'^\d{9}$')], max_length=9, null=True)
    phone = models.CharField(validators=[RegexValidator(r'^\d{9}$')], max_length=9, null=False)
      
    
    
    def __str__(self):
        return self.address
    class Meta:
        db_table = 'Adress'
        verbose_name = 'Adress'
        verbose_name_plural = 'Adresses'
        ordering = ['id']