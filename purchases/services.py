from django.core.exceptions import PermissionDenied, ValidationError
from django.db import transaction

from inventory.models import Vehicle

from .models import Purchase


@transaction.atomic
def purchase_vehicle(*, user, vehicle_id, quantity=1):
    if not user.is_authenticated:
        raise PermissionDenied("Please log in to purchase a vehicle.")

    vehicle = Vehicle.objects.select_for_update().get(pk=vehicle_id)

    if quantity <= 0:
        raise ValidationError("Purchase quantity must be greater than zero.")

    if vehicle.quantity < quantity:
        raise ValidationError("This vehicle is out of stock.")

    vehicle.quantity -= quantity
    vehicle.save(update_fields=["quantity", "updated_at"])

    return Purchase.objects.create(
        vehicle=vehicle,
        user=user,
        quantity=quantity,
        purchase_price=vehicle.price,
    )
