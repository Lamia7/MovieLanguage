import json

from django.core.management.base import BaseCommand  # CommandError?
from django.db.utils import IntegrityError

from quizz.models import Language, Quizz
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
            movie = quizz['movie'].upper()
            movie_obj = dm.save_movie(movie)

            language_obj = Language(name=quizz['language'].capitalize())
            language_obj = dm.save_language(language_obj)
            # TODO : voir si ok avec:
            # language = Language(name=quizz['language'].capitalize())
            # language_obj = dm.save_language(language)

            # TODO : delete question_quantity from model and here
            question_qty = len(quizz['questions'])

            quizz_obj = dm.save_quizz(
                title,
                movie_obj,
                language_obj,
                question_qty
            )

            # Loop into question item containing : QUESTIONS, ANSWERS, SOLUTION
            for question_item in quizz['questions']:
                # Save question into db
                question_obj = dm.save_question(
                    question_item['question'], quizz_obj)

                # Solution
                solution = question_item['solution']
                # Loop into each answer dict from answers' list
                for answer in question_item['answers']:
                    for key in answer.keys():  # key in answers' dict
                        if key == solution:
                            is_solution = True
                        else:
                            is_solution = False

                        # Save answer into DB
                        # answer_obj = dm.save_answers(
                        dm.save_answers(
                            answer[key],
                            question_obj,
                            is_solution
                        )
                        # print(f"ANSWER OBJ/ {answer_obj}")
        self.stdout.write(self.style.SUCCESS(
                    "Importing quizzes into database : SUCCESSFUL")
        )
