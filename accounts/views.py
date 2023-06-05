from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from .forms import CustomUserCreationForm, DashboardUserChangeForm

User = get_user_model()


class SignUpView(CreateView):
    template_name = "accounts/sign-up.html"
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")


class DashboardView(DetailView):
    template_name = "accounts/dashboard.html"
    model = User


class UpdateProfileView(UpdateView):
    template_name = "accounts/update-profile.html"
    model = User
    form_class = DashboardUserChangeForm

    def get_success_url(self):
        return reverse("user_dashboard", args=(self.request.user.pk,))
