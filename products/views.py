from django.shortcuts import render
from django.views.generic import TemplateView, ListView,DeleteView


class ProductListView(TemplateView):
    template_name = "products/product-list.html"


class ProductDetailView(TemplateView):
    template_name = "products/product-detail.html"
