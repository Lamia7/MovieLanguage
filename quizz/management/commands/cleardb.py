from django.core.management.base import BaseCommand  # CommandError?

from quizz.models import Language, Quizz, Movie, Question, Answer


class Command(BaseCommand):
    help = 'Clears data from database'

    def handle(self, *args, **kwargs):
        """Clears the database"""

        Movie.objects.all().delete()
        Language.objects.all().delete()
        Quizz.objects.all().delete()
        Question.objects.all().delete()
        Answer.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(
                    "Clearing data from database : SUCCESSFUL")
        )
