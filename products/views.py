from typing import Any, Dict
from django.views.generic import ListView, DetailView

from .models import Product, Brand, Category


class ProductListView(ListView):
    template_name = "products/product-list.html"
    context_object_name = "product_list"

    def get_queryset(self):
        queryset = Product.objects.filter(is_available=True).prefetch_related(
            "detail_set", is_available=True
        )
        return queryset

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        brands = Brand.objects.all()
        new_context = {
            "categories": categories,
            "brands": brands,
        }
        context.update(new_context)
        return context


class ProductDetailView(DetailView):
    template_name = "products/product-detail.html"
    model = Product
