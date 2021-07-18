from django.contrib import admin
from .models import Language, Movie, Question, Answer, Quizz, Result


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Language)
admin.site.register(Movie)
admin.site.register(Quizz)
admin.site.register(Answer)
admin.site.register(Result)
