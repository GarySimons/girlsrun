from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Code used here is taken from Code Institude's E-Commerce lesson.

def checkout(request):
    bag = request.session.get('bag, {}')
    if not bag:
        messages.error(request, "There's nothing in your bag")
        return redirect(reverse('products'))

        order_form = OrderForm()
        template = 'checkout/checkout.html'
        context = {
            'order_form' : order_form,
        }

        return render(request, template, context)
