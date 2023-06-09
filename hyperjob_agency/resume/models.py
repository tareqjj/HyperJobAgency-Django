from django.conf import settings
from django.db import models


# Create your models here.
class Resume(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)

    class Meta:
        verbose_name_plural = 'resumes'

    def __str__(self):
        return f"Author: {self.author}, Description: {self.description}"
