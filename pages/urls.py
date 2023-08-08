from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import HomeView, ContactUsView

urlpatterns = [
    path("", HomeView.as_view(), name="home_page"),
    path("contact-us/", ContactUsView.as_view(), name="contact_us"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
