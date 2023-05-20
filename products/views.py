from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DeleteView

from .models import Product


class ProductListView(ListView):
    template_name = "products/product-list.html"
    model = Product


class ProductDetailView(DeleteView):
    template_name = "products/product-detail.html"
    model = Product
