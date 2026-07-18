from django.urls import path

from . import views

app_name = "inventory"

urlpatterns = [
    path("", views.inventory, name="inventory"),
    path("vehicle-details/", views.vehicle_details, name="vehicle_details"),
    path("search-results/", views.search_results, name="search_results"),
    path("manage-vehicles/", views.manage_vehicles, name="manage_vehicles"),
    path("add-vehicle/", views.add_vehicle, name="add_vehicle"),
    path("update-vehicle/", views.update_vehicle, name="update_vehicle"),
    path("delete-confirmation/", views.delete_confirmation, name="delete_confirmation"),
    path("inventory-management/", views.inventory_management, name="inventory_management"),
]
