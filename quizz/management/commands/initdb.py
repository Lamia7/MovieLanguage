import json

from django.core.management.base import BaseCommand  # CommandError?
from django.db.utils import IntegrityError

from quizz.models import Language, Quizz, Movie
from quizz.data import DataManager


class Command(BaseCommand):
    help = 'Initialize database with quizzes'

    def handle(self, *args, **kwargs):
        """Initialize database with quizzes from JSON file"""

        dm = DataManager()

        # Convert data from JSON file into Python objects
        with open('quizz/quizz_data.json') as f:
            data = json.load(f)

        # Loop into quizzes
        for quizz in data['quizzes']:
            title = quizz['title'].upper()
            movie_obj = Movie(title=quizz['movie'].upper())
            movie_obj = dm.save_movie(movie_obj)

            language_obj = Language(name=quizz['language'].capitalize())
            language_obj = dm.save_language(language_obj)

            question_qty = len(quizz['questions'])

            # Instanciate quizz object
            quizz_obj = Quizz(
                title=title,
                movie=movie_obj,
                language=language_obj,
                question_quantity=question_qty
            )
            # print(f"QUIZZ: {quizz_obj}, LANG: {quizz_obj.language}, MOV: {quizz_obj.movie}")  # noqa E501
            # print("----------")

            # Saves quizz object
            try:
                quizz_obj.save()
            except ValueError as e:
                print("Error, unable to save quizz: ", e)
            except IntegrityError:  # Avoid duplicates
                # print("Error, unable to save quizz: ", e)
                quizz_obj = Quizz.objects.get(title=title)
            # dm.save_questions(quizz['questions'])
            # contient question, rép, solution
            for question_item in quizz['questions']:
                question_obj = dm.save_question(question_item['question'], quizz_obj)
                print(f"question obj: {question_obj}")
                # print(f"TYPE: {type(question['answers'])} - ANSWERS {question['answers']}")

                # save answer
                solution = question_item['solution']
                # pr chq dict réponse dans la liste de réponses
                for answer in question_item['answers']:
                    # pr chq clé de chq dict de réponse
                    for key in answer.keys():
                        # print(f"ANSWERS {answer[key]}")
                        # si la clé dans le dict de réponse et = à solution
                        if key == solution:
                            is_solution = True
                            # print(f"c'est la bonne réponse: {key}")
                        else:
                            is_solution = False
                        # enregistrer réponse
                        answer_obj = dm.save_answers(answer[key], question_obj, is_solution)
                        # answer_obj = dm.save_answers(question_item, question_obj)
            print(f"answer_obj: {answer_obj}")
            print("--------------------")
            continue
