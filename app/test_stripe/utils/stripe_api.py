import stripe

from django.conf import settings
from django.urls import reverse


stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


def create_checkout_session_for_item(item, request):
    line_items = [
        {
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }
    ]
    return stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('succes')) + "?session_id={CHECKOUT_SESSION_ID}"
    )


def get_stripe_config():
    return {'publicKey': settings.STRIPE_TEST_PUBLIC_KEY}
