from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, TemplateView,CreateView, UpdateView, DeleteView, FormView

from .models import Product
from .forms import ProductCreateForm, ProductUpdateForm, ProductFormSet


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


class ProductDeleteView(DeleteView):
    template_name = "products/product-delete.html"
    model = Product
    success_url = reverse_lazy("product_dashboard")


class PoductPictureUpdateView(UpdateView):
    template_name = "products/picture-update.html"
    model = Product
    form_class = ProductFormSet

    def get_success_url(self):
        slug = self.get_object().slug
        return reverse("product_detail", args=[slug, ])
