from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import Client, TestCase
from django.urls import reverse

from inventory.models import Vehicle
from purchases.models import Purchase
from purchases.services import purchase_vehicle

User = get_user_model()


class PurchaseServiceTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="customer",
            email="customer@example.com",
            password="StrongPass123!",
        )
        self.vehicle = Vehicle.objects.create(
            make="BMW",
            model="X5",
            category="Luxury SUV",
            price=Decimal("78500.00"),
            quantity=2,
            description="Luxury SUV",
        )

    def test_purchase_decreases_quantity(self):
        purchase = purchase_vehicle(user=self.user, vehicle_id=self.vehicle.pk, quantity=1)
        self.vehicle.refresh_from_db()
        self.assertEqual(self.vehicle.quantity, 1)
        self.assertEqual(purchase.quantity, 1)
        self.assertEqual(purchase.purchase_price, Decimal("78500.00"))

    def test_purchase_rejects_out_of_stock(self):
        self.vehicle.quantity = 0
        self.vehicle.save(update_fields=["quantity"])
        with self.assertRaises(ValidationError):
            purchase_vehicle(user=self.user, vehicle_id=self.vehicle.pk, quantity=1)


class PurchaseViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="customer",
            email="customer@example.com",
            password="StrongPass123!",
        )
        self.vehicle = Vehicle.objects.create(
            make="Tesla",
            model="Model Y",
            category="Electric SUV",
            price=Decimal("54990.00"),
            quantity=1,
            description="Electric SUV",
        )
        self.client.login(username="customer", password="StrongPass123!")

    def test_purchase_view_creates_record(self):
        response = self.client.post(
            reverse("purchases:purchase_vehicle"),
            {"vehicle_id": self.vehicle.pk, "quantity": 1},
            HTTP_REFERER="http://testserver/inventory/",
        )
        self.assertEqual(response.status_code, 302)
        self.vehicle.refresh_from_db()
        self.assertEqual(self.vehicle.quantity, 0)
        self.assertEqual(Purchase.objects.filter(user=self.user, vehicle=self.vehicle).count(), 1)

    def test_purchase_requires_login(self):
        self.client.logout()
        response = self.client.post(
            reverse("purchases:purchase_vehicle"),
            {"vehicle_id": self.vehicle.pk, "quantity": 1},
        )
        self.assertEqual(response.status_code, 302)

    def test_purchase_history_accessible_for_user(self):
        purchase_vehicle(user=self.user, vehicle_id=self.vehicle.pk, quantity=1)
        response = self.client.get(reverse("purchases:purchase_history"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "dealer-inventory-data")
