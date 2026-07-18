from django.shortcuts import render


def inventory(request):
    return render(request, "inventory/inventory.html")


def vehicle_details(request):
    return render(request, "inventory/vehicle_details.html")


def search_results(request):
    return render(request, "inventory/search_results.html")


def manage_vehicles(request):
    return render(request, "inventory/manage_vehicles.html")


def add_vehicle(request):
    return render(request, "inventory/add_vehicle.html")


def update_vehicle(request):
    return render(request, "inventory/update_vehicle.html")


def delete_confirmation(request):
    return render(request, "inventory/delete_confirmation.html")


def inventory_management(request):
    return render(request, "inventory/inventory_management.html")
