# Generated by Django 4.1.5 on 2023-01-23 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecapp', '0003_purchasedproduct_nameonpurchase_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchasedproduct',
            old_name='transcationid',
            new_name='transactionid',
        ),
    ]
