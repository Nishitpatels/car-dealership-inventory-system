from django.urls import path

from . import views

app_name = "authentication"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("admin-login/", views.admin_login, name="admin_login"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("register/", views.register, name="register"),
]
