from django.urls import path
from .views import \
    ProductListView, \
    ProductDetailView, \
    DashboardView, \
    ProductCreateView, \
    ProductUpdateView, \
    ProductDeleteView

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/update/<slug:slug>/", ProductUpdateView.as_view(), name="product_update"),
    path("products/delete/<slug:slug>/", ProductDeleteView.as_view(), name="product_delete"),
    path("products/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
    path("dashboard/", DashboardView.as_view(), name="product_dashboard"),
]
