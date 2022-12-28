from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class Product_category(models.Model):
    product_cat = models.CharField(max_length=50)
    product_cat_image = models.ImageField(upload_to='demo/static/images/')
    product_cat_slug = AutoSlugField(populate_from='product_cat',unique = True, null=True, default=None)
    


class Product_line(models.Model):
    product_line = models.CharField(max_length=100)
    product_line_image = models.ImageField(upload_to='demo/static/images/')
    product_line_slug = AutoSlugField(populate_from='product_line',unique = True, null=True, default=None)
    Product_category_F = models.ForeignKey(Product_category, on_delete=models.CASCADE )

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_desc = models.TextField()
    product_image = models.ImageField(upload_to='demo/static/images/')
    product_quantity = models.DecimalField(max_digits=1000,decimal_places=0)
    product_price = models.DecimalField(max_digits=1000,decimal_places=2)
    product_discount =  models.FloatField(max_length=4)
    product_sell_price = models.DecimalField(max_digits=1000,decimal_places=2)
    product_net_price =  models.DecimalField(max_digits=1000,decimal_places=2)
    prod_del_check = models.IntegerField()
    prod_deli_charg_req = models.BooleanField()
    prod_delivery_charge = models.DecimalField(max_digits=1000,decimal_places=2,default=0)
    product_name_slug = AutoSlugField(populate_from='product_name',unique = True, null=True, default=None)
    product_line_F = models.ForeignKey(Product_line, on_delete = models.CASCADE)



class Cart(models.Model):
    cart_product_name = models.CharField(max_length=100)    
    cart_product_desc = models.TextField()
    cart_prod_quantity = models.DecimalField(max_digits=1000,decimal_places=0)
    cart_product_price = models.DecimalField(max_digits=1000,decimal_places=2)
    cart_product_discount =  models.FloatField(max_length=4)
    cart_prod_sell_price = models.DecimalField(max_digits=1000,decimal_places=2)
    cart_prod_net_price =  models.DecimalField(max_digits=1000,decimal_places=2)
    cart_prod_deli_chrg = models.DecimalField(max_digits=1000,decimal_places=2,default=0)
    cart_prod_total = models.DecimalField(max_digits=1000,decimal_places=2)
    cart_user_id = models.CharField(max_length=100)
    

