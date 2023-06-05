from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("username", "email", "is_active", "is_staff", "is_verified")
    list_editable = ("is_active", "is_staff", "is_verified")
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("email", "is_verified")}),)
    fieldsets = UserAdmin.fieldsets + (("Other info", {"fields": ("phone", "age", "sex", "address", "is_verified")}),)


admin.site.register(CustomUser, CustomUserAdmin)
