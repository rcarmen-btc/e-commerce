from django.contrib import admin

from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image', 'in_stock', 'is_active', 'price', 'created_by', 'slug')
    list_editable = ('category', 'image', 'in_stock', 'is_active', 'price', 'created_by')
    prepopulated_fields = {'slug': ('title', ), }
    search_fields = ('title', )



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    prepopulated_fields = {'slug': ('name', ), }

