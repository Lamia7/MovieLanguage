from django.db.utils import IntegrityError

from quizz.models import Language, Movie


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
