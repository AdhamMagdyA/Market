# Generated by Django 4.0.4 on 2022-05-16 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_productoldprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=2, null=True),
        ),
    ]
