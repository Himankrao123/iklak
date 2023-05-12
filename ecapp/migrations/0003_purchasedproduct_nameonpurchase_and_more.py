# Generated by Django 4.1.5 on 2023-01-23 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecapp', '0002_userprofile_verifycode'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasedproduct',
            name='nameonpurchase',
            field=models.CharField(default='none', max_length=40),
        ),
        migrations.AddField(
            model_name='purchasedproduct',
            name='paymentid',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='purchasedproduct',
            name='paymentstatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='purchasedproduct',
            name='transcationid',
            field=models.CharField(default='none', max_length=20),
        ),
    ]
