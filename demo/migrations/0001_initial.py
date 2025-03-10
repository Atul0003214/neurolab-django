# Generated by Django 4.1.4 on 2022-12-28 12:05

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_product_name', models.CharField(max_length=100)),
                ('cart_product_desc', models.TextField()),
                ('cart_prod_quantity', models.DecimalField(decimal_places=0, max_digits=1000)),
                ('cart_product_price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('cart_product_discount', models.FloatField(max_length=4)),
                ('cart_prod_sell_price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('cart_prod_net_price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('cart_prod_deli_chrg', models.DecimalField(decimal_places=2, default=0, max_digits=1000)),
                ('cart_prod_total', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('cart_user_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_cat', models.CharField(max_length=50)),
                ('product_cat_image', models.ImageField(upload_to='demo/static/images/')),
                ('product_cat_slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='product_cat', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product_line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_line', models.CharField(max_length=100)),
                ('product_line_image', models.ImageField(upload_to='demo/static/images/')),
                ('product_line_slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='product_line', unique=True)),
                ('Product_category_F', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.product_category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_desc', models.TextField()),
                ('product_image', models.ImageField(upload_to='demo/static/images/')),
                ('product_quantity', models.DecimalField(decimal_places=0, max_digits=1000)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('product_discount', models.FloatField(max_length=4)),
                ('product_sell_price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('product_net_price', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('prod_del_check', models.IntegerField()),
                ('prod_deli_charg_req', models.BooleanField()),
                ('prod_delivery_charge', models.DecimalField(decimal_places=2, default=0, max_digits=1000)),
                ('product_name_slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='product_name', unique=True)),
                ('product_line_F', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.product_line')),
            ],
        ),
    ]
