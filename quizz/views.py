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
        context['questions'] = Question.objects.filter(quizz=self.kwargs['pk'])
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
    print(f"VALUES: {values_resp} // TYPE : {type(values_resp)}")
    for element in values_resp:
        # Get first element of each values_resp list
        answer_string = element[0]
        print(f"ELEMENT: {element} // {type(element)}")  # answer-1 etc
        # if it contains this, add 1 to counter
        if answer_string.__contains__("CORRECT: True"):
            print("oui")
            correct_answers += 1
    print(f"COUNTER:::: {correct_answers}")

    # TODO
    # 1- trouver nombre de questions dans le quizz
    # DELETE: quizz = Quizz.objects.get(pk=quizz_pk)
    questions_quantity = Question.objects.filter(quizz=pk).count()
    print(f"QUIZZ: {questions_quantity}")
    # 2- Calculer le resultat en fonction du nb de questions ds quizz
    result = int((correct_answers / questions_quantity)*100)
    print(f"RESULT : {result}")
    # 3- si res >= 50 alors c gagné
    if result >= 50:
        print("GAGNE")
    # 4- sinon c perdu
    else:
        print("GAME OVER")
    # ================

    return render(request, "quizz/result.html", context={'pk': pk})


""" TO DELETE
    # Get values of the dict
    # print(f"GET VALUES SUBMITTED: {submitted_choices.values()}")
    # print(f"TYPE VALUES SUBMITTED: {type(submitted_choices.values())}")

    # data = {}
    # data['csrf_token'] = submitted_choices.get('csrfmiddlewaretoken')
    # print(f"data['csrf_token']: {data['csrf_token']}")
"""
