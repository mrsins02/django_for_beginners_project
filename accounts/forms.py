from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "email",
        )
        widgets = {
            "email": forms.EmailInput(attrs={"class": "single-input"}),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = "__all__"


class DashboardUserChangeForm(UserChangeForm):
    password = forms.CharField(widget=forms.TextInput(attrs={"type": "hidden"}), required=False)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "phone", "age", "sex", "address",)
