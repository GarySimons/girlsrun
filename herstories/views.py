from django.shortcuts import render
from .models import Herstory

# Create your views here.

def herstories(request):
    """ A view to return the Her Stories page """

    herstories = Herstory.objects.all()

    context = {
        'herstories': herstories,
    }

    return render(request, 'herstories/herstories.html', context)
