from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.

class Collections(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=24)
    description = models.CharField(max_length=240)
    movies = models.TextField(blank=True, null=True, default=list())

    def __str__(self):
        return self.title





