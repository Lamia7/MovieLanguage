from django.db.utils import IntegrityError

from quizz.models import Language, Movie, Question, Answer


class DataManager:
    """Manages data (save)
    """

    def save_movie(self, movie):
        movie_obj = Movie.objects.create(title=movie)
        return movie_obj

    def save_language(self, language):
        try:
            language.save()
        except IntegrityError:
            language = Language.objects.get(name=language)
        return language

    def save_question(self, question, quizz):
        question = Question.objects.create(
            question_content=question,
            quizz=quizz
        )
        return question

    def save_answers(self, answer_text, question_obj, is_solution):
        answer = Answer.objects.create(
            answer_content=answer_text,
            is_correct=is_solution,
            question=question_obj
        )
        return answer
