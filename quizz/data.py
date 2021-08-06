from django.db.utils import IntegrityError

from quizz.models import Language, Movie, Quizz, Question, Answer


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

    def save_quizz(self, title, movie, language, question_qty):
        # Saves quizz object
        try:
            # Instanciate quizz object
            quizz_obj = Quizz.objects.create(
                    title=title,
                    movie=movie,
                    language=language,
                    question_quantity=question_qty
            )
        except ValueError as e:
            print("Error, unable to save quizz: ", e)
        except IntegrityError:  # Avoid duplicates
            # print("Error, unable to save quizz: ", e)
            quizz_obj = Quizz.objects.get(title=title)
        return quizz_obj

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
