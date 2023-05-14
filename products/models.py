from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    category = models.CharField(max_length=72, unique=True)
    slug = models.SlugField(db_index=True, editable=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # make a slug from category name
        self.slug = slugify(self.category)
        super(Category, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.category.capitalize()

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

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class Color(models.Model):
    color_name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(db_index=True, editable=False)
    color_code = models.CharField(max_length=32, unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # make a slug from color name
        self.slug = slugify(self.color_name)
        super(Color, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.color_name.capitalize()

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"


class Size(models.Model):
    size = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(db_index=True, editable=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # make a slug from size
        self.slug = slugify(self.size)
        super(Size, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.size.capitalize()

    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"


class Product(models.Model):
    sex_choices = {
        ("male", "Male"),
        ("female", "Female"),
    }
    name = models.CharField(max_length=72, unique=True)
    slug = models.SlugField(db_index=True, editable=False)
    category = models.ForeignKey(to="Category", on_delete=models.CASCADE)
    brand = models.ForeignKey(to="Brand", on_delete=models.CASCADE)
    price = models.CharField(max_length=8, default="0")
    count = models.IntegerField(default=0)
    sex = models.CharField(choices=sex_choices, default="male", max_length=16)
    is_available = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    size = models.ManyToManyField(to="Size")
    color = models.ManyToManyField(to="Color")

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # make a slug from product name
        self.slug = slugify(self.name)
        super(Product, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return self.name.capitalize()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
