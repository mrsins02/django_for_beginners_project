from django.contrib import admin
from .models import Product, Category, Brand, Size, Color

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Product)
