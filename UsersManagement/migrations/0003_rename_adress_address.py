# Generated by Django 5.0 on 2023-12-21 18:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UsersManagement', '0002_alter_adress_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='adress',
            new_name='Address',
        ),
    ]
