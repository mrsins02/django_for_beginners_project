from django.urls import path
from .views import SignUpView, DashboardView, UpdateProfileView

urlpatterns = [
    path("sign-up/", SignUpView.as_view(), name="sign_up"),
    path("dashboard/update/<int:pk>/", UpdateProfileView.as_view(), name="update_user_profile"),
    path("dashboard/<int:pk>/", DashboardView.as_view(), name="user_dashboard"),
]
