from django.db.utils import IntegrityError

from quizz.models import Language, Movie, Question, Answer


class DataManager:
    """Manages data (save)
    """

    def save_movie(self, movie):
        try:
            movie.save()
        except IntegrityError:
            movie = Movie.objects.get(title=movie)
        return movie

    def save_language(self, language):
        try:
            language.save()
        except IntegrityError:
            language = Language.objects.get(name=language)
        return language

    def save_question(self, question, quizz):
        try:
            question = Question.objects.create(
                question_content=question,
                quizz=quizz
            )
        except IntegrityError:
            question = Question.objects.get(question_content=question)
        return question

    def save_answers(self, answer_text, question_obj, is_solution):
        try:
            answer = Answer.objects.create(
                answer_content=answer_text,
                is_correct=is_solution,
                question=question_obj
            )
        except IntegrityError:
            answer = Answer.objects.get(answer_content=answer_text)
        return answer
