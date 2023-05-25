from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Product
from .forms import ProductCreateForm, ProductUpdateForm


class ProductListView(ListView):
    template_name = "products/product-list.html"
    model = Product


class ProductDetailView(DetailView):
    template_name = "products/product-detail.html"
    model = Product


class DashboardView(ListView):
    template_name = "products/dashboard.html"
    model = Product


class ProductCreateView(CreateView):
    template_name = "products/product-create.html"
    model = Product
    form_class = ProductCreateForm


class ProductUpdateView(UpdateView):
    template_name = "products/product-update.html"
    model = Product
    form_class = ProductUpdateForm

    def get_object(self, queryset=None):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Product, slug=slug)


class ProductDeleteView(DeleteView):
    template_name = "products/product-delete.html"
    model = Product
    success_url = reverse_lazy("product_dashboard")

    def get_object(self, queryset=None):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Product, slug=slug)
