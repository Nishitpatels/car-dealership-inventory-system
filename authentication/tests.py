from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

User = get_user_model()


class UserRegistrationTests(TestCase):
    def test_register_creates_user(self):
        response = self.client.post(
            reverse("authentication:register"),
            {
                "first_name": "Alex",
                "last_name": "Morgan",
                "username": "alexmorgan",
                "email": "alex@example.com",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
            },
        )
        self.assertRedirects(response, reverse("authentication:login"))
        self.assertTrue(User.objects.filter(username="alexmorgan").exists())

    def test_register_rejects_duplicate_username(self):
        User.objects.create_user(username="taken", email="one@example.com", password="StrongPass123!")
        response = self.client.post(
            reverse("authentication:register"),
            {
                "first_name": "Test",
                "last_name": "User",
                "username": "taken",
                "email": "two@example.com",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.filter(username="taken").count(), 1)


class UserLoginTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="customer",
            email="customer@example.com",
            password="StrongPass123!",
        )
        self.admin = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="StrongPass123!",
        )

    def test_user_login_success(self):
        response = self.client.post(
            reverse("authentication:login"),
            {"username": "customer", "password": "StrongPass123!"},
        )
        self.assertRedirects(response, reverse("core:home"))

    def test_user_login_rejects_admin_account(self):
        response = self.client.post(
            reverse("authentication:login"),
            {"username": "admin", "password": "StrongPass123!"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_admin_login_success(self):
        response = self.client.post(
            reverse("authentication:admin_login"),
            {"username": "admin", "password": "StrongPass123!"},
        )
        self.assertRedirects(response, reverse("dashboard:dashboard"))

    def test_admin_login_rejects_regular_user(self):
        response = self.client.post(
            reverse("authentication:admin_login"),
            {"username": "customer", "password": "StrongPass123!"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)


class AccessControlTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="customer",
            email="customer@example.com",
            password="StrongPass123!",
        )
        self.admin = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="StrongPass123!",
        )

    def test_dashboard_requires_superuser(self):
        self.client.login(username="customer", password="StrongPass123!")
        response = self.client.get(reverse("dashboard:dashboard"))
        self.assertEqual(response.status_code, 403)

    def test_user_dashboard_redirects_admin(self):
        self.client.login(username="admin", password="StrongPass123!")
        response = self.client.get(reverse("authentication:user_dashboard"))
        self.assertRedirects(response, reverse("dashboard:dashboard"))

    def test_anonymous_user_redirected_from_purchase_history(self):
        response = self.client.get(reverse("purchases:purchase_history"))
        self.assertEqual(response.status_code, 302)


class UserProfileTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="customer",
            email="customer@example.com",
            password="StrongPass123!",
            first_name="Old",
            last_name="Name",
        )
        self.other = User.objects.create_user(
            username="other",
            email="other@example.com",
            password="StrongPass123!",
        )
        self.client.login(username="customer", password="StrongPass123!")

    def test_user_can_update_profile(self):
        response = self.client.post(
            reverse("authentication:profile"),
            {
                "first_name": "New",
                "last_name": "Customer",
                "email": "newcustomer@example.com",
            },
        )
        self.assertRedirects(response, reverse("authentication:profile"))
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, "New")
        self.assertEqual(self.user.last_name, "Customer")
        self.assertEqual(self.user.email, "newcustomer@example.com")

    def test_profile_rejects_duplicate_email(self):
        response = self.client.post(
            reverse("authentication:profile"),
            {
                "first_name": "New",
                "last_name": "Customer",
                "email": "other@example.com",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, "customer@example.com")
