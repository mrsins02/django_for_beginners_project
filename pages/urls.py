from django.urls import path
from .views import HomeView, AboutUsView

urlpatterns = [
    path("", HomeView.as_view(), name="home_page"),
    path("about-us", AboutUsView.as_view(), name="about_page"),
]
