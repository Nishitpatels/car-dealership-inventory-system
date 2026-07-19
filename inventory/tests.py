from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from inventory.models import Vehicle

User = get_user_model()


class VehicleModelTests(TestCase):
    def test_availability_status(self):
        vehicle = Vehicle.objects.create(
            make="BMW",
            model="X5",
            category="Luxury SUV",
            price=Decimal("50000.00"),
            quantity=0,
            description="Test vehicle",
        )
        self.assertEqual(vehicle.availability, "Out of Stock")

        vehicle.quantity = 2
        self.assertEqual(vehicle.availability, "Low Stock")

        vehicle.quantity = 5
        self.assertEqual(vehicle.availability, "Available")


class VehicleSearchTests(TestCase):
    def setUp(self):
        Vehicle.objects.create(
            make="BMW",
            model="X5",
            category="Luxury SUV",
            price=Decimal("78500.00"),
            quantity=4,
            description="Luxury SUV",
        )
        Vehicle.objects.create(
            make="Hyundai",
            model="Creta",
            category="Compact SUV",
            price=Decimal("27600.00"),
            quantity=9,
            description="Compact SUV",
        )

    def test_search_by_make(self):
        response = self.client.get(reverse("inventory:inventory"), {"make": "BMW"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BMW")
        self.assertNotContains(response, "Hyundai Creta")

    def test_search_by_model(self):
        response = self.client.get(reverse("inventory:search_results"), {"model": "Creta"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Creta")

    def test_search_by_category(self):
        response = self.client.get(reverse("inventory:search_results"), {"category": "Compact SUV"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Creta")

    def test_search_by_price_range(self):
        response = self.client.get(
            reverse("inventory:search_results"),
            {"min_price": "70000", "max_price": "90000"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BMW")
        self.assertNotContains(response, "Creta")

    def test_combined_search_filters(self):
        response = self.client.get(
            reverse("inventory:search_results"),
            {
                "make": "BMW",
                "model": "X5",
                "category": "Luxury SUV",
                "min_price": "70000",
                "max_price": "90000",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BMW")
        self.assertNotContains(response, "Hyundai")


class VehicleAdminCrudTests(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="StrongPass123!",
        )
        self.client.login(username="admin", password="StrongPass123!")
        self.vehicle = Vehicle.objects.create(
            make="Audi",
            model="A6",
            category="Luxury Sedan",
            price=Decimal("62000.00"),
            quantity=3,
            description="Executive sedan",
        )

    def test_manage_vehicles_requires_admin(self):
        self.client.logout()
        response = self.client.get(reverse("inventory:manage_vehicles"))
        self.assertEqual(response.status_code, 302)

    def test_add_vehicle(self):
        response = self.client.post(
            reverse("inventory:add_vehicle"),
            {
                "make": "Toyota",
                "model": "Camry",
                "category": "Sedan",
                "price": "32000.00",
                "quantity": "5",
                "description": "Reliable sedan",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Vehicle.objects.filter(make="Toyota", model="Camry").exists())

    def test_add_vehicle_rejects_negative_price(self):
        response = self.client.post(
            reverse("inventory:add_vehicle"),
            {
                "make": "Toyota",
                "model": "Camry",
                "category": "Sedan",
                "price": "-1.00",
                "quantity": "5",
                "description": "Reliable sedan",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Vehicle.objects.filter(make="Toyota", model="Camry").exists())

    def test_update_vehicle(self):
        response = self.client.post(
            f"{reverse('inventory:update_vehicle')}?id={self.vehicle.pk}",
            {
                "make": "Audi",
                "model": "A6",
                "category": "Luxury Sedan",
                "price": "64000.00",
                "quantity": "2",
                "description": "Updated executive sedan",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.vehicle.refresh_from_db()
        self.assertEqual(self.vehicle.price, Decimal("64000.00"))

    def test_delete_vehicle(self):
        response = self.client.post(f"{reverse('inventory:delete_confirmation')}?id={self.vehicle.pk}")
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Vehicle.objects.filter(pk=self.vehicle.pk).exists())

    def test_restock_vehicle(self):
        response = self.client.post(
            reverse("inventory:restock_vehicle"),
            {"vehicle_id": self.vehicle.pk, "quantity": 4},
        )
        self.assertEqual(response.status_code, 302)
        self.vehicle.refresh_from_db()
        self.assertEqual(self.vehicle.quantity, 7)

    def test_vehicle_details_404_for_missing_vehicle(self):
        response = self.client.get(f"{reverse('inventory:vehicle_details')}?id=99999")
        self.assertEqual(response.status_code, 404)
