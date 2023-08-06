from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ProductListView, ProductDetailView, SearchView

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path(
        "category/<slug:category>/",
        ProductListView.as_view(),
        name="product_category_list",
    ),
    path("brand/<slug:brand>/", ProductListView.as_view(), name="product_brand_list"),
    path("search/", SearchView.as_view(), name="product_search"),
    path("products/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
