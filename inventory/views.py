from django.shortcuts import render

from authentication.access import admin_required


def inventory(request):
    return render(request, "inventory/inventory.html")


def vehicle_details(request):
    return render(request, "inventory/vehicle_details.html")


def search_results(request):
    return render(request, "inventory/search_results.html")


@admin_required
def manage_vehicles(request):
    return render(request, "inventory/manage_vehicles.html")


@admin_required
def add_vehicle(request):
    return render(request, "inventory/add_vehicle.html")


@admin_required
def update_vehicle(request):
    return render(request, "inventory/update_vehicle.html")


@admin_required
def delete_confirmation(request):
    return render(request, "inventory/delete_confirmation.html")


@admin_required
def inventory_management(request):
    return render(request, "inventory/inventory_management.html")
