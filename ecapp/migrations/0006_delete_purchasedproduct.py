# Generated by Django 4.1.5 on 2023-01-24 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecapp', '0005_alter_purchasedproduct_modeofpayment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PurchasedProduct',
        ),
    ]
