from django.test import TestCase
from quizz.models import Answer, Language, Movie, Question, Quizz


class ModelsTestCase(TestCase):
    def setUp(self):
        self.movie_obj = Movie.objects.create(title="Captain Fantastic")
        self.language_obj = Language.objects.create(name="English")
        self.quizz_obj = Quizz.objects.create(
            title="Quizz1",
            movie=self.movie_obj,
            image="",
            question_quantity=5,
            date="",
            required_score_to_pass=50,
            language=self.language_obj
        )
        self.question_obj = Question.objects.create(
            question_content="How many kids does Ben Cash have ?",
            quizz=self.quizz_obj
        )

    def test_language_str(self):
        self.assertEqual(str(self.language_obj), "English")

    def test_movie_str(self):
        self.assertEqual(str(self.movie_obj), "Captain Fantastic")

    def test_quizz_str(self):
        self.assertEqual(str(self.quizz_obj), "Quizz1")

    def test_get_all_questions_of_quizz(self):
        pass

    def test_question_str(self):
        self.assertEqual(
            str(self.question_obj),
            "How many kids does Ben Cash have ?"
        )

    def test_get_all_answers_of_question(self):
        pass

    def test_answer_str(self):
        answer = Answer.objects.create(
            answer_content="6",
            is_correct=True,
            question=self.question_obj,
        )
        self.assertEqual(
            str(answer),
            "QUESTION: How many kids does Ben Cash have ? - REPONSE: 6 - CORRECT: True"  # noqa: E501
        )

    # def test_result_str(self):
    #     result = Result.objects.create(
    #         quizz="...",
    #         user="...",
    #         score=5.0,
    #     )
    #     self.assertEqual(
    #         str(result),
    #         "USER: ... - QUIZZ: ... - SCORE: 5.0"
    #     )
