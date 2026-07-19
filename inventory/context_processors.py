from django.contrib.auth import get_user_model
from django.core.paginator import Paginator

from core.models import ContactMessage
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
    pagination = {}

    if request.path in filtered_paths:
        paginator = Paginator(vehicles, 6)
        page_obj = paginator.get_page(request.GET.get("page"))
        vehicles = page_obj.object_list
        query_params = request.GET.copy()
        query_params.pop("page", None)
        pagination = {
            "current": page_obj.number,
            "total": paginator.num_pages,
            "hasPrevious": page_obj.has_previous(),
            "previous": page_obj.previous_page_number() if page_obj.has_previous() else None,
            "hasNext": page_obj.has_next(),
            "next": page_obj.next_page_number() if page_obj.has_next() else None,
            "pages": list(paginator.page_range),
            "queryString": query_params.urlencode(),
        }

    purchase_queryset = Purchase.objects.select_related("vehicle", "user")
    user_queryset = get_user_model().objects.none()

    if request.user.is_authenticated:
        if request.user.is_superuser:
            purchases = purchase_queryset.all()
            user_queryset = get_user_model().objects.order_by("-date_joined")
            contact_messages = ContactMessage.objects.all()
        else:
            purchases = purchase_queryset.filter(user=request.user)
            contact_messages = ContactMessage.objects.none()
    else:
        purchases = Purchase.objects.none()
        contact_messages = ContactMessage.objects.none()

    return {
        "dealer_inventory_data": serialize_inventory(
            vehicles,
            purchases=purchases,
            users=user_queryset,
            request_user=request.user,
            pagination=pagination,
            contact_messages=contact_messages,
            brands_source=all_vehicles,
        ),
    }
