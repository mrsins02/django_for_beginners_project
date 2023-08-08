import os

from django.db import models


def get_ext(filename):
    ext = os.path.splitext(filename)[1]
    return ext


def upload_dir(instance, filename):
    ext = get_ext(filename)
    return f"banner/{instance.title}.{ext}"


class Setting(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=32, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}({self.pk})"

    class Meta:
        verbose_name = "Setting"
        verbose_name_plural = "Settings"


class Banner(models.Model):
    title = models.CharField(max_length=32)
    image = models.ImageField(upload_to=upload_dir)
    description = models.CharField(max_length=128)
    url = models.URLField()
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}({self.pk})"

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"
