from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'volume', 'description', 'image')  
    list_filter = ('price',) 

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
