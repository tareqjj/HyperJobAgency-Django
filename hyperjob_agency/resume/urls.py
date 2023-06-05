from django.urls import path
from resume.views import ResumeList

urlpatterns = [
    path("resumes", ResumeList.as_view(), name="resume_list")
]