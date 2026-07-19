from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory, TestCase

from . import views


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
