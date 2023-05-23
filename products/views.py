from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Product
from .forms import ProductCreateForm


class ProductListView(ListView):
    template_name = "products/product-list.html"
    model = Product


class ProductDetailView(DetailView):
    template_name = "products/product-detail.html"
    model = Product


class DashboardView(TemplateView):
    template_name = "products/dashboard.html"


class ProductCreateView(CreateView):
    template_name = "products/product-create.html"
    model = Product
    form_class = ProductCreateForm


class ProductUpdateView(UpdateView):
    template_name = "products/product-detail.html"
    model = Product


class ProductDeleteView(DeleteView):
    template_name = "products/product-detail.html"
    model = Product
