from django.contrib.auth import get_user_model

from purchases.models import Purchase

from .models import Vehicle
from .querysets import vehicle_search_queryset
from .serializers import serialize_inventory


def dealer_inventory(request):
    all_vehicles = Vehicle.objects.all()
    filtered_paths = (
        "/inventory/",
        "/inventory/search-results/",
    )
    should_filter = request.path in filtered_paths and request.GET
    vehicles = vehicle_search_queryset(request.GET, all_vehicles) if should_filter else all_vehicles

    purchase_queryset = Purchase.objects.select_related("vehicle", "user")
    user_queryset = get_user_model().objects.none()

    if request.user.is_authenticated:
        if request.user.is_superuser:
            purchases = purchase_queryset.all()
            user_queryset = get_user_model().objects.order_by("-date_joined")
        else:
            purchases = purchase_queryset.filter(user=request.user)
    else:
        purchases = Purchase.objects.none()

    return {
        "dealer_inventory_data": serialize_inventory(
            vehicles,
            purchases=purchases,
            users=user_queryset,
            request_user=request.user,
        ),
    }
