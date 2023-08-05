from django.views.generic import ListView, DetailView

from .models import Product, Detail


class ProductListView(ListView):
    template_name = "products/product-list.html"
    context_object_name = "product_list"

    def get_queryset(self):
        queryset = Product.objects.filter(is_available=True).prefetch_related("detail_set")
        print(queryset.first().detail_set.first().price)
        return queryset


class ProductDetailView(DetailView):
    template_name = "products/product-detail.html"
    model = Product
