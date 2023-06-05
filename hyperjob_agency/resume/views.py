from django.shortcuts import render
from django.views import generic
from resume.models import Resume


# Create your views here.
class ResumeList(generic.ListView):
    template_name = "resume/resume_list.html"

    def get_queryset(self):
        return Resume.objects.all()
