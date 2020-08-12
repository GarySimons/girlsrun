# Code used here is taken from Code Institude's E-Commerce lesson.

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


def update_on_save(sender, instance, created, **kwargs):
