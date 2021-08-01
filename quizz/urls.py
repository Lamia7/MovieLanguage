from django.urls import path

from . import views

app_name = "quizz"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("quizz_list/", views.QuizzListView.as_view(), name="quizz_list"),
    path("quizz/<int:pk>/", views.QuizzDetailView.as_view(), name="quizz"),
    path("quizz/result/<int:pk>/", views.result, name="result"),
]
