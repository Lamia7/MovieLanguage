from quizz.models import Quizz
from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.
def home(request):
    """Displays the home page

    Args:
        request (obj): Django object to generate response

    Returns:
        str: Template file
    """
    return render(request, "quizz/home.html")


# def quizz_list(request):
#     """Displays the quizz_list page

#     Args:
#         request (obj): Django object to generate response

#     Returns:
#         str: Template file
#     """
#     return render(request, "quizz/quizz_list.html")
class QuizzListView(ListView):
    """CBV that displays the quizz_list page"""
    model = Quizz
    template_name = "quizz/quizz_list.html"
