# Generated by Django 4.0.4 on 2022-05-17 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_productdiscount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='productDiscount',
        ),
    ]
