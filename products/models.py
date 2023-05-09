from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    category = models.CharField(max_length=72)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Brand(models.Model):
    brand = models.CharField(max_length=72)

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class Color(models.Model):
    color_name = models.CharField(max_length=32)
    color_code = models.CharField(max_length=32)

    def __str__(self):
        return self.color_name

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"


class Size(models.Model):
    size = models.CharField(max_length=32)

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"


class Product(models.Model):
    name = models.CharField(max_length=72)
    slug = models.SlugField(db_index=True, editable=False)
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE)
    brand = models.ForeignKey(to="Brand", on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    size = models.ForeignKey(to="Size", on_delete=models.CASCADE)
    color = models.ForeignKey(to="Color", on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # make a slug from product name
        self.slug = slugify(self.name)
        super(Product, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
