from django.test import TestCase
from django.core.management import call_command

from quizz.models import Quizz, Language, Movie, Question, Answer
from quizz.data import DataManager


# Mock json data
mock_data = {
    "quizz":
        {
            "title": "Harry Potter I",
            "movie": "Harry Potter I",
            "image": "",
            "question_quantity": "",
            "required_score_to_pass": "",
            "language": "english",
            "questions": [
                {
                    "question": "Where is located Harry's bedroom in the Dursleys' house ?",
                    "answers": [
                        {
                            "A": "In the basement"
                        },
                        {
                            "B": "Under the stairs"
                        },
                        {
                            "C": "In the garage"
                        },
                        {
                            "D": "In the yard"
                        }
                    ],
                    "solution": "B"
                },
                {
                    "question": "What speciality does professor Firenze teach ?",
                    "answers": [
                        {
                            "A": "Divination"
                        },
                        {
                            "B": "Flying"
                        },
                        {
                            "C": "Herbology"
                        },
                        {
                            "D": "Potions"
                        }
                    ],
                    "solution": "A"
                },
            ]
        },
}


class InitDbTestCase(TestCase):

    def setUp(self):
        self.dm = DataManager()
        self.data = mock_data

    def test_feed_database_with_json_data_success(self):
        print(f"MOCK DATA TYPE: {type(self.data)}")
        call_command('initdb')

        # avec DM
        title_obj = self.data['title'].upper()
        movie_obj = self.dm.save_movie(self.data['movie'].upper())
        language_obj = self.dm.save_language(self.data['language'].capitalize())
        Quizz.objects.create(
                title=title_obj,
                movie=movie_obj,
                language=language_obj,
                question_quantity=3
        )
        # ====

        # movie_mock = Movie.objects.create(title="HARRY POTTER I")
        # language_mock = Language.objects.create(name="English")
        # Quizz.objects.create(
        #         title="HARRY POTTER I",
        #         movie=movie_mock,
        #         language=language_mock,
        #         question_quantity=3
        # )
        # ===================
        # question_mock = Question.objects.create(
        #     question_content=question,
        #     quizz=quizz
        # )

        quizz_quantity = Quizz.objects.all().count()
        self.assertEqual(quizz_quantity, 1)
