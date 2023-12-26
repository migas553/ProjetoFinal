# Generated by Django 5.0 on 2023-12-26 14:38

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0005_shippingaddress_alter_order_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('card_number', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator('^\\d{16}$')])),
                ('card_holder', models.CharField(max_length=100)),
                ('expiration_date', models.DateField()),
                ('cvv', models.CharField(max_length=3, validators=[django.core.validators.RegexValidator('^\\d{3}$')])),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Orders.payment'),
            preserve_default=False,
        ),
    ]
