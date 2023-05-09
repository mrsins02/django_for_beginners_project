from django.contrib import admin
from .models import Product, Category, Brand, Size, Color


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "count", "is_available")
    list_editable = ("price", "count", "is_available")
    list_filter = ("category__category", "brand__brand", "size__size", "color__color_name", "is_available")


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Product, ProductsAdmin)
