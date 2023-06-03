from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    sex_choices = (("male", "Male"),
                   ("female", "Female"))

    phone = models.CharField(max_length=16, blank=True, default="")
    age = models.PositiveIntegerField(blank=True, null=True)
    sex = models.CharField(choices=sex_choices, max_length=8, blank=True, default="")
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.username}"

    def get_name(self):
        try:
            return f"{self.first_name} {self.last_name}".capitalize()
        except ValueError:
            return ""
