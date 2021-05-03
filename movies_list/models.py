from django.db import models
from django.conf import settings


# Create your models here.

class Collections(models.Model):

    title = models.CharField(max_length=24)
    description = models.CharField(max_length=240)
    movies = models.TextField(blank=True, null=True, default=list())

    def __str__(self):
        return self.title

# class Movielist(models.Model):

#     uuid = models.CharField(max_length=240)
#     title = models.CharField(max_length=24)
#     description = models.CharField(max_length=240)
#     genres = models.CharField(max_length=240)

#     # def __str__(self):
#     #     return self.title




