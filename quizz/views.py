from django.shortcuts import redirect, render
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
    # TODO : paginate_by = 9


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
    questions_quantity = Question.objects.filter(quizz=pk).count()
    total_submitted_answers = 0  # initiate counter
    total_correct_answers = 0

    # Convert request.POST into python dict
    submitted_choices = dict(request.POST)

    # Get responses into dict_values type & convert to list
    values_resp = list(submitted_choices.values())
    values_resp.pop(0)  # removes csrf token

    # Check if user passes quizz
    for element in values_resp:
        total_submitted_answers += 1
        # Get first element of each values_resp list
        answer_string = element[0]
        if answer_string.__contains__("CORRECT: True"):
            total_correct_answers += 1

    # Check if all questions have been replied
    if total_submitted_answers != questions_quantity:
        # TODO: Add a message to inform user all answers have not been replied
        return redirect('quizz:quizz', pk)

    # Calculate result
    result = int((total_correct_answers / questions_quantity) * 100)
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


class LegalNoticeView(TemplateView):
    """CBV that displays the legal notice page"""

    template_name = "quizz/legal_notice.html"
