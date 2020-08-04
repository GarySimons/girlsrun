from django.shortcuts import render

# Create your views here.

def mystory(request):
    """ A view to return the My Story page """

    return render(request, 'mystory/mystory.html')
