from django.shortcuts import render
from .models import Run

# Create your views here.

def run(request):
    """ A view to return the Upcoming Runs page """

    run = Run.objects.all()

    context = {
        'run': run,
    }

    return render(request, 'run/run.html', context)
