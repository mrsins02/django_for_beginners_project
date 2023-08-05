import os.path

from django.core import validators
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.text import slugify


def get_ext(filename):
    ext = os.path.splitext(filename)[1]
    return ext


def upload_dir(instance, filename):
    ext = get_ext(filename)
    return f"products/{instance.product.category.slug[:32]}/{instance.product.slug}/{instance.product.slug}.{ext}"


class Category(models.Model):
    category = models.CharField(max_length=72, unique=True)
    slug = models.SlugField(db_index=True, editable=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # make a slug from category name
        self.slug = slugify(self.category)
        super(Category, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.category.capitalize()

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.slug])

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Brand(models.Model):
    brand = models.CharField(max_length=72, unique=True)
    slug = models.SlugField(db_index=True, editable=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # make a slug from brand name
        self.slug = slugify(self.brand)
        super(Brand, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.brand.capitalize()

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.slug])

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class Size(models.Model):
    size = models.CharField(max_length=72, unique=True)

    def __str__(self):
        return self.size.capitalize()

    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"


class Color(models.Model):
    color = models.CharField(max_length=72, unique=True)
    code = models.CharField(max_length=72, unique=True)

    def __str__(self):
        return self.color.capitalize()

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"


class Product(models.Model):
    sex_choices = {
        ("male", "Male"),
        ("female", "Female"),
    }
    name = models.CharField(max_length=72, unique=True)
    slug = models.SlugField(db_index=True, editable=False)
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE)
    brand = models.ForeignKey(to="Brand", on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # make a slug from product name
        self.slug = slugify(self.name)
        super(Product, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.name.capitalize()

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.slug])

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("-date_created",)


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True, upload_to=upload_dir)

    def __str__(self):
        return f"{self.product.name}({self.pk})"

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe(f"<img src='{self.image.url}' height='50'/>")
        else:
            return ""
    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Products Images"


class Detail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0,
                                validators=[validators.MinValueValidator(0)])
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.name}({self.size})({self.color})"

    class Meta:
        verbose_name = "Product Detail"
        verbose_name_plural = "Products Details"
