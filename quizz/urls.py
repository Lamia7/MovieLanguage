from django.urls import path

from . import views

app_name = "quizz"
urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("quizz_list/", views.QuizzListView.as_view(), name="quizz_list"),
]
