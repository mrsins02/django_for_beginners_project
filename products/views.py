from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Prefetch, Q
from .models import Product, Brand, Category, Detail


class ProductListView(ListView):
    template_name = "products/product-list.html"
    context_object_name = "product_list"

    def get_queryset(self):
        ordering = self.request.GET.get("ordering", "-id")
        if category := self.kwargs.get("category"):
            queryset = (
                Product.objects.filter(
                    category__slug__iexact=category, is_available=True
                )
                .order_by(ordering)
                .prefetch_related(
                    Prefetch(
                        lookup="detail_set",
                        queryset=Detail.objects.filter(is_available=True),
                    )
                )
            )
        elif brand := self.kwargs.get("brand"):
            queryset = (
                Product.objects.filter(brand__slug__iexact=brand, is_available=True)
                .order_by(ordering)
                .prefetch_related(
                    Prefetch(
                        lookup="detail_set",
                        queryset=Detail.objects.filter(is_available=True),
                    )
                )
            )
        elif search := self.request.GET.get("search"):
            queryset = (
                Product.objects.filter(
                    Q(name__contains=search)
                    | Q(category__category__contains=search)
                    | Q(brand__brand__contains=search),
                    is_available=True,
                )
                .order_by(ordering)
                .prefetch_related(
                    Prefetch(
                        lookup="detail_set",
                        queryset=Detail.objects.filter(is_available=True),
                    )
                )
            )
        else:
            queryset = (
                Product.objects.filter(is_available=True)
                .order_by(ordering)
                .prefetch_related(
                    Prefetch(
                        lookup="detail_set",
                        queryset=Detail.objects.filter(is_available=True),
                    )
                )
            )
        return queryset

    def get_context_data(self, **kwargs):
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
    context_object_name = "product"

    def get_queryset(self):
        queryset = Product.objects.filter(
            slug__exact=self.kwargs.get("slug"), is_available=True
        ).prefetch_related(
            Prefetch(
                lookup="detail_set",
                queryset=Detail.objects.filter(is_available=True),
            )
        )
        return queryset


class SearchView(TemplateView):
    template_name = "products/search.html"
