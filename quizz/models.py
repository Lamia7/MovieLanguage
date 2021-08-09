from django.db import models
from django.utils.translation import gettext as _


class Language(models.Model):
    name = models.CharField(
        max_length=50,
        # null=True,
        unique=True,
        verbose_name=_("langue"),
    )

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=300, verbose_name=_("titre film"))

    def __str__(self):
        return self.title


class Quizz(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True,
        verbose_name=_("titre quizz"),
    )
    movie = models.ForeignKey(
        "Movie",
        on_delete=models.SET_NULL,
        verbose_name=_("film"),
        null=True,
        related_name="quizz"
    )
    date = models.DateTimeField(auto_now_add=True)
    required_score_to_pass = models.IntegerField(
        help_text="Score minimum attendu (%)",
        default=50,
        verbose_name=_("score minimum")
    )
    language = models.ForeignKey(
        "Language",
        on_delete=models.SET_NULL,
        verbose_name=_("langue"),
        null=True,
        related_name="quizz"
    )

    class Meta:
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.title


class Question(models.Model):
    question_content = models.CharField(
        max_length=900,
        verbose_name=_("question"),
    )
    quizz = models.ForeignKey(
        "Quizz",
        on_delete=models.CASCADE,
        related_name="questions"
    )

    def __str__(self):
        return self.question_content


class Answer(models.Model):
    answer_content = models.CharField(
        max_length=900,
        verbose_name=_("réponse"),
    )
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(
        "Question", on_delete=models.CASCADE, related_name="answers"
    )

    def __str__(self):
        return f"QUESTION: {self.question} - REPONSE: {self.answer_content} - CORRECT: {self.is_correct}"  # noqa: E501


class Result(models.Model):
    quizz = models.ForeignKey("Quizz", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    score = models.FloatField(blank=True)

    def __str__(self):
        return f"USER: {self.user} - QUIZZ: {self.quizz} - SCORE: {self.score}"  # noqa: E501
