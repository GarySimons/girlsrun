from django.shortcuts import render
from .models import Run

# Create your views here.

def run(request):
    """ A view to return the Upcoming Runs page """

    runs = Run.objects.all()

    context = {
        'runs': runs,
    }

    return render(request, 'run/run.html', context)
