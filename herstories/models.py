from django.db import models
from django.conf import settings


class Herstory(models.Model):
    """
    Model for Herstories page
    """
    class Meta:
        verbose_name_plural = 'Herstories'

    full_name = models.CharField(max_length=50, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    occupation = models.CharField(max_length=200, null=False, blank=False)
    story = models.CharField(max_length=500, null=False, blank=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.full_name