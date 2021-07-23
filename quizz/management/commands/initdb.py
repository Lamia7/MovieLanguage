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
            except IntegrityError as e:  # Avoid duplicates
                print("Error, unable to save quizz: ", e)
            continue
