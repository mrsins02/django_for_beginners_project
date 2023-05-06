from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home_page"))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse("home_page"))
        print(response)
        self.assertTemplateUsed(response, "pages/home.html")


class ContactUsPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/contact-us/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("contact_us"))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse("contact_us"))
        print(response)
        self.assertTemplateUsed(response, "pages/contact-us.html")
