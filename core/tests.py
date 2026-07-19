from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase
from django.urls import reverse

from . import views
from .models import ContactMessage


class ErrorPageTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_403_page_renders(self):
        request = self.factory.get("/restricted/")
        request.user = AnonymousUser()
        response = views.permission_denied(request, Exception("denied"))
        self.assertEqual(response.status_code, 403)
        self.assertContains(response, "dealer-inventory-data", status_code=403)

    def test_500_page_renders(self):
        request = self.factory.get("/error/")
        request.user = AnonymousUser()
        response = views.server_error(request)
        self.assertEqual(response.status_code, 500)
        self.assertContains(response, "dealer-inventory-data", status_code=500)


class ContactMessageTests(TestCase):
    def test_contact_message_is_saved(self):
        response = self.client.post(
            reverse("core:contact"),
            {
                "name": "Alex Morgan",
                "email": "Alex@Example.COM",
                "subject": "Vehicle availability",
                "message": "Is the Toyota SUV still available?",
            },
        )
        self.assertRedirects(response, reverse("core:contact"))
        message = ContactMessage.objects.get()
        self.assertEqual(message.name, "Alex Morgan")
        self.assertEqual(message.email, "alex@example.com")

    def test_contact_message_requires_fields(self):
        response = self.client.post(reverse("core:contact"), {"name": "", "email": "", "subject": "", "message": ""})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 0)
