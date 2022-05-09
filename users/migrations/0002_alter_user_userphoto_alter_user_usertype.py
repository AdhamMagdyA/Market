# Generated by Django 4.0.4 on 2022-05-08 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userPhoto',
            field=models.ImageField(default='media/profilePic.jpg', null=True, upload_to='', verbose_name='photos/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='user',
            name='userType',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('USER', 'User'), ('SELLER', 'Seller')], default='USER', max_length=20),
        ),
    ]