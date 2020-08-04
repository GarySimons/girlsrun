from django.shortcuts import render

# Create your views here.

def herstories(request):
    """ A view to return the Her Stories page """

    return render(request, 'herstories/herstories.html')
