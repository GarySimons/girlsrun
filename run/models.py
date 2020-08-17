from django.db import models
from django.conf import settings


class Run(models.Model):
    """
    Model for upcoming runs
    """
    date = models.CharField(max_length=254, null=False, blank=False)
    location = models.CharField(max_length=254, null=False, blank=False)
    distance = models.IntegerField(null=False, blank=False)
    description = models.TextField(default='some string')
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.date