from django.shortcuts import render

# Create your views here.


def beginner(request):
    """
    A view to return the getting started page
    """

    return render(request, 'beginner/beginner.html')
