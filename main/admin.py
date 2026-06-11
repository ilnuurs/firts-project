from django.contrib import admin

# Register your models here.
from .models import Product, Category



class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id",'name')
    list_display_links = ("id", 'name')
    search_fields = ('name',)
    
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id",'name')
    list_display_links = ("id", 'name')
    search_fields = ('name',)
    
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

