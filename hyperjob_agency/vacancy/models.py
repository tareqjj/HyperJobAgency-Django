from django.conf import settings
from django.db import models
from django.urls import reverse


# Create your models here.
class Vacancy(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)

    class Meta:
        verbose_name_plural = 'vacancies'

    def __str__(self):
        return f"Author: {self.author}, Description: {self.description}"
