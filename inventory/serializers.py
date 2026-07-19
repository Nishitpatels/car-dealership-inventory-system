from calendar import month_abbr
from collections import OrderedDict
from decimal import Decimal

from django.utils import timezone

from core.models import ContactMessage


def format_price(value):
    amount = Decimal(value)
    return f"${amount:,.0f}"


def format_date(value):
    if not value:
        return "Never"
    return value.strftime("%b %d, %Y")


def serialize_vehicle(vehicle):
    image_url = vehicle.image.url if vehicle.image else "/static/images/vehicles/default-vehicle.svg"
    labels = []
    if vehicle.price >= Decimal("60000"):
        labels.append("Premium")
    if vehicle.quantity > 0 and vehicle.quantity <= 2:
        labels.append("Low Stock")

    return {
        "id": vehicle.pk,
        "make": vehicle.make,
        "model": vehicle.model,
        "category": vehicle.category,
        "price": format_price(vehicle.price),
        "priceValue": float(vehicle.price),
        "quantity": vehicle.quantity,
        "status": vehicle.availability,
        "labels": labels,
        "year": vehicle.created_at.year,
        "fuel": "Petrol",
        "transmission": "Automatic",
        "engine": "Verified dealership listing",
        "mileage": "Contact showroom",
        "colour": "Showroom finish",
        "image": image_url,
        "gallery": [image_url],
        "description": vehicle.description,
        "createdAt": format_date(vehicle.created_at),
        "updatedAt": format_date(vehicle.updated_at),
        "features": [
            "Verified inventory record",
            "Dealer inspected listing",
            f"{vehicle.category} category",
            "Price and availability from database",
            "Session-protected admin controls",
            "Ready for purchase workflow",
        ],
    }


def serialize_purchase(purchase):
    vehicle = purchase.vehicle
    user = purchase.user
    customer_name = f"{user.first_name} {user.last_name}".strip() or user.username
    image_url = vehicle.image.url if vehicle.image else "/static/images/vehicles/default-vehicle.svg"
    return {
        "id": purchase.pk,
        "code": f"PUR-{purchase.pk:05d}",
        "userId": user.pk,
        "customer": customer_name,
        "customerEmail": user.email,
        "vehicle": f"{vehicle.make} {vehicle.model}",
        "vehicleId": vehicle.pk,
        "vehicleImage": image_url,
        "price": format_price(purchase.purchase_price),
        "priceValue": float(purchase.purchase_price),
        "total": format_price(purchase.total_price),
        "totalValue": float(purchase.total_price),
        "quantity": purchase.quantity,
        "date": format_date(purchase.created_at),
        "status": purchase.status,
    }


def serialize_user(user):
    name = f"{user.first_name} {user.last_name}".strip() or user.username
    initials = "".join(part[0] for part in name.split()[:2]).upper() or user.username[:2].upper()
    if user.is_superuser:
        role = "Superuser"
    elif user.is_staff:
        role = "Staff"
    else:
        role = "Customer"

    return {
        "id": user.pk,
        "initials": initials,
        "name": name,
        "email": user.email,
        "username": user.username,
        "role": role,
        "status": "Active" if user.is_active else "Inactive",
        "lastLogin": format_date(user.last_login),
        "joinedAt": format_date(user.date_joined),
        "isSuperuser": user.is_superuser,
    }


def serialize_contact_message(message):
    return {
        "id": message.pk,
        "name": message.name,
        "email": message.email,
        "subject": message.subject,
        "message": message.message,
        "submittedAt": format_date(message.submitted_at),
    }


def build_stats(vehicles, purchases=None, users=None):
    purchases = list(purchases or [])
    users = list(users or [])
    total_units = sum(vehicle.quantity for vehicle in vehicles)
    available_vehicle_lines = sum(1 for vehicle in vehicles if vehicle.quantity > 0)
    out_of_stock = sum(1 for vehicle in vehicles if vehicle.quantity <= 0)
    low_stock = sum(1 for vehicle in vehicles if 0 < vehicle.quantity <= 2)
    inventory_value = sum(vehicle.price * vehicle.quantity for vehicle in vehicles)
    revenue = sum(purchase.total_price for purchase in purchases)
    active_users = sum(1 for user in users if user.is_active)

    return {
        "totalVehicles": len(vehicles),
        "availableStock": total_units,
        "availableVehicleLines": available_vehicle_lines,
        "outOfStock": out_of_stock,
        "lowStock": low_stock,
        "criticalAlerts": out_of_stock + low_stock,
        "totalPurchases": len(purchases),
        "totalUsers": len(users),
        "activeUsers": active_users,
        "inventoryValue": format_price(inventory_value),
        "inventoryValueValue": float(inventory_value),
        "revenue": format_price(revenue),
        "revenueValue": float(revenue),
        "totalUnits": total_units,
        "averagePurchaseValue": format_price(revenue / len(purchases)) if purchases else "$0",
    }


def build_revenue_chart(purchases):
    now = timezone.now()
    buckets = OrderedDict()

    for offset in range(6, -1, -1):
        month = now.month - offset
        year = now.year
        while month <= 0:
            month += 12
            year -= 1
        buckets[(year, month)] = Decimal("0")

    for purchase in purchases:
        key = (purchase.created_at.year, purchase.created_at.month)
        if key in buckets:
            buckets[key] += purchase.total_price

    return {
        "labels": [month_abbr[month] for _, month in buckets],
        "values": [float(value) for value in buckets.values()],
    }


def serialize_inventory(vehicles, purchases=None, users=None, request_user=None, pagination=None, contact_messages=None, brands_source=None):
    vehicles = list(vehicles)
    purchases = list(purchases or [])
    users = list(users or [])
    items = [serialize_vehicle(vehicle) for vehicle in vehicles]
    brands = sorted({vehicle.make for vehicle in (brands_source or vehicles)})
    serialized_purchases = [serialize_purchase(purchase) for purchase in purchases]
    serialized_users = [serialize_user(user) for user in users]
    current_user_purchases = serialized_purchases
    if request_user and request_user.is_authenticated and not request_user.is_superuser:
        current_user_purchases = [purchase for purchase in serialized_purchases if purchase["userId"] == request_user.pk]

    return {
        "vehicles": items,
        "brands": brands or ["BMW", "Mercedes", "Audi", "Toyota", "Honda", "Hyundai", "Kia", "Tesla", "Ford", "Mahindra", "Tata"],
        "purchases": serialized_purchases,
        "userPurchases": current_user_purchases,
        "users": serialized_users,
        "contactMessages": [serialize_contact_message(message) for message in (contact_messages or [])],
        "stats": build_stats(vehicles, purchases, users),
        "revenueChart": build_revenue_chart(purchases),
        "pagination": pagination or {},
    }
