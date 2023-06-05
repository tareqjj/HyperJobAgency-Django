from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.views import generic
from resume.models import Resume
from vacancy.models import Vacancy


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"


class VacancyList(generic.ListView):
    template_name = "vacancy/vacancy_list.html"

    def get_queryset(self):
        print(Vacancy.objects.all())
        return Vacancy.objects.all()


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = "login"
    template_name = "signup.html"


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "login.html"
    next_page = "/"


class CreateVacancyView(LoginRequiredMixin, CreateView):
    model = Vacancy
    fields = ["description"]
    template_name = "create_form.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display"] = True
        context['title_heading'] = "Create Vacancy"
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponseForbidden(b"Request Forbidden")


class CreateResumeView(LoginRequiredMixin, CreateView):
    model = Resume
    fields = ["description"]
    template_name = "create_form.html"
    success_url = "/"
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display"] = True
        context['title_heading'] = "Create Resume"
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponseForbidden(b"Request Forbidden")


def create_form_handler(request):
    if not request.user.is_authenticated:
        return render(request, template_name="create_form.html")
    elif request.user.is_staff:
        return redirect("vacancy/new")
    else:
        return redirect("resume/new")
