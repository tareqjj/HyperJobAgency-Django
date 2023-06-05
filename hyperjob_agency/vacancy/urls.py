from django.urls import path

from vacancy import views
from vacancy.views import VacancyList, CreateVacancyView, CreateResumeView

urlpatterns = [
    path("vacancies", VacancyList.as_view(), name="vacancy_list"),
    path("vacancy/new", CreateVacancyView.as_view(), name="create_vacancy"),
    path("resume/new", CreateResumeView.as_view(), name="create_vacancy"),
    path("home", views.create_form_handler, name="home")
]
