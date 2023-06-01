from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic.edit import CreateView

user = get_user_model()


class SignUpView(CreateView):
    template_name = "accounts/sign-up.html"
    model = user
    fields = "__all__"
