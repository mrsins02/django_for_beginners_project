from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

user = get_user_model()


class SignUpView(CreateView):
    template_name = "accounts/sign-up.html"
    model = user
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
