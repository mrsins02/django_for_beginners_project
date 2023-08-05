
from django.views.generic import ListView, DetailView

from .models import Product


class ProductListView(ListView):
    template_name = "products/product-list.html"
    model = Product


class ProductDetailView(DetailView):
    template_name = "products/product-detail.html"
    model = Product



