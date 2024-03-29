# Generated by Django 4.2 on 2023-05-11 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecapp', '0008_alter_product_category_alter_userprofile_verifycode'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('paymentid', models.CharField(default='none', max_length=20, primary_key=True, serialize=False, unique=True)),
                ('transactionid', models.CharField(default='none', max_length=20)),
                ('paymentstatus', models.BooleanField(default=False)),
                ('modeofpayment', models.CharField(choices=[('card', 'debit/creditcard'), ('net', 'net banking'), ('upi', 'upi')], default='card', max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='purchasedproduct',
            name='address',
        ),
        migrations.RemoveField(
            model_name='purchasedproduct',
            name='dateofpurchase',
        ),
        migrations.RemoveField(
            model_name='purchasedproduct',
            name='modeofpayment',
        ),
        migrations.RemoveField(
            model_name='purchasedproduct',
            name='nameonpurchase',
        ),
        migrations.RemoveField(
            model_name='purchasedproduct',
            name='paymentid',
        ),
        migrations.RemoveField(
            model_name='purchasedproduct',
            name='paymentstatus',
        ),
        migrations.RemoveField(
            model_name='purchasedproduct',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='purchasedproduct',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='purchasedproduct',
            name='purchaser',
        ),
        migrations.RemoveField(
            model_name='purchasedproduct',
            name='status',
        ),
        migrations.RemoveField(
            model_name='purchasedproduct',
            name='transactionid',
        ),
        migrations.AddField(
            model_name='purchasedproduct',
            name='purchasedprodid',
            field=models.CharField(default='none', max_length=20, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('orderid', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('nameonpurchase', models.CharField(default='none', max_length=40)),
                ('dateofpurchase', models.DateField()),
                ('address', models.CharField(default='nowhere', max_length=200)),
                ('pincode', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('placed', 'placed'), ('shipped', 'shipped'), ('delivered', 'delivered')], default='placed', max_length=20)),
                ('phone', models.IntegerField()),
                ('paymentid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecapp.paymentdetails')),
                ('purchaser', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='purchasedproduct',
            name='orderid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecapp.orderdetails'),
        ),
    ]
