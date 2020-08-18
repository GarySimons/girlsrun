from django.shortcuts import render
from .models import Story

# Create your views here.

def stories(request):
    """ A view to return the Herstories page """

    stories = Story.objects.all()

    context = {
        'stories': stories,
    }

    return render(request, 'stories/stories.html', context)
