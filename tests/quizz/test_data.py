from django.test import TestCase
# from django.db.utils import IntegrityError

from quizz.models import Language, Movie, Quizz, Question, Answer
from quizz.data import DataManager


# Unit tests
class DataTestCase(TestCase):

    def setUp(self):
        self.movie_mock = Movie.objects.create(title="CAPTAIN FANTASTIC")
        self.language_mock = Language.objects.create(name="Spanish")
        self.quizz_mock = Quizz.objects.create(
            title="CAPTAIN FANTASTIC",
            movie=self.movie_mock,
            language=self.language_mock)
        self.question_mock = Question.objects.create(
            question_content="How many kids does Ben Cash have ?",
            quizz=self.quizz_mock)
        self.answer_mock = Answer.objects.create(
            answer_content="6",
            is_correct=True,
            question=self.question_mock)

    def test_save_movie_success(self):
        dm = DataManager()
        movie = "CAPTAIN FANTASTIC"
        movie_saved = dm.save_movie(movie)
        self.assertEqual(movie_saved.title, self.movie_mock.title)

    def test_save_language_success(self):
        dm = DataManager()
        self.assertEqual(
            dm.save_language(self.language_mock), self.language_mock)

    def test_save_language_failed(self):
        pass

    # TODO: Create a test with an expected mock that has
    # not been saved already
    # def test_save_quizz_success(self):
    #     dm = DataManager()
    #     self.assertEqual(
    #         dm.save_quizz(
    #             title="CAPTAIN FANTASTIC",
    #             movie=self.movie_mock,
    #             language=self.language_mock,
    #             question_qty=3
    #         ),
    #         self.quizz_mock
    #     )

    def test_save_question_success(self):
        dm = DataManager()
        question_saved = dm.save_question(
            "How many kids does Ben Cash have ?", self.quizz_mock)
        self.assertEqual(
            question_saved.question_content,
            self.question_mock.question_content
        )

    def test_save_answers_success(self):
        dm = DataManager()
        answer_saved = dm.save_answers(
            "6", self.question_mock, True)
        self.assertEqual(
            answer_saved.answer_content,
            self.answer_mock.answer_content
        )
