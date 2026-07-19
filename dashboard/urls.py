from django.urls import path

from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("users/", views.user_management, name="user_management"),
    path("users/invite/", views.invite_user, name="invite_user"),
    path("users/deactivate/", views.deactivate_user, name="deactivate_user"),
    path("contact-messages/", views.contact_messages, name="contact_messages"),
    path("contact-messages/delete/", views.delete_contact_message, name="delete_contact_message"),
    path("profile/", views.profile, name="profile"),
    path("settings/", views.settings, name="settings"),
]
