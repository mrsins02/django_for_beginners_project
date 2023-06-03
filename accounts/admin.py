from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserChangeForm
    # form = CustomUserCreationForm
    model = CustomUser
    list_display = ("username", "email", "is_active", "is_staff")
    list_editable = ("is_active", "is_staff")
    fieldsets = UserAdmin.fieldsets + (("Other info", {"fields": ("phone", "age", "sex", "address")}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("email",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
