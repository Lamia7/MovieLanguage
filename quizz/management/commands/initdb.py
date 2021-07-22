import json

from django.core.management.base import BaseCommand  # CommandError?
from django.db.utils import IntegrityError

from quizz.models import Language, Quizz, Movie
from quizz.data import DataManager


class Command(BaseCommand):
    help = 'Initialize database with quizzes'

    # METHODE save_quizz(self, data)

    def handle(self, *args, **kwargs):
        """Initialize database with quizzes from JSON file"""

        dm = DataManager()

        # Convert data from JSON file into Python objects
        with open('quizz/quizz_data.json') as f:
            data = json.load(f)

        # Loop into quizzes
        for quizz in data['quizzes']:
            # transforme le titre en upper case
            title = quizz['title'].upper()
            # print(title)
            # transforme movie en upper case
            movie_obj = Movie(title=quizz['movie'].upper())
            # print(movie_obj)
            dm.save_movie(movie_obj)
            # try:
            #     movie_obj.save()
            # except IntegrityError:
            #     movie_obj = Movie.objects.get(title=movie_obj)
            # capitalize language
            language_obj = Language(name=quizz['language'].capitalize())
            # print(language_obj)
            language_obj = dm.save_language(language_obj)
            # try:
            #     language_obj.save()
            # except IntegrityError:
            #     language_obj = Language.objects.get(name=language_obj)
            # quizz['language'].capitalize()
            # compte nombre de questions
            question_qty = len(quizz['questions'])
            # print(question_qty)
            print("----------")
            # instancier un objet quizz
            quizz_obj = Quizz(
                title=title,
                movie=movie_obj,
                language=language_obj,
                question_quantity=question_qty
            )
            print(f"QUIZZ: {quizz_obj}, LANG: {quizz_obj.language}, MOV: {quizz_obj.movie}")  # noqa E501
            print("----------")
            # essaie de l'enregistrer
            try:
                quizz_obj.save()
            except ValueError as e:
                print("Error, unable to save quizz: ", e)
            except IntegrityError as e:
                print("Error, unable to save quizz: ", e)
                # enregistre language, linking them to Quizz obj
                # except IntegrityError:  Avoid duplicated language
                # récupérer quizz_obj = Language.objects.get(name=language)
            continue
