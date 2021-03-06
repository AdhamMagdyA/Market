# Generated by Django 4.0.4 on 2022-05-17 05:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carts', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default=0, max_length=25)),
                ('last_name', models.CharField(default=0, max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('userPhoto', models.ImageField(default='media/profilePic.jpg', null=True, upload_to='', verbose_name='photos/%y/%m/%d')),
                ('last_login', models.DateField(default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=False)),
                ('userAuth', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.authorization')),
                ('userCart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='carts.cart')),
            ],
            options={
                'verbose_name': 'NormalUsers',
                'ordering': ['first_name'],
            },
        ),
    ]
