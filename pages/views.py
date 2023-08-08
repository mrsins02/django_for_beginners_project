from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Setting, Banner


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        banner = Banner.objects.get(is_default=True)
        context_ = {
            "banner": banner,
        }
        context.update(context_)
        return context


class ContactUsView(TemplateView):
    template_name = "pages/contact-us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        setting = Setting.objects.get(is_default=True)
        context_ = {
            "setting": setting,
        }
        context.update(context_)
        return context
