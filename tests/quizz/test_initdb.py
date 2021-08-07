from unittest import mock
from django.test import TestCase
from django.core.management import call_command

from quizz.models import Quizz, Language, Movie, Question, Answer


# Mock json data
mock_data = {
    "quizzes": [
        {
            "title": "Harry Potter I",
            "movie": "Harry Potter I",
            "question_quantity": "",
            "required_score_to_pass": "",
            "language": "english",
            "questions": [
                {
                    "question": "Where is located Harry's bedroom in the Dursleys' house ?",  # noqa: E501
                    "answers": [
                        {"A": "In the basement"},
                        {"B": "Under the stairs"},
                        {"C": "In the garage"},
                        {"D": "In the yard"},
                    ],
                    "solution": "B",
                },
                {
                    "question":
                        "What speciality does professor Firenze teach ?",
                    "answers": [
                        {"A": "Divination"},
                        {"B": "Flying"},
                        {"C": "Herbology"},
                        {"D": "Potions"},
                    ],
                    "solution": "A",
                },
            ],
        },
    ]
}


class InitDbTestCase(TestCase):
    def load_data(self, data):
        # Create a 'mock' object for the method load from json
        with mock.patch("json.load") as json_load:
            # Now json.load will return your data from the test
            json_load.return_value = data
            call_command("initdb")

    def test_feed_database_with_json_data_success(self):
        data = mock_data
        self.load_data(data)

        self.assertEqual(Quizz.objects.count(), 1)
        self.assertEqual(Movie.objects.count(), 1)
        self.assertEqual(Language.objects.count(), 1)
        self.assertEqual(Question.objects.count(), 2)
        self.assertEqual(Answer.objects.count(), 8)
