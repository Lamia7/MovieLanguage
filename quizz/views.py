from quizz.models import Question, Quizz
from django.shortcuts import render
from django.views.generic import ListView, DetailView


# Create your views here.
def home(request):
    """Displays the home page

    Args:
        request (obj): Django object to generate response

    Returns:
        str: Template file
    """
    return render(request, "quizz/home.html")


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
        return context
