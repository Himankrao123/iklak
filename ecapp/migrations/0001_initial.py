# Generated by Django 4.1.5 on 2023-01-22 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ecapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('emailid', models.EmailField(max_length=254)),
                ('contactnumber', models.IntegerField()),
                ('subjecttocontact', models.TextField()),
                ('desc', models.TextField()),
                ('dateofcontact', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productID', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.FileField(upload_to=ecapp.models.product_directory_path)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('category', models.CharField(choices=[('bottle art', 'bottle art'), ('name plate', 'name plate'), ('madhubani painting', 'madhubani painting'), ('wall plate', 'wall plate')], default='madhubani painting', max_length=40)),
                ('size', models.CharField(max_length=40)),
                ('materials', models.CharField(max_length=100)),
                ('soldcount', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=1)),
                ('outofstock', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecapp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactnumber', models.IntegerField()),
                ('dateofbirth', models.DateField()),
                ('address', models.CharField(default='nowhere', max_length=100)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], default='male', max_length=20)),
                ('profilePhoto', models.FileField(upload_to=ecapp.models.user_directory_path)),
                ('verified', models.BooleanField(default=False)),
                ('userz', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PurchasedProduct',
            fields=[
                ('orderid', models.CharField(default='none', max_length=10, primary_key=True, serialize=False)),
                ('dateofpurchase', models.DateField()),
                ('quantity', models.IntegerField()),
                ('modeofpayment', models.CharField(choices=[('cod', 'cash on delivery'), ('online', 'online payment')], default='cod', max_length=20)),
                ('address', models.CharField(default='nowhere', max_length=200)),
                ('pincode', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('placed', 'placed'), ('shipped', 'shipped'), ('delivered', 'delivered')], default='placed', max_length=20)),
                ('phone', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecapp.product')),
                ('purchaser', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecapp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]