from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from quizz.models import Question, Quizz


class HomeView(TemplateView):
    """CBV that displays the home page"""

    template_name = "quizz/home.html"


class QuizzListView(ListView):
    """CBV that displays the quizz_list page"""

    model = Quizz
    template_name = "quizz/quizz_list.html"
    context_object_name = "quizz_list"
    # paginate_by = 9


class QuizzDetailView(DetailView):
    """CBV that displays the quizz page"""

    model = Quizz
    template_name = "quizz/quizz.html"
    context_object_name = "quizz"

    def get_context_data(self, **kwargs):
        context = super(QuizzDetailView, self).get_context_data(**kwargs)
        context["questions"] = Question.objects.filter(quizz=self.kwargs["pk"])
        # context['quizz'] = Quizz.objects.get(pk=self.kwargs['pk'])
        return context


def result(request, pk):
    # Convert request.POST into python dict
    submitted_choices = dict(request.POST)

    # TODO: check if all questions have been answered
    # 1- count the number of elements in responses
    # 2- get number of questions in a quizz
    # 3- compare both results
    # 4- if same result then continue
    # 5- if not, redirect to quizz
    # =================

    # Initiate counter of correct responses
    correct_answers = 0

    # Get responses into dict_values type
    values_resp = submitted_choices.values()

    # Check if user passes quizz
    for element in values_resp:
        # Get first element of each values_resp list
        answer_string = element[0]
        if answer_string.__contains__("CORRECT: True"):
            correct_answers += 1

    # Calculate result
    questions_quantity = Question.objects.filter(quizz=pk).count()
    result = int((correct_answers / questions_quantity) * 100)
    quizz_title = Quizz.objects.get(pk=pk).title

    if result >= 50:  # If 50% user passes
        result_message = "Bravo! Vous avez validé ce quizz."
    else:
        result_message = (
            "Aïe, vous n'avez pas validé ce quizz. Une autre fois peut-être."
        )

    context = {
        "pk": pk,
        "result": result,
        "result_message": result_message,
        "quizz_title": quizz_title,
    }

    return render(request, "quizz/result.html", context=context)
