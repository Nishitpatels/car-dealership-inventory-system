from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

User = get_user_model()


class DashboardTests(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="StrongPass123!",
        )
        self.user = User.objects.create_user(
            username="customer",
            email="customer@example.com",
            password="StrongPass123!",
        )

    def test_admin_dashboard_loads(self):
        self.client.login(username="admin", password="StrongPass123!")
        response = self.client.get(reverse("dashboard:dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "dealer-inventory-data")

    def test_user_management_lists_users(self):
        self.client.login(username="admin", password="StrongPass123!")
        response = self.client.get(reverse("dashboard:user_management"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "customer@example.com")

    def test_deactivate_user(self):
        self.client.login(username="admin", password="StrongPass123!")
        response = self.client.post(
            reverse("dashboard:deactivate_user"),
            {"user_id": self.user.pk},
        )
        self.assertRedirects(response, reverse("dashboard:user_management"))
        self.user.refresh_from_db()
        self.assertFalse(self.user.is_active)

    def test_cannot_deactivate_superuser(self):
        self.client.login(username="admin", password="StrongPass123!")
        response = self.client.post(
            reverse("dashboard:deactivate_user"),
            {"user_id": self.admin.pk},
        )
        self.assertRedirects(response, reverse("dashboard:user_management"))
        self.admin.refresh_from_db()
        self.assertTrue(self.admin.is_active)
