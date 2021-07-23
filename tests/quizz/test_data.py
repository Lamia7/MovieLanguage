from django.test import TestCase
from django.db.utils import IntegrityError

from quizz.models import Language, Movie
from quizz.data import DataManager


# Integration tests
class DataTestCase(TestCase):

    def setUp(self):
        self.movie_mock = Movie.objects.create(title="CAPTAIN FANTASTIC")
        self.language_mock = Language.objects.create(name="Spanish")

    def test_save_movie_success(self):
        dm = DataManager()
        self.assertEqual(dm.save_movie(self.movie_mock), self.movie_mock)

    def test_save_movie_failed(self):
        dm = DataManager()
        #movie_mock = Movie.objects.create(title="CAPTAIN FANTASTIC")
        #dm.save_movie(movie_mock)
        dm.save_movie(self.movie_mock)
        if IntegrityError:
            movie_get = Movie.objects.get(title="CAPTAIN FANTASTIC")
        self.assertEqual(dm.save_movie(self.movie_mock), movie_get)

    def test_save_language_success(self):
        dm = DataManager()
        self.assertEqual(dm.save_language(self.language_mock), self.language_mock)

    def test_save_language_failed(self):
        pass
