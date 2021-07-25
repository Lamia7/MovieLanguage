from django.test import TestCase
from django.db.utils import IntegrityError

from quizz.models import Language, Movie, Quizz, Question, Answer
from quizz.data import DataManager


# Integration tests
class DataTestCase(TestCase):

    def setUp(self):
        self.movie_mock = Movie.objects.create(title="CAPTAIN FANTASTIC")
        self.language_mock = Language.objects.create(name="Spanish")
        self.quizz_mock = Quizz.objects.create(
            title="CAPTAIN FANTASTIC",
            movie=self.movie_mock,
            language=self.language_mock,
            question_quantity=3)
        self.question_mock = Question.objects.create(
            question_content="How many kids does Ben Cash have ?",
            quizz=self.quizz_mock)
        self.answer_mock = Answer.objects.create(
            answer_content="6",
            is_correct=True,
            question=self.question_mock)

    def test_save_movie_success(self):
        dm = DataManager()
        self.assertEqual(dm.save_movie(self.movie_mock), self.movie_mock)

    def test_save_movie_failed(self):
        dm = DataManager()
        dm.save_movie(self.movie_mock)
        if IntegrityError:
            movie_get = Movie.objects.get(title="CAPTAIN FANTASTIC")
        self.assertEqual(dm.save_movie(self.movie_mock), movie_get)

    def test_save_language_success(self):
        dm = DataManager()
        self.assertEqual(
            dm.save_language(self.language_mock), self.language_mock)

    def test_save_language_failed(self):
        pass

    def test_save_question_success(self):
        dm = DataManager()
        question_saved = dm.save_question(
            "How many kids does Ben Cash have ?", self.quizz_mock)
        self.assertEqual(
            question_saved.question_content,
            self.question_mock.question_content
        )

    def test_save_question_failed(self):
        pass

    def test_save_answers_success(self):
        dm = DataManager()
        answer_saved = dm.save_answers(
            "6", self.question_mock, True)
        self.assertEqual(
            answer_saved.answer_content,
            self.answer_mock.answer_content
        )
