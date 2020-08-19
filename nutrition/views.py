from django.shortcuts import render

# Create your views here.

def nutrition(request):
    """ A view to return the nutrition page   """

    return render(request, 'nutrition/nutrition.html')
