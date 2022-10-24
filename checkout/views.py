from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LwVjqIEspgfEafdLVNPZIdDDvbg0tW4GdnTSmpdFEoWL6g5IhLPdsaBnBzkLvvav8ZEpDTK9HHeS77UBh6mvoYg00SeRraaRq',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
