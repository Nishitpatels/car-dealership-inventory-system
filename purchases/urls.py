from django.urls import path

from . import views

app_name = "purchases"

urlpatterns = [
    path("history/", views.purchase_history, name="purchase_history"),
]
