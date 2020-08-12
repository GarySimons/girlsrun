from django import template

# Code used here is adapted from Code Institude's E-Commerce lesson.

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity