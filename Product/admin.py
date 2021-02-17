from django.contrib import admin
from Product.models import Product_Model
# Register your models here.
class Product_Model_Admin(admin.ModelAdmin):
    list_display = ['name','price','category','stock','create_date']

admin.site.register(Product_Model,Product_Model_Admin)
