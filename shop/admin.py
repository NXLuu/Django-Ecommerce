from django.contrib import admin
from .models import Category, Product, Publisher

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'date', 'publisher']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Publisher)
# admin.site.register(Menu)
# admin.site.register(Item)
