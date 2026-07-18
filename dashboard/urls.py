from django.urls import path

from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("users/", views.user_management, name="user_management"),
    path("profile/", views.profile, name="profile"),
    path("settings/", views.settings, name="settings"),
]
