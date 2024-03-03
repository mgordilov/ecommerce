from django.shortcuts import render, redirect

import os

import stripe

stripe.api_key = 'sk_test_51MlaPJBH5qedVa5Iw9X22b6mvAOUiO4rVOQn2B0IbXIn9xAKhnUAnlGplBRWtc2RieFaFVbJ3omxXcdx0xzXGTmM00Q1iXpIzY'

# Create your views here.
def home(request):
    return render(request, 'ecommerce_app/home.html')

def createCheckoutSession(request):
    if request.method == 'POST':
        checkout_session = stripe.checkout.Session.create(
            line_items = [
                {
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {
                            'name': 'Creating tesst checkout',
                        },
                        'unit_amount': 20000,
                    },
                    'quantity': 1,
                },
            ],
            mode = 'payment',
            success_url = 'http://example.com',
            cancel_url = 'http://localhost:8000/',
        )
        return redirect(checkout_session.url, code=303)

    else:
        return render(request, 'ecommerce_app/home.html')