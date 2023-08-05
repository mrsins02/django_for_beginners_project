from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import \
    ProductListView, \
    ProductDetailView

urlpatterns = [
                  path("", ProductListView.as_view(), name="product_list"),
                  path("products/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
