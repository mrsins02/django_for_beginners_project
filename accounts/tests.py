from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class AccountTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="testuser",
                                            email="testmail@google.com",
                                            password="admin")

    def test_user_model(self):
        self.assertEqual(User.objects.all()[0].username, "testuser")
        self.assertEqual(User.objects.all()[0].email, "testmail@google.com")

    def test_login(self):
        response = self.client.get("/accounts/login/")
        reverse_response = self.client.get(reverse("login"))
        post_response = self.client.post(reverse("login"),
                                         {"username": "testuser",
                                          "password": "admin"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(reverse_response.status_code, 200)
        self.assertTemplateUsed(reverse_response, "registration/login.html")
        self.assertEqual(post_response.status_code, 302)

    def test_logout(self):
        response = self.client.get("/accounts/logout/")
        reverse_response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(reverse_response.status_code, 302)

    def test_signup(self):
        response = self.client.get("/accounts/sign-up/")
        reverse_response = self.client.get(reverse("sign_up"))
        post_response = self.client.post(reverse("sign_up"),
                                         {"username": "testuser2",
                                          "email": "testuser2@gmail.com",
                                          "password1": "admin",
                                          "password2": "admin"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(reverse_response.status_code, 200)
        self.assertTemplateUsed(reverse_response, "accounts/sign-up.html")
        self.assertEqual(post_response.status_code, 200)
        self.assertEqual(User.objects.all().count(), 2)
        self.assertEqual(User.objects.all()[1].username, "testuser2")
        self.assertEqual(User.objects.all()[1].email, "testuser2@gmail.com")

