from django.db import models
from django.conf import settings


class Herstory(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    occupation = models.CharField(max_length=200, null=False, blank=False)
    story = models.CharField(max_length=50, null=False, blank=False)

