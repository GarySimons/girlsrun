from django.shortcuts import render

# Create your views here.


def coaching(request):
    """
    A view to return the coaching page
    """

    return render(request, 'coaching/coaching.html')
