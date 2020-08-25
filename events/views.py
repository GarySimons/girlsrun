from django.shortcuts import render
from .models import Event

# Create your views here.
def event(request):
    """ A view to return the Upcoming Runs page """

    events = Event.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'event/event.html', context)
