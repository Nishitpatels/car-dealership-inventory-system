from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class Purchase(models.Model):
    STATUS_COMPLETED = "Completed"
    STATUS_CHOICES = [
        (STATUS_COMPLETED, "Completed"),
    ]

    vehicle = models.ForeignKey(
        "inventory.Vehicle",
        on_delete=models.PROTECT,
        related_name="purchases",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="vehicle_purchases",
    )
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    purchase_price = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=STATUS_COMPLETED)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["user", "created_at"]),
            models.Index(fields=["vehicle", "created_at"]),
            models.Index(fields=["status"]),
        ]

    def __str__(self):
        return f"PUR-{self.pk:05d} · {self.vehicle} · {self.user}"

    @property
    def total_price(self):
        return self.purchase_price * self.quantity
