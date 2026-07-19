from pathlib import Path

from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify

from .storage import VehicleImageStorage


vehicle_image_storage = VehicleImageStorage()


def vehicle_image_upload_path(instance, filename):
    extension = Path(filename).suffix.lower() or ".jpg"
    name = slugify(f"{instance.make}-{instance.model}") or "vehicle"
    return f"{name}{extension}"


class Vehicle(models.Model):
    CATEGORY_CHOICES = [
        ("Luxury SUV", "Luxury SUV"),
        ("Luxury Sedan", "Luxury Sedan"),
        ("Electric SUV", "Electric SUV"),
        ("Premium SUV", "Premium SUV"),
        ("SUV", "SUV"),
        ("Compact SUV", "Compact SUV"),
        ("Performance Coupe", "Performance Coupe"),
        ("Family SUV", "Family SUV"),
        ("Sedan", "Sedan"),
        ("Hatchback", "Hatchback"),
        ("Pickup", "Pickup"),
    ]

    make = models.CharField(max_length=80)
    model = models.CharField(max_length=120)
    category = models.CharField(max_length=80, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField()
    image = models.FileField(storage=vehicle_image_storage, upload_to=vehicle_image_upload_path, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at", "make", "model"]
        indexes = [
            models.Index(fields=["make"]),
            models.Index(fields=["model"]),
            models.Index(fields=["category"]),
            models.Index(fields=["price"]),
        ]

    def __str__(self):
        return f"{self.make} {self.model}"

    @property
    def availability(self):
        if self.quantity <= 0:
            return "Out of Stock"
        if self.quantity <= 2:
            return "Low Stock"
        return "Available"
