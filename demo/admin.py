from django.contrib import admin
from . models import Product,Cart,Product_category,Product_line
# Register your models here.



admin.site.register(Cart)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','product_quantity','product_price',)
    list_filter = ['product_name']
    search_fields = ['product_name']


admin.site.register(Product,ProductAdmin)


class Product_categoryAdmin(admin.ModelAdmin):
    list_display = ('product_cat',)
    list_filter = ['product_cat']
    search_fields = ['product_cat']

admin.site.register(Product_category,Product_categoryAdmin)


class Product_lineAdmin(admin.ModelAdmin):
    list_display = ('product_line','Product_category_F')
    list_filter = ['product_line']
    search_fields = ['product_line']

admin.site.register(Product_line,Product_lineAdmin)