from django.test import TestCase
from django.urls import reverse


class TestQuizzView(TestCase):
    def setUp(self):
        self.home_url = reverse("quizz:home")
        self.quizz_list_url = reverse("quizz:quizz_list")

    def test_homepage(self):
        # check that reverse the home template
        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "quizz/home.html")

    def test_quizz_list_page(self):
        # check that reverse the quizz_list template
        response = self.client.get(self.quizz_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "quizz/quizz_list.html")

    def test_result(self):
        # checks the result page
        pk = 2
        data = {
            "pk": 2,
            "result": 66,
            "result_message": "Bravo! Vous avez validé ce quizz.",
            "quizz_title": "Quizz numéro 2"
        }
        response = self.client.post(
            reverse("quizz:result", kwargs={'pk': pk}), data
        )

        self.assertEqual(response.status_code, 302)
