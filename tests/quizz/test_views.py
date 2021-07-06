from django.test import TestCase, Client
from django.urls import reverse


class TestHomeView(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse("quizz:home")

    def test_homepage(self):
        # check that reverse the home template
        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "quizz/home.html")
