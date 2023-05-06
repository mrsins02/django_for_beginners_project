from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "pages/home.html"


class ContactUsView(TemplateView):
    template_name = "pages/contact-us.html"
