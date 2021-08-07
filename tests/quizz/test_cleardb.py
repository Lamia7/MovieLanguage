from django.test import TestCase
from django.core.management import call_command

from quizz.models import Quizz, Language, Movie


# Integration tests
class ClearDbTestCase(TestCase):

    def setUp(self):
        self.movie_mock = Movie.objects.create(title="CAPTAIN FANTASTIC")
        self.language_mock = Language.objects.create(name="Spanish")
        self.quizz_mock = Quizz.objects.create(
                title="CAPTAIN FANTASTIC",
                movie=self.movie_mock,
                language=self.language_mock
        )

    def test_clear_data_from_database_success(self):
        call_command('cleardb')
        quizz_quantity = Quizz.objects.all().count()
        self.assertEqual(quizz_quantity, 0)
