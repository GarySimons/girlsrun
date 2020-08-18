from django.db import models
from django.conf import settings


class Story(models.Model):
    """
    Model for Herstories page
    """
    class Meta:
        verbose_name_plural = 'Stories'

    full_name = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    occupation = models.CharField(max_length=254, null=False, blank=False)
    details = models.TextField(default='some string')
    image = models.ImageField()

    def __str__(self):
        return self.full_name