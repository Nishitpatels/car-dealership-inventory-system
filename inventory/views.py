from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from authentication.access import admin_required
from .forms import RestockForm, VehicleForm
from .image_services import assign_vehicle_image, delete_vehicle_image_if_unused
from .models import Vehicle


def get_inventory_queryset():
    return Vehicle.objects.all()


def get_vehicle_from_request(request):
    vehicle_id = request.GET.get("id") or request.POST.get("id")
    if not vehicle_id:
        return None
    try:
        return get_object_or_404(Vehicle, pk=vehicle_id)
    except (ValueError, ValidationError):
        return None


def add_form_errors_to_messages(request, form):
    for field, errors in form.errors.items():
        label = form.fields[field].label if field in form.fields else "Vehicle"
        for error in errors:
            messages.error(request, f"{label}: {error}")


def inventory(request):
    return render(request, "inventory/inventory.html")


def vehicle_details(request):
    vehicle_id = request.GET.get("id")
    if vehicle_id:
        try:
            exists = Vehicle.objects.filter(pk=vehicle_id).exists()
        except (ValueError, ValidationError):
            exists = False
        if not exists:
            messages.error(request, "Vehicle not found.")
            return render(request, "core/404.html", status=404)
    return render(request, "inventory/vehicle_details.html")


def search_results(request):
    return render(request, "inventory/search_results.html")


@admin_required
def manage_vehicles(request):
    return render(request, "inventory/manage_vehicles.html")


@admin_required
def add_vehicle(request):
    if request.method == "POST":
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            assign_vehicle_image(vehicle)
            vehicle.save()
            messages.success(request, "Vehicle added successfully.")
            return redirect(f"{reverse('inventory:vehicle_details')}?id={vehicle.pk}")
        add_form_errors_to_messages(request, form)

    return render(request, "inventory/add_vehicle.html")


@admin_required
def update_vehicle(request):
    vehicle = get_vehicle_from_request(request)
    if vehicle is None:
        messages.error(request, "Select a vehicle to update.")
        return redirect("inventory:manage_vehicles")

    if request.method == "POST":
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            vehicle = form.save(commit=False)
            assign_vehicle_image(vehicle)
            vehicle.save()
            messages.success(request, "Vehicle updated successfully.")
            return redirect(f"{reverse('inventory:vehicle_details')}?id={vehicle.pk}")
        add_form_errors_to_messages(request, form)

    return render(request, "inventory/update_vehicle.html")


@admin_required
def delete_confirmation(request):
    vehicle = get_vehicle_from_request(request)
    if vehicle is None:
        messages.error(request, "Select a vehicle to delete.")
        return redirect("inventory:manage_vehicles")

    if request.method == "POST":
        delete_vehicle_image_if_unused(vehicle)
        vehicle.delete()
        messages.success(request, "Vehicle deleted successfully.")
        return redirect("inventory:manage_vehicles")

    return render(request, "inventory/delete_confirmation.html")


@admin_required
def inventory_management(request):
    return render(request, "inventory/inventory_management.html")


@require_POST
@admin_required
def restock_vehicle(request):
    form = RestockForm(request.POST)
    if not form.is_valid():
        for errors in form.errors.values():
            for error in errors:
                messages.error(request, error)
        return redirect("inventory:inventory_management")

    with transaction.atomic():
        vehicle = get_object_or_404(Vehicle.objects.select_for_update(), pk=form.cleaned_data["vehicle_id"])
        vehicle.quantity += form.cleaned_data["quantity"]
        vehicle.save(update_fields=["quantity", "updated_at"])

    messages.success(request, f"{vehicle} restocked by {form.cleaned_data['quantity']} unit(s).")
    return redirect("inventory:inventory_management")
