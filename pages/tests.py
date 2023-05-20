from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def test_home_page(self):
        response = self.client.get("/")
        reverse_response = self.client.get(reverse("home_page"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(reverse_response.status_code, 200)
        self.assertTemplateUsed(reverse_response, "pages/home.html")


class ContactUsPageTests(SimpleTestCase):
    def test_contact_us_page(self):
        response = self.client.get("/contact-us/")
        reverse_response = self.client.get(reverse("contact_us"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(reverse_response.status_code, 200)
        self.assertTemplateUsed(reverse_response, "pages/contact-us.html")
