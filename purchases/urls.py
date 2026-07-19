from django.urls import path

from . import views

app_name = "purchases"

urlpatterns = [
    path("purchase/", views.purchase_vehicle_view, name="purchase_vehicle"),
    path("history/", views.purchase_history, name="purchase_history"),
]
