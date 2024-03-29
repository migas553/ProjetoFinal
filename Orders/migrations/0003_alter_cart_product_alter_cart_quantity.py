# Generated by Django 5.0 on 2023-12-26 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0002_alter_orderproducts_options_and_more'),
        ('Products', '0008_alter_category_slug_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Products.product'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
