from django.contrib import admin
from .models import Product, Category, Brand, Image, Detail, Size, Color


class ProductImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ('id', 'image_tag',)
    extra = 1


class ProductDetailInline(admin.TabularInline):
    model = Detail
    readonly_fields = ('id',)
    extra = 1


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name", "category",)
    list_filter = ("category__category", "brand__brand")
    inlines = (ProductImageInline, ProductDetailInline)


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Image)
admin.site.register(Detail)
admin.site.register(Product, ProductsAdmin)
