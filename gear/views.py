from django.shortcuts import render

# Create your views here.


def gear(request):
    """
    A view to return the Gear page under Advice
    """

    return render(request, 'gear/gear.html')
