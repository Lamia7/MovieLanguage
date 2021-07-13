from django.test import TestCase
from django.urls import reverse

from users.models import User


class TestUsersViews(TestCase):
    def setUp(self):
        self.register_url = reverse("users:register")
        self.account_url = reverse("users:account")

    # Unit test
    def test_display_register_page(self):
        self.assertEqual(self.client.get(self.register_url).status_code, 200)
        self.assertTemplateUsed(self.client.get(
            self.register_url), "users/register.html"
        )
        self.assertContains(self.client.get(self.register_url), "username")
        self.assertContains(self.client.get(self.register_url), "email")
        self.assertContains(self.client.get(self.register_url), "password1")
        self.assertContains(self.client.get(self.register_url), "password2")

    # Integration test
    def test_registration_success(self):
        data = {
            "username": "user1",
            "email": "user1@gmail.com",
            "password1": "userpassword1",
            "password2": "userpassword1",
        }

        response = self.client.post(self.register_url, data)
        self.assertEqual(User.objects.count(), 1)
        self.assertRedirects(response, reverse("users:login"))
        self.assertEqual(response.status_code, 302)

    def test_registration_failed(self):
        data = {
            "username": "user1",
            "password1": "userpassword1",
        }

        response = self.client.post(self.register_url, data)
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(response.status_code, 200)

    def test_display_account_page(self):
        # check that reverse the account template
        user = User.objects.create_user(
            username="user1",
            email="user1@gmail.com",
            password="password1234",
        )
        self.client.force_login(user)

        response = self.client.get(self.account_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/account.html")
