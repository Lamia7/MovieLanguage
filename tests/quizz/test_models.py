from django.test import TestCase
from quizz.models import Answer, Language, Movie, Question, Quizz


class ModelsTestCase(TestCase):
    def setUp(self):
        self.movie_data = "Captain Fantastic"

    def test_language_str(self):
        language = Language.objects.create(name="English")
        self.assertEqual(str(language), "English")

    def test_movie_str(self):
        movie = Movie.objects.create(title="Captain Fantastic")
        self.assertEqual(str(movie), "Captain Fantastic")

    def test_quizz_str(self):
        movie = Movie.objects.create(title="Captain Fantastic")
        language = Language.objects.create(name="English")
        quizz = Quizz.objects.create(
            title="Quizz1",
            movie=movie,
            image="",
            question_quantity=5,
            date="",
            required_score_to_pass=50,
            language=language
        )
        self.assertEqual(str(quizz), "Quizz1")

    def test_get_all_questions_of_quizz(self):
        pass

    def test_question_str(self):
        movie = Movie.objects.create(title="Captain Fantastic")
        language = Language.objects.create(name="English")
        quizz = Quizz.objects.create(
            title="Quizz1",
            movie=movie,
            image="",
            question_quantity=5,
            date="",
            required_score_to_pass=50,
            language=language
        )
        question = Question.objects.create(
            question_content="How many kids does Ben Cash have ?",
            quizz=quizz
        )
        self.assertEqual(str(question), "How many kids does Ben Cash have ?")

    def test_get_all_answers_of_question(self):
        pass

    def test_answer_str(self):
        movie = Movie.objects.create(title="Captain Fantastic")
        language = Language.objects.create(name="English")
        quizz = Quizz.objects.create(
            title="Quizz1",
            movie=movie,
            image="",
            question_quantity=5,
            date="",
            required_score_to_pass=50,
            language=language
        )
        question = Question.objects.create(
            question_content="How many kids does Ben Cash have ?",
            quizz=quizz
        )
        answer = Answer.objects.create(
            answer_content="6",
            is_correct=True,
            question=question,
        )
        self.assertEqual(
            str(answer),
            "QUESTION: How many kids does Ben Cash have ? - REPONSE: 6 - CORRECT: True"
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
