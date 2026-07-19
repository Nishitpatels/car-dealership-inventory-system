from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from core.models import ContactMessage

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

    def test_admin_profile_updates(self):
        self.client.login(username="admin", password="StrongPass123!")
        response = self.client.post(
            reverse("dashboard:profile"),
            {
                "first_name": "Admin",
                "last_name": "Manager",
                "email": "manager@example.com",
            },
        )
        self.assertRedirects(response, reverse("dashboard:profile"))
        self.admin.refresh_from_db()
        self.assertEqual(self.admin.first_name, "Admin")
        self.assertEqual(self.admin.email, "manager@example.com")

    def test_contact_messages_visible_to_admin(self):
        ContactMessage.objects.create(
            name="Alex",
            email="alex@example.com",
            subject="Availability",
            message="Is this SUV available?",
        )
        self.client.login(username="admin", password="StrongPass123!")
        response = self.client.get(reverse("dashboard:contact_messages"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "alex@example.com")

    def test_delete_contact_message(self):
        message = ContactMessage.objects.create(
            name="Alex",
            email="alex@example.com",
            subject="Availability",
            message="Is this SUV available?",
        )
        self.client.login(username="admin", password="StrongPass123!")
        response = self.client.post(reverse("dashboard:delete_contact_message"), {"message_id": message.pk})
        self.assertRedirects(response, reverse("dashboard:contact_messages"))
        self.assertFalse(ContactMessage.objects.filter(pk=message.pk).exists())


class InviteUserTests(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="StrongPass123!",
        )
        self.client.login(username="admin", password="StrongPass123!")

    def test_invite_user_page_requires_admin(self):
        self.client.logout()
        response = self.client.get(reverse("dashboard:invite_user"))
        self.assertEqual(response.status_code, 302)

    def test_invite_user_creates_account(self):
        response = self.client.post(
            reverse("dashboard:invite_user"),
            {
                "first_name": "Jamie",
                "last_name": "Lee",
                "username": "jamielee",
                "email": "jamie@example.com",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
                "is_active": "on",
            },
        )
        self.assertRedirects(response, reverse("dashboard:user_management"))
        user = User.objects.get(username="jamielee")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.check_password("StrongPass123!"))

    def test_invite_user_rejects_duplicate_username(self):
        User.objects.create_user(
            username="existing",
            email="existing@example.com",
            password="StrongPass123!",
        )
        response = self.client.post(
            reverse("dashboard:invite_user"),
            {
                "first_name": "Test",
                "last_name": "User",
                "username": "existing",
                "email": "new@example.com",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.filter(email="new@example.com").count(), 0)

    def test_invite_user_rejects_duplicate_email(self):
        User.objects.create_user(
            username="userone",
            email="shared@example.com",
            password="StrongPass123!",
        )
        response = self.client.post(
            reverse("dashboard:invite_user"),
            {
                "first_name": "Test",
                "last_name": "User",
                "username": "usertwo",
                "email": "shared@example.com",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username="usertwo").exists())

    def test_invite_user_rejects_password_mismatch(self):
        response = self.client.post(
            reverse("dashboard:invite_user"),
            {
                "first_name": "Test",
                "last_name": "User",
                "username": "mismatch",
                "email": "mismatch@example.com",
                "password1": "StrongPass123!",
                "password2": "DifferentPass123!",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username="mismatch").exists())

    def test_invited_user_appears_in_user_management(self):
        self.client.post(
            reverse("dashboard:invite_user"),
            {
                "first_name": "Nina",
                "last_name": "Patel",
                "username": "ninapatel",
                "email": "nina@example.com",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
                "is_active": "on",
                "is_staff": "on",
            },
        )
        response = self.client.get(reverse("dashboard:user_management"))
        self.assertContains(response, "ninapatel")
        self.assertContains(response, "nina@example.com")
        user = User.objects.get(username="ninapatel")
        self.assertTrue(user.is_staff)

    def test_regular_user_cannot_invite_users(self):
        self.client.logout()
        User.objects.create_user(
            username="customer",
            email="customer@example.com",
            password="StrongPass123!",
        )
        self.client.login(username="customer", password="StrongPass123!")
        response = self.client.get(reverse("dashboard:invite_user"))
        self.assertEqual(response.status_code, 403)
