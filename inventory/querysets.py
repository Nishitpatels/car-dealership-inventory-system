from decimal import Decimal, InvalidOperation

from django.db.models import Q

from .models import Vehicle


def vehicle_search_queryset(params, base_queryset=None):
    queryset = base_queryset or Vehicle.objects.all()

    query = (params.get("q") or params.get("query") or "").strip()
    make = (params.get("make") or "").strip()
    model = (params.get("model") or "").strip()
    category = (params.get("category") or "").strip()
    min_price = (params.get("min_price") or params.get("min-price") or "").strip()
    max_price = (params.get("max_price") or params.get("max-price") or params.get("budget") or "").strip()
    availability = (params.get("availability") or params.get("status") or "").strip()

    if query:
        query_filter = (
            Q(make__icontains=query)
            | Q(model__icontains=query)
            | Q(category__icontains=query)
            | Q(description__icontains=query)
        )
        for term in query.split():
            query_filter |= (
                Q(make__icontains=term)
                | Q(model__icontains=term)
                | Q(category__icontains=term)
                | Q(description__icontains=term)
            )
        queryset = queryset.filter(query_filter)

    if make:
        queryset = queryset.filter(make__icontains=make)

    if model:
        queryset = queryset.filter(model__icontains=model)

    if category:
        queryset = queryset.filter(category__icontains=category)

    try:
        if min_price:
            queryset = queryset.filter(price__gte=Decimal(min_price))
    except InvalidOperation:
        pass

    try:
        if max_price:
            queryset = queryset.filter(price__lte=Decimal(max_price))
    except InvalidOperation:
        pass

    if availability == "Available":
        queryset = queryset.filter(quantity__gt=2)
    elif availability == "Low Stock":
        queryset = queryset.filter(quantity__gt=0, quantity__lte=2)
    elif availability == "Out of Stock":
        queryset = queryset.filter(quantity=0)

    return queryset
